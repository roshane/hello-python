import http.client
import json
from urllib.parse import urlparse, parse_qs
import uuid

HTTP_HEADERS = {
    "Content-Type": "application/json",
    "x-user-id": "johndoe@gmail.com",
    "Authorization" : f'Bearer {str(uuid.uuid4())}',
    "x-correlator-id": str(uuid.uuid4())
}


def _request(method="GET", port=443, host='localhost', path='', query=None, data=None, is_ssl=True):
    conn = http.client.HTTPSConnection(host, port=port) if is_ssl else http.client.HTTPConnection(host, port=port)
    url = f'{path}?{query}'
    conn.request(method=method, url=url, headers=HTTP_HEADERS, body=data if data is not None else {})
    response = conn.getresponse()
    parsed = parse_response(response)
    conn.close()
    return parsed


def parse_response(response=None):
    if response is not None:
        print('parse_response', response)
        data = response.read().decode('utf-8')
        data = data if data is None else to_json(data)
        return {
            "status": response.status,
            "reason": response.reason,
            "data": data
        }
    else:
        return None


def format_query_string(qs):
    query_map = parse_qs(qs)
    query_strings = []
    for k in iter(query_map):
        values = query_map[k]
        query_strings.append('&'.join([f'{k}={str(v)}' for v in values]))
    return '&'.join(query_strings)


def http_get(url='', query=None, callback=None):
    try:
        parsed_url = urlparse(url)
        _host = parsed_url.hostname
        _port = parsed_url.port if parsed_url.port is not None else 443 if parsed_url.scheme == 'https' else 80
        _method = 'GET'
        _path = parsed_url.path
        _get_response = None
        if parsed_url.scheme == 'https':
            _get_response = _request(method=_method, port=_port, host=_host, path=_path,
                                     query=query if query is not None else None)
        else:
            _get_response = _request(method=_method, port=_port, host=_host, path=_path,
                                     query=query if query is not None else None, is_ssl=False)
        #print('http_get', _get_response)
        return _get_response if callback is None else callback(_get_response)
    except Exception as e:
        raise f"Error http_get {str(e)}"


def http_post(url='', query=None, callback=None, data=None):
    try:
        data = json.dumps(data) if data is not None else json.dumps({})
        parsed_url = urlparse(url)
        _host = parsed_url.hostname
        _port = parsed_url.port if parsed_url.port is not None else 443 if parsed_url.scheme == 'https' else 80
        _method = 'POST'
        _path = parsed_url.path
        if parsed_url.scheme == 'https':
            _get_response = _request(method=_method, port=_port, host=_host, path=_path, data=data,
                                     query=query if query is not None else None)
        else:
            _get_response = _request(method=_method, port=_port, host=_host, path=_path, data=data,
                                     query=query if query is not None else None, is_ssl=False)
        return _get_response if callback is None else callback(_get_response)
    except Exception as e:
        raise f'Error http_post {str(e)}'


def json_to_str(data=None):
    return data if data is None else json.dumps(data, indent=2)


def to_json(data=None):
    return data if data is None else json.loads(data)


def main():
    get_url = "https://jsonplaceholder.typicode.com/todos"
    _get_response = http_get(url=get_url)
    #print('GET response: ', type(_get_response), _get_response)
    _todos = _get_response['data']
    _todo_ids = list(map(lambda it: it['id'], _todos))
    print('TODO ids: ', type(_todo_ids), _todo_ids)
    #print('typeof _get_response[data]', type(_get_response['data']))
    _post_response_list = list(map(lambda it:http_post('https://postman-echo.com/post', data=it), _todos[:3]))
    #_post_response = http_post('https://postman-echo.com/post', data=_get_response['data'])
    #print('POST response', type(_post_response), json_to_str(_post_response['data']))
    #print('POST response_list', type(_post_response_list), _post_response_list)
    for r in _post_response_list:
        print("POST response", type(r), r)
        print("\n")
    #print('typeof _post_response[data]', type(_post_response['data']))


if __name__ == "__main__":
    main()

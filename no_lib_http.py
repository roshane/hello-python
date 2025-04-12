import datetime
import http.client
import json

HTTP_HEADERS = {
    "content-type": "application/json",
    "x-user-id": "johndoe@gmail.com"
}
def request(host='localhost',
            path = "/", 
            port=8080, 
            params = None, 
            data=None, 
            method="GET"):
    conn = http.client.HTTPSConnection(host, port=port, timeout=5)
    print(f"GET params: {params} data: {str(data)} params: {params}")
    if method == "GET":
        conn.request(method, path, headers = HTTP_HEADERS)
        response = conn.getresponse()
        parsed = parse_response(response)
        conn.close()
        return parsed
    elif method == "PUT":
        raise f"Unsupported method {method}" 

def parse_response(response:None):
    if response is not None:
        return {
            "status": response.status,
            "reason": response.reason,
            "data" : response.read().decode('utf-8')
        }
    else:
       return None 

def http_get(path='',
             query=None,
             callback=None):
    pass
    
    
def dumps(data=None):
    if data is not None:
        return json.dumps(data, indent = 2)
    else:
        return None

def loads(data=None):
    if data is not None:
        return json.loads(data)
    else:
        return None


def main():
    response = request(host="jsonplaceholder.typicode.com",path="/todos/1", port=443)
    print(f"raw response type {type(response['data'])}")
    body = loads(response['data'])
    if response is not None:
        print(f"response {dumps(response)}\nbody JSON {body}")

if __name__ == "__main__":
    main()

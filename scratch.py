import urllib.parse


def format_query_string(qs):
    query_map = urllib.parse.parse_qs(qs)
    query_strings = []
    for k in iter(query_map):
        values = query_map[k]
        query_strings.append('&'.join([f'{k}={str(v)}' for v in values]))
    return '&'.join(query_strings)


if __name__ == '__main__':
    url = 'https://postman-echo.com/post?name=roshane&name=perera&age=12&email=perera@localhost.com'
    parsed = urllib.parse.urlparse(url)
    query = format_query_string(parsed.query)
    print('Result: ', query)

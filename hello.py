def application(environ, start_response):

    qs=str(environ.get(u'QUERY_STRING'))

    qs=qs.split('&')


    data=''

    for i in qs:
        data+=i+'\n'

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])


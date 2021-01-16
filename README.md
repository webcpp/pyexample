# pyexample
A example of hi.py

# install 

see `Makefile`

# benchmark

## tornado

```python
import tornado.web
import tornado.ioloop



class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello,world')

if __name__ == '__main__':
    app = tornado.web.Application([(r'/',IndexHandler)])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

```

```txt
apib -c30000 -t4 -d30 http://localhost:8888/

(5 / 30) 986.586 40% cpu
(10 / 30) 1599.549 43% cpu
(15 / 30) 1403.172 26% cpu
(20 / 30) 1837.903 27% cpu
(25 / 30) 1553.798 27% cpu
(30 / 30) 1371.989 26% cpu
Duration:             30.031 seconds
Attempted requests:   43814
Successful requests:  43814
Non-200 results:      0
Connections opened:   51237
Socket errors:        0

Throughput:           1458.964 requests/second
Average latency:      3012.726 milliseconds
Minimum latency:      159.182 milliseconds
Maximum latency:      7820.211 milliseconds
Latency std. dev:     438.022 milliseconds
50% latency:          3018.406 milliseconds
90% latency:          3438.933 milliseconds
98% latency:          3525.265 milliseconds
99% latency:          3604.970 milliseconds

Client CPU average:    31%
Client CPU max:        43%
Client memory usage:    61%

Total bytes sent:      3.11 megabytes
Total bytes received:  8.61 megabytes
Send bandwidth:        0.83 megabits / second
Receive bandwidth:     2.29 megabits / second

```
## hi.py

```nginx
    server {
        listen       80;
        server_name  pyexample;

        hi_need_kvdb off;
		hi_need_cache off;
		hi_cache_expires 1s;
		hi_need_cookies off;
		hi_need_session off;
		hi_session_expires 300s;
        hi_need_headers off;

	    location ~ \.py$ {
            rewrite ^/(.*)\.py$ /$1 break;
		    hi_python_script pyexample/index.py;
	        
	    }

        location / {
            autoindex off;
            root   pyexample/assets;
            #index  index.html index.htm;
        }
    }

```

```txt
apib -c30000 -t4 -d30 http://pyexample/test.py

(5 / 30) 16438.213 90% cpu
(10 / 30) 21110.076 100% cpu
(15 / 30) 21726.258 100% cpu
(20 / 30) 21428.534 100% cpu
(25 / 30) 21183.363 100% cpu
(30 / 30) 21060.743 99% cpu
Duration:             30.023 seconds
Attempted requests:   615791
Successful requests:  615791
Non-200 results:      0
Connections opened:   34283
Socket errors:        0

Throughput:           20510.615 requests/second
Average latency:      1300.019 milliseconds
Minimum latency:      0.297 milliseconds
Maximum latency:      7165.013 milliseconds
Latency std. dev:     2297.919 milliseconds
50% latency:          66.815 milliseconds
90% latency:          5700.949 milliseconds
98% latency:          6415.835 milliseconds
99% latency:          6538.935 milliseconds

Client CPU average:    98%
Client CPU max:        100%
Client memory usage:    65%

Total bytes sent:      37.57 megabytes
Total bytes received:  179.10 megabytes
Send bandwidth:        10.01 megabits / second
Receive bandwidth:     47.72 megabits / second

```
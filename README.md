# CMPUT 404 - Lab 2
## Ken Li

### Questions
https://uofa-cmput404.github.io/lab-2-tcp-proxy.html

### Instructions to Run
```
$ virtualenv venv --python=python3
$ source venv/bin/activate
$ pip install -r requirements.txt  // optional, no packages used

// client.py
$ python client.py

// echo_server.py
(terminal1) $ python echo_server.py
(terminal2) $ echo "Foobar" | nc localhost 8001 -q 1

// proxy_server.py and proxy_client.py
(terminal1) $ python proxy_server.py
(terminal2) $ python proxy_client.py

// multi_proxy_server.py and multi_proxy_client.py
(terminal1) $ python multi_proxy_server.py
(terminal2) $ python multi_proxy_client.py

```
### Note:
* There are no requirements need to run my programs but my `requirements.txt` includes `pylint` which my vscode installs automatically

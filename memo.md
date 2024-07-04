IP: 192.168.11.90 
ROUTER IP: 192.168.11.1
DNS IP: 192.168.11.1

interface wlan0
static_routers=192.168.11.1
static domain_name_servers=192.168.11.1
static ip_address=192.168.11.90/24

# Virtual Environment作成
```bash
py -m venv .venv
```

Activate:
```bash
. .venv/Scripts/activate
```


Deployment tutorial:
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04
import pywebio
from pywebio.platform import path_deploy

if __name__ == '__main__':
    path_deploy(base="http://10.0.0.130:8000/bob1/bob1", debug=True, ip_address='10.0.0.20', port=8000)
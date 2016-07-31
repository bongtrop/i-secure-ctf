import re
import requests

s = requests.Session()

for i in range(100):
    r = s.get("http://ctf4.isecureplayground.xyz:8000/btn/index.php")
    if i ==0:
        print "PHPSESSID="+r.cookies["PHPSESSID"]

    m = re.search(r"<p>(.+?)<br />The (.+?) number[?]<br /></p>", r.content)

    numbers = m.group(1).split(", ")
    op = m.group(2)

    numbers = map(int, numbers)
    if op == "minimum":
        res = min(numbers)
    else:
        res = max(numbers)

    payload = {"number": res, "submit": "submit"}
    r = s.post("http://ctf4.isecureplayground.xyz:8000/btn/proc.php", data=payload)

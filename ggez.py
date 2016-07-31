import socket
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("ctf2.isecureplayground.xyz",7777))

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_!-\"'/.+*%$#@^~`%&()=\\"

now = "U7CCp$M4GrrAw*ktuWB%Rz9tWg7VPaR#Xk75The_Fl@g_1s_GG"
res = ""

data = sock.recv(1024)
print data

for i in range(100):
    can = False
    for c in chars:
        if i<len(now):
            c = now[i]

        data = sock.recv(1024)
        print data

        sock.sendall(c+"\n")

        data = sock.recv(1024)
        print data

        m = re.search(r"correct", data)

        if m:
            res += c
            #print "Res: " + res
            can = True
            break

    if not can:
        print "not in set"
        exit()

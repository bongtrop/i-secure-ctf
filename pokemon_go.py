
inp = """66 52
53 21
24 29
33 64
50 22
43 8
29 37
97 8
36 61
43 8
18 20
40 57
45 25
13 44
24 88
80 19
20 91
17 34
72 29
37 60
94 20
83 1
26 24
94 11
59 57
29 70
45 8
38 15
56 51
99 13
39 20""";

lines = inp.split("\n")

res = ''

for line in lines:
    words = line.split(' ')

    res += chr(int(words[0])+int(words[1]) - 2)

print res

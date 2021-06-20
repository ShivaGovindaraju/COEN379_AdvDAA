#! /usr/bin/python3

def getZarr(string, z): 
    n = len(string) 
  
    l, r, k = 0, 0, 0
    for i in range(1, n): 
        if i > r: 
            l, r = i, i 
            while r < n and string[r - l] == string[r]: 
                r += 1
            z[i] = r - l 
            r -= 1
        else: 
            k = i - l 
            if z[k] < r - i + 1: 
                z[i] = z[k] 
            else: 
                l = i 
                while r < n and string[r - l] == string[r]: 
                    r += 1
                z[i] = r - l 
                r -= 1

s = "aaabbbaaabbbaaa"
n = len(s)
Z = [0] * n
getZarr(s, Z)
print("Z:  {}".format(Z))

Kp = [0] * n
i = n - 1
while i > 0:
  Kp[i + Z[i] -1] = Z[i]
  #print("{} {} {}".format(i+Z[i]-1, i, Kp))
  i = i - 1

print("\nKp: {}".format(Kp))

p = "aaa"
m = len(p)
w = p + "#" + s
print("W: {}".format(w))
u = len(w)
Zw = [0] * u
getZarr(w, Zw)
print("Zw:  {}".format(Zw))
Kpw = [0] * u
i = u - 1
while i > 0:
  Kpw[i + Zw[i] -1] = Zw[i]
  #print("{} {} {}".format(i+Zw[i]-1, i, Kpw))
  i = i - 1

print("\nKpw: {}".format(Kpw))
print("m {} u {}".format(m, u))
for i in range(0, n+1):
    print("i {} i+m {} kpw {}".format(i, i + m, Kpw[i + m]))
    if Kpw[i + m] == m:
        print("match found: {}".format(i - m))

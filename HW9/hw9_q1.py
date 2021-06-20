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

K = [0] * n
K[n-1] = Kp[n-1]
i = n - 2
while i > 0:
  K[i] = max(Kp[i], K[i+1]-1)
  i = i - 1

print("\nK:  {}".format(K))

t = s[::-1]
N = [0] * n
Z_t = [0] * n
getZarr(t, Z_t)
for i in range(0, n):
  N[i] = Z_t[n-1 -i]

print("\nN:  {}".format(N))

Lp = [-1] * n
for k in range(0, n):
  if N[k] > 0:
    #print("{} {}".format(n-1-N[k], k))
    Lp[n - 1 - N[k]] = k

print("\nLp: {}".format(Lp))

lp = [0] * n
last = 0
i = n - 2
while i >= 0:
  k = n - 1 - i
  if N[k-1] == k:
    lp[i] = k
    last = k
  else:
    lp[i] = last
  i = i - 1

print("\nlp: {}".format(lp))
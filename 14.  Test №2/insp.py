import time
start_time = time.time()

def p_func(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    return pi

string = 'ABACABACABACABA'
a = []
k = 0
for item in string:
    k += 1
    a.append(string[0:k])

print(a)



print()
print("time elapsed: {:.2f}s".format(time.time() - start_time))
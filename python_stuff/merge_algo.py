a1 = [12, 3, 45, 56, 1]
b1 = [33, 111, 23, 4, 222, 99, 232, 2222]
c1 = []
i = 0
j = 0
k = 0
if len(a1) <= len(b1) or len(b1) <= len(a1):
    for k in range(len(a1+b1)):
        import pdb
        pdb.set_trace()
        if a1[i] <= b1[j]:
            c1[k] = a1[i]
            i += 1
        else:
            c1[k] = b1[j]
            j += 1
        k += 1

print c1




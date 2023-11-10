A = [1, 2, 3, 4, 5, 6, 7]
A.append(0)
print(A)
n = len(A)
# print(n)
# print(A[n-1])
k = 2
c = 555
for i in range(1, n-k):
    print(i)
    j = n-i
    A[j] = A[j-1]
A[k] = c

print(A)

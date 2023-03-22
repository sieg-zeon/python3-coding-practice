# https://paiza.jp/works/mondai/dp_primer/dp_primer_recursive_formula_boss
# ・ a_1 = 1
# ・ a_2 = 1
# ・ a_n = a_{n-2} + a_{n-1} (n ≧ 3)

Q = int(input())

for i in range(Q):
    k = int(input())
    if k == 1 or k == 2:
        print(1)
    else:
        a = [0] * (k+1)
        a[1], a[2] = 1,1

        for i in range(3, k+1):
            a[i] = a[i-1] + a[i-2]
        print(a[k])

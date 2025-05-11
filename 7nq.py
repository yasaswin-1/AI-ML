def nQueens(k, n):
    for i in range(1, n + 1):
        if place(k, i):
            x[k] = i
            if k == n:
                print("Positions:", x[1:])
                for j in range(1, n + 1):
                    print(" ".join("Q" if x[j] == l else "-" for l in range(1, n + 1)))
            else:
                nQueens(k + 1, n)

def place(k, i):
    return all(x[j] != i and abs(x[j] - i) != abs(j - k) for j in range(1, k))

n = int(input("Enter the number of Queens: "))
if n in [2, 3]:
    print("Not Possible")
else:
    x = [0] * (n + 1)
    nQueens(1, n)
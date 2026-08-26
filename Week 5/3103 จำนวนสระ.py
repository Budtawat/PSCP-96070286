"""จำนวนสระ"""
def main():
    """จำนวนสระ"""
    N = int(input())
    al = [0,0,0,0,0]
    for _ in range(N):
        n = input().upper()
        if n == "A":
            al[0] += 1
        elif n == "E":
            al[1] += 1
        elif n == "I":
            al[2] += 1
        elif n == "O":
            al[3] += 1
        elif n == "U":
            al[4] += 1
    totak = al[0] + al[1] + al[2] + al[3] + al[4]
    print(totak)
main()

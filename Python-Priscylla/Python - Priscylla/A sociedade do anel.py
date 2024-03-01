def main():
    n = int(input())
    rpst = [0] * 5

    for _ in range(n):
        nome, c = input().split()
        if c == 'X':
            rpst[0] += 1
        elif c == 'H':
            rpst[1] += 1
        elif c == 'E':
            rpst[2] += 1
        elif c == 'A':
            rpst[3] += 1
        else:
            rpst[4] += 1

    print(f"{rpst[0]} Hobbit(s)")
    print(f"{rpst[1]} Humano(s)")
    print(f"{rpst[2]} Elfo(s)")
    print(f"{rpst[3]} Anao(oes)")
    print(f"{rpst[4]} Mago(s)")

if __name__ == "__main__":
    main()
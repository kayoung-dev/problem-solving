def main():
    try:
        n_line = input().strip()
        if not n_line:
            return
        n = int(n_line)

        states_line = input().strip()
        if not states_line:
            print(0)
            return

        states = list(map(int, states_line.split()))

        ok = 0
        for s in states[:n]:
            if s == 1:
                ok += 1

        print(ok)

    except EOFError:
        pass

if __name__ == "__main__":
    main()

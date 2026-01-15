def main():
    try:
        s = input().rstrip("\n")
        if not s:
            return

        out = []
        for ch in s:
            found = False
            for x in out:
                if x == ch:
                    found = True
                    break
            if not found:
                out.append(ch)

        print("".join(out))

    except EOFError:
        pass

if __name__ == "__main__":
    main()

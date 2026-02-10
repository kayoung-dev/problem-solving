def main():
    try:
        n = int(input().strip())
        records = list(map(int, input().split()))

        unique = []
        for x in records[:n]:
            duplicated = False
            for y in unique:
                if y == x:
                    duplicated = True
                    break
            if not duplicated:
                unique.append(x)

        print(" ".join(map(str, unique)))

    except EOFError:
        pass

if __name__ == "__main__":
    main()

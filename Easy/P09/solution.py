def main():
    try:
        n = int(input().strip())
        moves = list(map(int, input().split()))

        position = 0
        for m in moves[:n]:
            position += m

        print(position)

    except EOFError:
        pass

if __name__ == "__main__":
    main()

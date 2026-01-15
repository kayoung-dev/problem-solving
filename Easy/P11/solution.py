def main():
    try:
        n = int(input().strip())
        prices = list(map(int, input().split()))
        m = int(input().strip())
        orders = list(map(int, input().split()))

        total = 0
        for o in orders[:m]:
            total += prices[o - 1]

        print(total)

    except EOFError:
        pass

if __name__ == "__main__":
    main()

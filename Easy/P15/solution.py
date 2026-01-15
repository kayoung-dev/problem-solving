def main():
    try:
        data = list(map(int, input().split()))
        total = 0

        # 짝수 번째 위치(1-based) -> index 1, 3, 5 ...
        for i in range(1, len(data), 2):
            if data[i] > 0:
                total += data[i]

        print(total)

    except EOFError:
        pass

if __name__ == "__main__":
    main()

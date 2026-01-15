def main():
    try:
        n_line = input().strip()
        if not n_line:
            return
        n = int(n_line)

        arr_line = input().strip()
        if not arr_line:
            return
        arr = list(map(int, arr_line.split()))

        max_val = arr[0]
        for x in arr[:n]:
            if x > max_val:
                max_val = x

        print(max_val)

    except EOFError:
        pass

if __name__ == "__main__":
    main()

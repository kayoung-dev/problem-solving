def main():
    try:
        logs = input().split()
        floor = 1

        for log in logs:
            action = log[0]
            value = int(log[1:]) if len(log) > 1 else 0

            if action == 'U':
                floor += value
            elif action == 'D':
                floor -= value

            if floor < 1:
                floor = 1
            elif floor > 50:
                floor = 50

        print(floor)

    except EOFError:
        pass

if __name__ == "__main__":
    main()

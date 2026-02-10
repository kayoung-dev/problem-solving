def grade(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"

def main():
    try:
        n_line = input().strip()
        if not n_line:
            return
        n = int(n_line)

        scores_line = input().strip()
        if not scores_line:
            return

        scores = list(map(int, scores_line.split()))

        for s in scores[:n]:
            print(grade(s))

    except EOFError:
        pass

if __name__ == "__main__":
    main()

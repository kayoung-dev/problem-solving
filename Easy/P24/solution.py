import sys
def main():
    line = sys.stdin.readline().strip()
    if not line: return
    try:
        n, idx = map(int, line.split())
        print(f"{idx // n} {idx % n}")
    except: pass
if __name__ == "__main__": main()

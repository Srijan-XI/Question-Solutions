def minion_game(string):
    n = len(string)
    kevin_score = 0
    stuart_score = 0

    for i in range(n):
        if string[i] in "AEIOU":
            kevin_score += (n - i)
        else:
            stuart_score += (n - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input().strip()
    minion_game(s)

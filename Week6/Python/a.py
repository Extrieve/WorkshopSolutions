'''
https://codeforces.com/problemset/problem/59/A
'''

def lowerOrUpper(word):
    upper = lower = 0

    for char in word:
        if char.isupper():
            upper += 1
        else:
            lower += 1

    return word.upper() if upper > lower else word.lower()


def main():
    word = input()
    print(lowerOrUpper(word))


if __name__ == '__main__':
    main()
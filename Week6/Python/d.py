'''
https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true
'''

def closestNumbers(arr):
    arr.sort()
    min_diff = abs(arr[1] - arr[0])
    pairs = [(arr[0], arr[1])]
    for i in range(1, len(arr) - 1):
        diff = abs(arr[i + 1] - arr[i])
        if diff < min_diff:
            min_diff = diff
            pairs = [(arr[i], arr[i + 1])]
        elif diff == min_diff:
            pairs.append((arr[i], arr[i + 1]))

    return pairs


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    for pair in closestNumbers(arr):
        print(*pair, end=' ')


if __name__ == '__main__':
    main()

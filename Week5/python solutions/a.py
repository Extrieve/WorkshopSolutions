'''
Source: https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
'''

from collections import Counter

# Pythonic Solution
def highest_candle(candles):
    return Counter(candles).most_common(1)[0][1]


# Non-Pythonic Solution
def highest_candle(candles):
    candle_group = dict()

    for candle in candles:
        if candle in candle_group:
            candle_group[candle] += 1
        else:
            candle_group[candle] = 1

    return max(candle_group.values())


if __name__ == '__main__':
    candles = [3, 2, 1, 3]
    print(highest_candle(candles))

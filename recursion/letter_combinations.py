# https://www.youtube.com/watch?v=PIeiiceWe_w

def letterCombinations(digits):
    
    if not digits:
        return []

    hash = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    res = []

    def recur(digitIndex, s):
        if digitIndex == len(digits):
            res.append(s)
            return

        # print(hash[di])
        for char in hash[digits[digitIndex]]:
            recur(digitIndex + 1, s + char)

    recur(0, "")
    return res



for x in letterCombinations("22333"):
    print(x) 
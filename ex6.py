from functools import reduce

count_palindromes = lambda lists: list(map(lambda sublist: reduce(lambda count, s: count + 1, filter(lambda s: s == s[::-1], sublist), 0), lists))

# דוגמה לשימוש:
lists = [["madam", "hello", "racecar"], ["abc", "def", "ghi"], ["level", "deed", "noon"]]
print(count_palindromes(lists))

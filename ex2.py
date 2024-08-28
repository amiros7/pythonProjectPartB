from functools import reduce

concat_with_space = lambda strings: reduce(lambda x, y: x + ' ' + y, strings)

# דוגמה לשימוש:
strings = ["Hello", "this", "is", "Amir", "Project"]
print(concat_with_space(strings))  # Output: "Hello world this is Python"

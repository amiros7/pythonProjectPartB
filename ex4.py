from functools import reduce

# פונקציה מסדר גבוה שמקבלת פעולה בינארית ומחזירה פונקציה שמבצעת אותה בצורה מצטברת
cumulative_operation = lambda operation: lambda seq: reduce(operation, seq)

# מימוש הפונקציה לפקטוריאל
factorial = cumulative_operation(lambda x, y: x * y)

# מימוש הפונקציה להעלאה בחזקה
exponentiation = lambda base, exp: cumulative_operation(lambda x, y: x * y)([base] * exp)

# דוגמאות לשימוש:
print(factorial(range(1, 6)))  # פקטוריאל של 5: 5! = 120
print(exponentiation(2, 3))    # 2 בחזקת 3: 2^3 = 8

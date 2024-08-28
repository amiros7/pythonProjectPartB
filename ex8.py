from math import isqrt

# פונקציה שמחזירה רשימה של מספרים ראשוניים מסודרים בסדר יורד
get_primes_sorted_desc = lambda nums: sorted(
    [n for n in nums if n > 1 and all(n % i != 0 for i in range(2, isqrt(n) + 1))],
    reverse=True
)

# דוגמת שימוש:
nums = [10, 29, 4, 17, 23, 8]
print(get_primes_sorted_desc(nums))  # פלט: [29, 23, 17]

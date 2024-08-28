cumulative_sum_of_squares = lambda lists: list(
    map(
        lambda sublist: sum(
            map(
                lambda x: x**2,
                filter(lambda x: x % 2 == 0, sublist)
            )
        ),
        lists
    )
)

# דוגמה לשימוש:
lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
print(cumulative_sum_of_squares(lists))  # Output: [20, 100, 100]

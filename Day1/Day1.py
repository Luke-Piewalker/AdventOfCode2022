def get_calorie_sums():
    with open('Day1Input.txt', 'r') as file:
        return [sum(map(int, x.split('\n'))) for x in file.read().strip().split('\n\n')]


def get_top_calories():
    return max(get_calorie_sums())


def get_top_three_calories_sum():
    return sum(sorted(get_calorie_sums())[-3:])


print(get_top_calories())
print(get_top_three_calories_sum())
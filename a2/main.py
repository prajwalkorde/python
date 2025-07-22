# main.py

import statistics_module as stats

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 6]

mean_value = stats.mean(numbers)
median_value = stats.median(numbers)
mode_value = stats.mode(numbers)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")

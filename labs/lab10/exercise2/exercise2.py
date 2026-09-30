num_days = int(input())
danger_threshold = float(input())

danger_days = 0
total = 0

for i in range(num_days):
    day_temp = float(input())
    if day_temp > danger_threshold:
        danger_days += 1
    total += day_temp

average_temp = total / num_days

print(danger_days)
print(f"{average_temp:.1f}")

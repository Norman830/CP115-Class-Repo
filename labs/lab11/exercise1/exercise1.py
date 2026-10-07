speed = int(input())

running_streak = 0
longest_streak = 0 
total_reading = 0

while speed != -1:
    total_reading += 1
    if speed < 20:
        running_streak += 1
    if running_streak > longest_streak:
        longest_streak = running_streak
    speed = int(input())

print(total_readings)
print(longest_streak)

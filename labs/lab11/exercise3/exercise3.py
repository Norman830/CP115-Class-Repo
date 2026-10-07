number = int(input())

count = 0
prev = number
biggest_jump = 0

while number != 0:
    count += 1
    jump = number - prev
    if biggest_jump < jump:
        biggest_jump = jump
    prev = number
    number = int(input())

print(count)
print(biggest_jump)

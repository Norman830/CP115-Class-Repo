yardLength = int(input())
yardWidth = int(input())
houseLength = int(input())
houseWidth = int(input())
squaremeter = yardLength * yardWidth - houseLength * houseWidth
wage = squaremeter * 2
print(wage)
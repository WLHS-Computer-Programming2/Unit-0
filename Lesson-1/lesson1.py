import random
# Variable assignment
my_name = 'Mr. Smith'
my_age = 38
fav_num = 3.14

# user input
fav_color = input("What is your favorite color? ")
num_cats = int(input("How many cats do you have? "))
print(num_cats - 1)

# formatting string
print(f"Hello, {my_name}. Your favorite color is {fav_color}.")

# for loops
for i in range(10):
    print(i+1)

for i in range(10,20):
    print(i+1, end = " ")

j = 0
while j < 10:
    print(j)
    j  = j + 1

if my_name == 'Mr. Smith':
    print("Teacher")

if my_age > 40:
    print("old")
else:
    print("not old")

if my_age > 65:
    print("senior")
elif my_age > 40:
    print("old")
else:
    print("not old")

random_num = random.randint(50,100)
print(random_num)
if my_age > 40 and random_num >70:
    print("old and lucky")
elif my_age <= 40 and random_num > 70:
    print("young and lucky")1
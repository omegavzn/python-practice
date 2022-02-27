# Finding the number of pairs within an array
#Challenge: How many pairs of colors are there within a set of baloons?

# Step 1: Define the array
baloons = [1,1,2,3,2,2,4,1]

# Step 2: Count the number of character occurances within a string
red = baloons.count(1)
blue = baloons.count(2)
yellow = baloons.count(3)
white = baloons.count(4)

# print (red)
# print (blue)
# print (yellow)
# print (white)

#Step 3: Find the number color pairs by dividing each color by 2
red_pairs = red // 2
blue_pairs = blue // 2
yellow_pairs = yellow // 2
white_pairs = white // 2

print(red_pairs)
print(blue_pairs)
print(yellow_pairs)
print(white_pairs)
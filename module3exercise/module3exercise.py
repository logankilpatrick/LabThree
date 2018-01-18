# Module 3 exercise

'''
# 1. Textbook R3.3  
# Find errors in the following statements

if x > 0 then
   print(x)
   
if 1 + x > x == sqrt(2):
   y = y + x
   
if x = 1:
   y += 1

sum = 0
xStr = input("Enter an integer value ")
x = int(xStr)
if xStr.isdigit():
   sum = sum + x
else:
   print("Bad input")
print(sum)




letterGrade = 'F'
if grade >= 90:
   letterGrade = 'A'
if grade >= 80:
   letterGrade = 'B'
if grade >= 70:
   letterGrade = 'C'
if grade >= 60:
   letterGrade = 'D'

'''
# 2. Textbook P3.18
# Write a program that reads in a string and prints whether it contains
# only letters, only lowercase letters, only digits, starts with an uppercase letter, ends with a period
'''
s = input("Enter a string: ")


if(s[len(s) - 1] == "."):
    print("Ends with period!!!!")
    
    
# 3. Textbook R4.2, b and d, R4.16
# Write a loop that computes the sum of squares of numbers between 1 and 100
total = 0
for num in range(1,101):
    total += num * num

print(total)
# Rewrite the loop to calculate the squares as a while loop
total = 0
num = 1
while (num < 101):
    total += num * num
    num += 1# ends while loop 

print(total)
'''
    
# Write a loop that computes the sum of all odd digits of n.
# Example: if n is 32677, then the sum is 3 + 7 + 7 = 17
'''
n = 32677
total = 0
nStr = str(n)#converts n number to  string 
#You cant see the indecies of a number! n[0] = 32677! Thats why we convert it 

for digit in nStr:
    if int(digit) % 2 : #1 if odd, 1 is true 
        total += int(digit)#ads the number if its an odd digit 

print(total)
        
'''


# 4. Textbook R4.30, R.
# Given the flipImage.py program of Section 4.10
# change the code to flip the image horizontally instead of vertically

#  This program creates a new flipped version of a GIF image.
#
from ezgraphics import GraphicsImage, GraphicsWindow

filename = "queen-mary.gif"

# Load the original image.
origImage = GraphicsImage(filename)

# Create an empty image that will contain the new flipped image.
width = origImage.width()
height = origImage.height()
newImage = GraphicsImage(width, height)

# Iterate over the image and copy the pixels to the new image to 
# produce the flipped image (vertical flip to an upside down image)
'''
newRow = height - 1
for row in range(height) :
    for col in range(width) :
        newCol = col
        pixel = origImage.getPixel(row, col)
        newImage.setPixel(newRow, newCol, pixel)
    newRow = newRow - 1
'''
# Save the new image with a new name.
newImage.save("flipped-" + filename)


#newRow = height - 1
'''
for row in range(height) :# flips over y-axis 
    newRow = row
    newCol = width - 1
    for col in range(width) :
        pixel = origImage.getPixel(row, col)
        newImage.setPixel(newRow, newCol, pixel)
        newCol = newCol - 1
'''
# 5. Textbook R.29
# show only the green component of each pixel of the image to green
for row in range(height) :# flips over y-axis 
    for col in range(width) :
        green = origImage.getGreen(row, col)
        origImage.setPixel(row, col, 0, green, 0)


# Draw the image
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(origImage)
win.wait()


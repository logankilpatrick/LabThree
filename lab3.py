#Lab 3
#Logan kilpatrick 
#10/03/17

from ezgraphics import GraphicsImage, GraphicsWindow
from math import sqrt
filename = "queen-mary.gif"
#filename = "jellyfish.gif"
#preexisting python functions run fatser than our code! 

origImage = GraphicsImage(filename)
width = origImage.width()
height = origImage.height()

newImage = GraphicsImage(width, height)

if(width > height):
    radius = (height /2)
    
else:
    radius = (width / 2)
    
centerx = int(height / 2)    
centery = int(width / 2)
     
debugg = False
if(debugg == True):
    print("Width", width)
    print("Height", height)
    print("CenterX", centerx)
    print("CenterY", centery)
    print("Radius", radius)    
     
  

for x in range(height):#This is right 
    for y in range(width):#this is right 
        redPix = origImage.getRed(x,y)
        greenPix = origImage.getGreen(x,y)
        bluePix = origImage.getBlue(x,y)
        
        redPix = int(0.2126 * redPix)
        greenPix = int(0.7152 * greenPix)
        bluePix = int(0.0722 * bluePix)#per page 108 in the slides from class
        
        
        grey = int((0.2126 * redPix) + (0.7152 * greenPix) + (0.0722 * bluePix))
        distance = (sqrt((centerx - x)**2 + (centery - y)**2))#Might be root of issue
                         ##### is that a + and then a -  right after the variable centery?
        
        if(distance > radius):
            newImage.setPixel(x,y, "white")
        else:
            newImage.setPixel(x,y, grey, grey, grey)
        # use shell to play around with how to get rgb value of image at a certain pixel!
        # Need to find a way to get current rgb color value                              



     
# Save the new image with a new name.
newImage.save("grey-" + filename)



# Draw the image
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(newImage)
win.wait()
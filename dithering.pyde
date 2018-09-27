
def setup():
    global img
    size(512,640)
    img = loadImage("unicorn.jpg")
    
def draw():
    img.loadPixels()
    
    for x in range(img.width-1):
        for y in range(img.height-1):
            pix = img.pixels[x + y * img.width]
            oldR = red(pix)
            oldG = green(pix)
            oldB = blue(pix)
            factor = 1
            newR = round(factor * oldR / 255) * (255/factor)
            newG = round(factor * oldG / 255) * (255/factor)
            newB = round(factor * oldB / 255) * (255/factor)
            img.pixels[x + y * img.width] = color(newR,newG,newB)
            
            errR = oldR - newR
            errG = oldG - newG
            errB = oldB - newB
            
            index = (x + 1) + y * img.width
            c = img.pixels[index]
            r = red(c)
            g = green(c)
            b = blue(c)
            r = r + errR * 7/16.0
            g = g + errG * 7/16.0
            b = b + errB * 7/16.0
            img.pixels[index] = color(r,g,b)
            
            index = (x-1) + (y+1) * img.width
            c = img.pixels[index]
            r = red(c)
            g = green(c)
            b = blue(c)
            r = r + errR * 3/16.0
            g = g + errG * 3/16.0
            b = b + errB * 3/16.0
            img.pixels[index] = color(r,g,b)

            index = x + (y+1) * img.width
            c = img.pixels[index]
            r = red(c)
            g = green(c)
            b = blue(c)
            r = r + errR * 5/16.0
            g = g + errG * 5/16.0
            b = b + errB * 5/16.0
            img.pixels[index] = color(r,g,b)
            
            index = (x+1) + (y+1) * img.width
            c = img.pixels[index]
            r = red(c)
            g = green(c)
            b = blue(c)
            r = r + errR * 1/16.0
            g = g + errG * 1/16.0
            b = b + errB * 1/16.0
            img.pixels[index] = color(r,g,b)
            
    img.updatePixels()
    image(img, 0, 0)
    

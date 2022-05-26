size(600, 600)
noFill()
noStroke()

fill('#FF0000') # red quadrant
rect(width/2, 0, width/2, height/2)

fill('#004477') # blue quadrant
rect(0, 0, width/2, height/2)

fill('#6633FF') # violet quadrant
rect(0, height/2, width/2, height/2)

fill('#FF9900') # orange quadrant
rect(width/2, height/2, width/2, height/2)

x = 30
y = 400
txt = '?'
if x >= width/2 and y >= height/2:
    txt = 'O'
elif x >= width/2:
    txt = 'R'
elif x <= width/2 and y <= height/2:
    txt = 'B'
else:
    txt = 'P'

fill('#FFFFFF')
textSize(40)
textAlign(CENTER, CENTER)
text(txt, x, y)

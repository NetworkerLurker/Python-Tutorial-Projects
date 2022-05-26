def setup():
    size(800, 600)
    
radius = 200
theta = 1
period = 2.1

def circlePoint(t, r):
    x = cos(t) * r
    y = sin(t) * r
    return [x, y]

def ellipsePoint(t, hr, vr):
    x = cos(t) * hr
    y = sin(t) * vr
    return [x, y]

def draw():
    global theta
    theta += TAU / (frameRate * period)
    background('#004477')
    noFill()
    strokeWeight(3)
    stroke('#0099FF')
    line(width/2, height, width/2, 0)
    line(0, height/2, width, height/2)
    # flip the y-axis
    scale(1, -1)
    translate(0, -height)
    translate(width/2, height/2)
    
    circle(0, 0, radius*2)
    stroke('#FFFFFF')
    
    
    # white dot
    noStroke()
    fill('#FFFFFF')
    #x = cos(theta) * radius
    #y = sin(theta) * radius
    amplitude = radius
    y = sin(theta) * amplitude
    circle(0, y, 15)
    x, y = ellipsePoint(theta, radius*1.5, radius)
    circle(x, y, 15)
    
    amplitude = radius
    y = sin(theta) * amplitude
    noFill()
    stroke('#FFFFFF')
    strokeJoin(ROUND)
    bends = 35
    
    beginShape()
    for i in range(bends):
        vx = 30 + 60 * (i % 2 - 1)
        vy = 300 - (300 - y) / (bends - 1) * i
        vertex(vx, vy)
    endShape()
    
    rect(-100, y-80, 200, 80)

    
    for i in range (51):
        f = .125 * 2
        t = theta + i * f
        x = -400 + i * 16
        y = sin(t) * amplitude
        circle(x, y, 15)

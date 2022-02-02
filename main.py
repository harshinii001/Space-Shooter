import pygame
from math import *

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False

# Parameters
angle = 30
xPos = 100
yPos = 250
# Length of object
length = 100

start = False
# Goal Position of End point
xGoalPos = 0
yGoalPos = 0
# Linear Velocity
linVel = 0
# Angular Velocity
angVel = 0
e1 = 0
e2 = 0
p1 = 0
p2 = 0
i1 = 0
i2 = 0
p = 0
q = 0
count = 0

def controller(X,Y,x,a):
    linVel = 0
    angVel = 0

    X0 = x + 100*cos(radians(a))
    linVel = (X - X0)*0.1
    if(X> 250):
        A = asin((Y-250)/100)
    else:
        A = radians(180)-asin((Y - 250) / 100)

    angVel = (A - radians(a))*0.1
    # Value Clamps
    linVel = max(-0.1, linVel)
    linVel = min(0.1, linVel)
    angVel = max(-0.1, angVel)
    angVel = min(0.1, angVel)
    return linVel, angVel


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if (pos[1] > 150) and (pos[1] < 350):
                xGoalPos, yGoalPos = pygame.mouse.get_pos()
                start = True
                count = 0
                print("x goal position", xGoalPos)
                print("y goal position", yGoalPos)


    pressed = pygame.key.get_pressed()

    if (start):
        linVel, angVel = controller(xGoalPos, yGoalPos, xPos, angle)

    # Updation
    count = count + 1
    e1 = linVel/0.1
    e2 = angVel/0.1
    i1 = i1 + e1
    i2 = i2 + e2
    p1 = e1 - p
    p = e1
    p2 = e2 - q
    q = e2
    xPos += linVel + 0 * i1 + 0 * p1
    angle += angVel + 0 * i2 + 0 *p2
    xPos = min(400, xPos)
    xPos = max(100, xPos)
    xEndLine = xPos + length * cos(radians(angle))
    yEndLine = yPos + length * sin(radians(angle))
    print("x position",xEndLine)
    print("y position",yEndLine)
    print(count)


    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 0, 0), (100, 250), (400, 250), 3)
    pygame.draw.line(screen, (0, 0, 255), (xPos, yPos), (xEndLine, yEndLine), 5)
    pygame.draw.circle(screen, (0, 255, 0), (xPos, yPos), 7)
    pygame.draw.circle(screen, (0, 255, 0), (xEndLine, yEndLine), 5)
    pygame.draw.circle(screen, (255, 255, 0), (xGoalPos, yGoalPos), 5)
    pygame.display.flip()

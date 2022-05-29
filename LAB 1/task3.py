from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    glVertex2f(x, y)
    glEnd()

def DDA(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    xInc = dx / steps
    yInc = dy / steps

    x = x0
    y = y0

    #print(xInc, yInc)

    draw_points(round(x), round(y))
    #print(round(x), round(y))

    x += xInc
    y += yInc
    for _ in range(1, steps):
        draw_points(round(x), round(y))
        #print(round(x), round(y))
        x += xInc
        y += yInc

    draw_points(round(x), round(y))
    #print(round(x), round(y))

def DASHED_DDA(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    xInc = dx / steps
    yInc = dy / steps

    x = x0
    y = y0

    #print(xInc, yInc)

    draw_points(round(x), round(y))
    #print(round(x), round(y))

    x += xInc
    y += yInc
    for _ in range(1, steps):
        if x % 5 == 0:
            draw_points(round(x), round(y))
            #print(round(x), round(y))
        x += xInc
        y += yInc

    draw_points(round(x), round(y))
    #print(round(x), round(y))
    
def task_three(sid):
    if sid % 2 == 0:
        DASHED_DDA(80, 220, 220, 220)
        DDA(150, 220, 150, 80)
    else:
        DDA(75, 225, 75, 75)
        DDA(225, 225, 225, 75)
        DASHED_DDA(75, 150, 225, 150)

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)
    # call the draw methods here
    task_three(20201220)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(300, 300)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 3")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

def draw_points(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    glVertex2f(x, y)
    glEnd()
            
def task_one():
    for _ in range(50):
        draw_points(random.randint(0, 500), random.randint(0, 500))

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #call the draw methods here
    task_one()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 1") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
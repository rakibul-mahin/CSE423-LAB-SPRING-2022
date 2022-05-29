from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glPointSize(3) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    glVertex2f(x, y) #jekhane show korbe pixel
    glEnd()

def plot_triangle(x0, y0, x1, y1, x2, y2):
    glBegin(GL_TRIANGLES)
    glVertex3f(x0, y0, 0)
    glVertex3f(x1, y1, 0)
    glVertex3f(x2, y2, 0)
    glEnd()

def plot_quad(x0, y0, x1, y1, x2, y2, x3, y3, c): #A B D C
    glBegin(GL_QUADS)
    if c == "l":
        glColor3f(1, 0, 0)
    elif c == "m":
        glColor3f(0, 1, 0)
    elif c == "r":
        glColor3f(0, 0, 1)

    glVertex2i(x0, y0)
    glVertex2i(x1, y1)
    glVertex2i(x2, y2)
    glVertex2i(x3, y3)
    glEnd()

def task_two():
    plot_triangle(250, 399, 150, 299, 350, 299)
    plot_quad(150, 299, 350, 299, 350, 99, 150, 99, 'l')
    plot_quad(180, 230, 220, 230, 220, 270, 180, 270, 'r')
    plot_quad(280, 230, 320, 230, 320, 270, 280, 270, 'r')
    plot_quad(230, 200, 270, 200, 270, 99, 230, 99, 'r')
    draw_points(265, 160)

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
    glColor3f(1.0, 1.0, 0.0)
    #call the draw methods here
    task_two()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Task 2")
glutDisplayFunc(showScreen)

glutMainLoop()
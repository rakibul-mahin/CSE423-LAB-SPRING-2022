from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def draw_points(x,y):
    glPointSize(1)
    glBegin(GL_POINTS)
    glColor3f(0, 1, 0)
    glVertex2f(x, y)
    glEnd()

def eightWayCircle(x,y,radius):
    #The Biggest Circle
    midPointCircleAlgorithm(x,y,radius)
    #This is the Right Circle
    midPointCircleAlgorithm(x+(radius/2),y,radius/2)
    #This is the Above Circle 
    midPointCircleAlgorithm(x,y+(radius/2),radius/2)
    #This is the Below Circle 
    midPointCircleAlgorithm(x,y-(radius/2),radius/2)
    #This is the Left Circle 
    midPointCircleAlgorithm(x-(radius/2),y,radius/2) 
    x0=x+(radius/2)-33
    y0=y+(math.sin(45)*(radius/2))-33
    #NORTH EAST Circle
    midPointCircleAlgorithm(x0,y0,radius/2) 
    x0=x+(radius/2)-33
    y0=y-(math.sin(45)*(radius/2))+33
    #SOUTH EAST Circle
    midPointCircleAlgorithm(x0,y0,radius/2)
    x0=x-(radius/2)+33
    y0=y-(math.sin(45)*(radius/2))+33
    #SOUTH WEST Circle
    midPointCircleAlgorithm(x0,y0,radius/2)
    x0=x-(radius/2)+33
    y0=y+(math.sin(45)*(radius/2))-33
    #NORTH WEST Circle
    midPointCircleAlgorithm(x0,y0,radius/2)

#This function will plot to converted zones
#Including zone 1
def Circlepoints(x, y,x0, y0):
    draw_points(x+x0, y+y0)
    draw_points(y+x0, x+y0)
    draw_points(y+x0, -x+y0)
    draw_points(x+x0, -y+y0)
    draw_points(-x+x0, -y+y0)
    draw_points(-y+x0,-x+y0)
    draw_points(-y+x0, x+y0)
    draw_points(-x+x0, y+y0)

#This function is the MidPoint Circle Algorithm
def midPointCircleAlgorithm(x0, y0, radius):
    #Initial d
    d=1-radius 
    x=0
    y=radius
    Circlepoints(x,y, x0,y0)
    
    while (x < y):
        
        if d<0:
            #IF EAST
            d=d+2*x+3
            x=x+1
        else:
            #IF SOUTH
            d=d+2*x-2*y+5
            x=x+1
            y=y-1
        Circlepoints(x,y, x0,y0)
        
def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    eightWayCircle(400,400,300)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(768, 768) 
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"8 Way Circle")
glutDisplayFunc(screen)
glutMainLoop()
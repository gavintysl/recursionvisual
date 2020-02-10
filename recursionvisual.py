# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:41:52 2018

@author: tysl
"""

import turtle

def drawTriangle(aTurtle,side):
    for i in range(3):
        aTurtle.forward(side)
        aTurtle.right(120)

def nestedTriangle(aTurtle,side):
    if side >= 1:                    
        drawTriangle(aTurtle,side)    
        nestedTriangle(aTurtle,side-5)  

def nestedTriangle2(aTurtle, side):
    for i in range(side, 1, -5):
        drawTriangle(aTurtle, i)
        
def tree(t, trunkLength, r_reduction, l_reduction, r_angle, l_angle):
    if trunkLength < 5:         
        return
    else:
        t.forward(trunkLength)
        t.right(r_angle)
        tree(t, trunkLength - r_reduction, r_reduction, l_reduction, r_angle, l_angle)  
        t.left(r_angle + l_angle)
        tree(t, trunkLength - l_reduction, r_reduction, l_reduction, r_angle, l_angle)  
        t.right(l_angle)
        t.backward(trunkLength) 
        
        
fred = turtle.Turtle()
win = turtle.Screen()
#turtle.tracer(0)
fred.up()
fred.left(90)
fred.backward(250)
fred.down()

#nestedTriangle(fred, 40)
#tree(fred, 100, 10, 15, 55, 65)
tree(fred, 100, 5, 30, 60, 20)
win.exitonclick()
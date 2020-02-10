import turtle

def drawSquare(aTurtle,side):
    for i in range(4):
        aTurtle.forward(side)
        aTurtle.right(90)

def nestedBox(aTurtle,side):
    if side >= 1:                    
        drawSquare(aTurtle,side)    
        nestedBox(aTurtle,side-5)  

def nestedBox2(aTurtle, side):
    for i in range(side, 1, -5):
        drawSquare(aTurtle, i)
        
def tree(t,trunkLength):
    if trunkLength < 5:         
        return
    else:
        t.forward(trunkLength)
        t.right(30)
        tree(t, trunkLength-15)  
        t.left(60)
        tree(t, trunkLength-15)  
        t.right(30)
        t.backward(trunkLength) 
        
        
fred = turtle.Turtle()
win = turtle.Screen()

fred.up()
fred.left(90)
fred.backward(250)
fred.down()

nestedBox(fred, 40)
#tree(fred,100)
win.exitonclick()

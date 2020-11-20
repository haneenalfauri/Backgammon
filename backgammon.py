from cs1graphics import *
from itertools import cycle

correct=False

while not correct :
    s=input('Enter pixels per grid cell: ')
    if s.isnumeric() and int(s)>0:
        correct=True
        size=int(s)
    else:
        print('Invalid Entery!')



width=size*15
hight=size*13

Haneen = Canvas(width,hight, 'navajowhite', 'backgammon')
# Drawing the frame
sq1=Layer()
for i in range(15):
# Top horizantal frame
    sq=Square(size,Point((size/2),(size/2)))
    sq.setFillColor('burlywood4')
    sq.setBorderColor('transparent')
    sq.move(i*size,0)
    sq1.add(sq)
Haneen.add(sq1)
# Bottom horizantal frame
sq2=sq1.clone()
sq2.move(0,size*12)
Haneen.add(sq2)
# left/vertical frame
sq2=Layer()
for i in range(13):
    sq=Square(size,Point((size/2),(size/2)))
    sq.setFillColor('burlywood4')
    sq.setBorderColor('transparent')
    sq.move(0,i*size)
    sq2.add(sq)
Haneen.add(sq2)
# Middle/vertical frame
sq3=sq2.clone()
sq3.move(7*size,0)
Haneen.add(sq3)
# right/vertical frame
sq4=sq2.clone()
sq4.move(14*size,0)
Haneen.add(sq4)

# For loop to draw all numbers (4 groups of numbers , each group has 6 numbers)
for i in range(0,4):
    for j in range(0,6):
        title=Text(str(j+(i*6)+1),size/3)
        title.setFontColor('black')
        if i==0:
            x=(1.5*size)+(j*size)
            y=(hight-(size/2))
        if i==1:
            x=(8.5*size)+(j*size)
            y=(hight-(size/2))
        if i==2:
            x=(13.5*size)-(size*j*i)+(j*size)
            y=(size/2)
        if i==3:
            x=(6.5*size)-(size*j)
            y=(size/2)
        
        title.move(x,y)
        Haneen.add(title)

       
# For loop to Draw all Triangles
col1=cycle(['darkorange','tan'])
tri1=Layer()
for n in range(1,7):
# bottom left
    p1=Polygon(Point((size)+(size*(n-1)),(hight-size)),Point((1.5*size)+size*(n-1),(hight/2)+(size/2)),Point((2*size)+(size*(n-1)),(hight-size)))
    p1.setFillColor(next(col1))
    tri1.add(p1)
Haneen.add(tri1)
# bottom right
p2=tri1.clone()
p2.move(7*size,0)
Haneen.add(p2)
# top right
p3=p2.clone()
p3.move(size,size*13)
p3.rotate(180)
Haneen.add(p3)
# top left
p4=p3.clone()
p4.move(size*7,0)
Haneen.add(p4)
              

    
# For loops to draw Checkers
col2=['black','white']
for n in range(2):
    # bottom left 2 black chekers
    if n==0:
        for m in range(2):
            c=Circle(0.9*(size/2),Point((1.5*size),hight-(1.45*size)-(m*0.9*size)))
            c.setFillColor(col2[n])
            Haneen.add(c)
    # Top left 2 white checker
    if n==1:
        for m in range(2):
            c=Circle(0.9*(size/2),Point((1.5*size),(1.45*size)+(m*0.9*size)))
            c.setFillColor(col2[n])
            Haneen.add(c)
# Draw 3 checkers for upper half and lower half
for x in range(2):
        for m in range(3):
            c=Circle(0.9*(size/2),Point((9.5*size),(1.45*size)+(m*0.9*size)+(x*8.3*size)))
            c.setFillColor(col2[x])
            Haneen.add(c)



#Draw the checkers
c1=Layer()
col2=['white','black']
#Bottom 5 white checkers
for n in range(5):
    for m in range(5):
        c=Circle(0.9*(size/2),Point((6.5*size),hight-(1.45*size)-(m*0.9*size)))
        c.setFillColor(col2[0])
        c1.add(c)
Haneen.add(c1)
#Top rigth 5 white checkers
c2=c1.clone()
c2.move(size*7,-size*6.5)
Haneen.add(c2)
#Top left 5 black checkers
c3=Layer()
for n in range(5):
    for m in range(5):
        c=Circle(0.9*(size/2),Point((6.5*size),(1.45*size)+(m*0.9*size)))
        c.setFillColor(col2[1])
        c3.add(c)
Haneen.add(c3)
#bottom rigth 5 black checkers
c2=c3.clone()
c2.move(size*7,size*6.5)
Haneen.add(c2)


# Draw the line that splits the backgammon  
p=Path(Point((width/2),0),Point((width/2),hight))
Haneen.add(p)

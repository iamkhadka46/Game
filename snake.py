from turtle import*
from random import randrange
from base import vector,square



food = vector(0,0)
snake = [vector(10,0)]
aim = vector(0,-10)


def change(x,y):
    aim.x = x
    aim.y = y
    
def inside(head):
    return -200< head.x < 190 and -200 < head.y < 190




def move():
    head = snake[-1].copy()
    head.move(aim)

    snake.append(head)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9,'Red')
        update()
        return

    if food == snake:
        print("Score",len(snake))
        food.x = randrange(-15,15)*10
        food.y = randrange(-15,15)*10


    else:
        snake.pop(0)

    clear()
    for body in snake:
        square(body.x, body.y, 9, 'blue')

    square(food.x,food.y,9,"black")
    update()
    ontimer(move,100)
        
   

    
    



setup(340, 340, 270,0)
hideturtle()
tracer(False)
listen()
onkey(lambda:change(10,0),'Right')
onkey(lambda:change(-10,0),'Left')
onkey(lambda:change(0,10),'Up')
onkey(lambda:change(0,-10),'Down')
move()
done()

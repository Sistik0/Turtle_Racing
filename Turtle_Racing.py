import turtle
import time
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
COLORS = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def get_number_of_racers():
    number_of_racers = 0
    while True:
        number_of_racers = input("Enter the number of racers (2-10): ")
        if number_of_racers.isdigit():
            number_of_racers = int(number_of_racers)
            if 2<= number_of_racers <= 10:
                break
        else:
            print("Please enter a number between 2 and 10")

    return number_of_racers

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= SCREEN_HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = SCREEN_WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-SCREEN_WIDTH//2 + (i+1) * spacingx, -SCREEN_HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Turtle Racing")
    

#print(get_number_of_racers())
racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)




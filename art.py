import turtle
from pynput import keyboard

t = turtle.Turtle()

turtle.pencolor("red")

def move_forward():
    t.forward(5)

def move_backward():
    t.backward(5)

def turn_left():
    t.left(5)

def turn_right():
    t.right(5)

def on_press(key):
    try:
        if key.char == 'w':
            move_forward()
        elif key.char == 's':
            move_backward()
        elif key.char == 'a':
            turn_left()
        elif key.char == 'd':
            turn_right()
    except AttributeError:
        pass  


listener = keyboard.Listener(on_press=on_press)
listener.start()

turtle.mainloop()

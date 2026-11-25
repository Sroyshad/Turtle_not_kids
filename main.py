import turtle



#Это вам не нужно, это мой фикс на типизации данных
def configure():
    print("Базовый терминал рисования\n"
          "Выбор параметров для редактирования:\n"
          " 1. Толщина линии\n"
          " 2. Цвет обводки\n"
          " 3. Скорость\n"
          " 4. Цвет фона\n"
          " 5. Цвет заливки сердца\n")

    choices = input("Введите 5 символа (1/0): ").ljust(5, "0")

    fat   = int(input("Толщина: ")) if choices[0] == "1" else 2
    color = (list(map(int, input("Цвет ко   нтура RGB через пробел: ").split()))
             if choices[1] == "1" else [239, 191, 4])
    speed = int(input("Скорость: ")) if choices[2] == "1" else 1
    collorScreen = (list(map(int, input("Цвет фона RGB через пробел: ").split()))
             if choices[3] == "1" else [166, 22, 22])
    collorBack = (list(map(int, input("Цвет заливки RGB через пробел: ").split()))
                    if choices[4] == "1" else [239, 191, 4])

    return fat, color, speed, collorScreen, collorBack

def draw_circle(pen):
    for _ in range(200):
        pen.right(1)
        pen.forward(1)

def main():
    fat, color, speed, collorScrean, collorBack = configure()
    screen = turtle.Screen()
    turtle.colormode(255)
    screen.bgcolor(*collorScrean)


    pen = turtle.Turtle()
    pen.pensize(fat)
    pen.pencolor(*color)
    pen.fillcolor(*collorBack)
    pen.speed(speed)

    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    draw_circle(pen)
    pen.left(120)
    draw_circle(pen)
    pen.forward(112)
    pen.end_fill()
    pen.hideturtle()
    screen.mainloop()

    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()

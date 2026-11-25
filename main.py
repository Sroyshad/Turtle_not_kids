import turtle
import math
# Создаём экран и задаём цвет фона
screen = turtle.Screen()
turtle.colormode(255)
screen.bgcolor(149,24,18)


#Это вам не нужно, это мой фикс на типизации данных
def configure():
    """Запрашивает настройки у пользователя."""
    print("Базовый терминал рисования\n"
          "Выбор параметров для редактирования:\n"
          " 1. Толщина линии\n"
          " 2. Цвет\n"
          " 3. Скорость")

    # Гарантируем длину 3 — нет IndexError
    choices = input("Введите 3 символа (1/0): ").ljust(3, "0")

    fat   = int(input("Толщина: ")) if choices[0] == "1" else 2
    color = (list(map(int, input("Цвет RGB через пробел: ").split()))
             if choices[1] == "1" else [239, 191, 4])
    speed = int(input("Скорость: ")) if choices[2] == "1" else 2

    return fat, color, speed

def draw_circle(pen):
    """Рисует круг одним вызовом."""
    for _ in range(200):
        pen.right(1)
        pen.forward(1)
# Создаём «черепашку»
def main():
    screen = turtle.Screen()
    turtle.colormode(255)
    screen.bgcolor(149, 24, 18)

    fat, color, speed = configure()

    pen = turtle.Turtle()
    pen.pensize(fat)
    pen.pencolor(*color)      # распаковка: pencolor(r, g, b)
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

    screen.update()           # отрисовать всё разом
    screen.exitonclick()


if __name__ == "__main__":
    main()

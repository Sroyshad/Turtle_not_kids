import turtle
from typing import Annotated

from pydantic import BaseModel, Field, field_validator

point = 5  # Количество пунктов

# class Validation(BaseModel):
#     fat: Annotated[int, Field(ge=0, le=100)]
#     speed: Annotated[int, Field(ge=0, le=9)]
#     colorScreen: tuple[int, int, int]
#     colorBack: tuple[int,int,int]
#
#     @field_validator('colorScreen', 'colorBack')
#     @classmethod
#     def RGB(cls, v):
#         if not all(0 <= i <= 255 for i in v):
#             raise ValueError("Формат RGB до 255")
#         return v


def choicesDef():
    print("Базовый терминал рисования\n"
          "Выбор параметров для редактирования:\n"
          " 1. Толщина линии\n"
          " 2. Цвет обводки\n"
          " 3. Скорость\n"
          " 4. Цвет фона\n"
          " 5. Цвет заливки сердца\n")
    while True:
        x = 0
        choice = input(f"Введите {point} символа (1/0): ").strip()
        choice = choice[:point].ljust(point, "0")

        for i in choice:
            if str(i) not in ("0", "1"):
                print("В ответе должны содержаться только цифры: \"0\" и \"1\"\n")

                break
            else:
                x+=1

        if x == point:
            break
    return choice

def configure():
    if Isexamination():
        fat = int(input("Толщина: "))
    color = (list(map(int, input("Цвет контура RGB через пробел: ").split()))
             if choices[1] == "1" else [239, 191, 4])
    speed = int(input("Скорость: ")) if choices[2] == "1" else 1
    colorScreen = (list(map(int, input("Цвет фона RGB через пробел: ").split()))
             if choices[3] == "1" else [166, 22, 22])
    colorBack = (list(map(int, input("Цвет заливки RGB через пробел: ").split()))
                    if choices[4] == "1" else [239, 191, 4])

    return Validation(fat=fat, color=color, speed=speed, colorScreen=colorScreen, colorBack=colorBack)

def draw_circle(pen):
    for _ in range(200):
        pen.right(1)
        pen.forward(1)

def main():
    fat, color, speed, colorScreen, colorBack = configure()
    screen = turtle.Screen()
    turtle.colormode(255)
    screen.bgcolor(*colorScreen)


    pen = turtle.Turtle()
    pen.pensize(fat)
    pen.pencolor(*color)
    pen.fillcolor(*colorBack)
    pen.speed(speed)

    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    draw_circle(pen)
    pen.left(120)
    draw_circle(pen)
    pen.forward(113)
    pen.end_fill()
    pen.hideturtle()

    screen.update()
    screen.exitonclick()
    screen.mainloop()


if __name__ == "__main__":
    main()

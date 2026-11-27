import turtle

POINT = 5  # Количество пунктов

def choicedef() -> str:
    print("Базовый терминал рисования\n"
          "Выбор параметров для редактирования:\n"
          " 1. Толщина линии\n"
          " 2. Цвет обводки\n"
          " 3. Скорость\n"
          " 4. Цвет фона\n"
          " 5. Цвет заливки сердца\n")
    while True:
        choice = input(f"Введите {POINT} символов, формата чисел:(1/0): ").strip()
        choice = choice[:POINT].ljust(POINT, "0")
        if all(i in ("0", "1") for i in choice):
            break
    return choice
def speed_turtle() -> int:
    while True:
        speed = input("Скорость (1 — медленно, 10 — быстро): ")
        if speed.isdigit():
            if -1 < int(speed) < 11:
                return int(speed)
            else:
                print("Нужно целое от 1 до 10")
        else:
            print("Нужно целое от 1 до 10")

def examination_rgb() -> list[int, int, int]:
    while True:
        color_screen = (list(map(int, input("Цвет фона RGB через пробел(пример:255 255 255): ").split())))
        if color_screen != " ":
        if all(0 <= i <= 255 for i in color_screen):
            if len(color_screen) == 3:
                return




def configure() -> tuple:
    choices = choicedef()
    fat = int(input("Толщина: ")) if choices[0] == "1" else 2
    color = examination_rgb() if choices[1] == "1" else [200, 191, 4]
    speed = speed_turtle() if choices[2] == "1" else 1
    color_screen = examination_rgb() if choices[3] == "1" else [166, 22, 22]
    color_back = examination_rgb() if choices[4] == "1" else [239, 191, 4]

    return fat, color, speed, color_back, color_screen



def main() -> None:
    fat, color, speed, color_back, color_screen = configure()
    screen = turtle.Screen()
    turtle.colormode(255)
    screen.bgcolor(*color_screen)


    pen = turtle.Turtle()
    pen.pensize(fat)
    pen.pencolor(*color)
    pen.fillcolor(*color_back)
    pen.speed(speed)

    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    pen.circle(-57.3, 200)
    pen.left(120)
    pen.circle(-57.3, 200)
    pen.forward(113)
    pen.end_fill()
    pen.hideturtle()

    screen.exitonclick()

if __name__ == "__main__":
    main()

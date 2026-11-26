point = 5
def choicesDef():
    while True:
        x = 0
        print("Базовый терминал рисования\n"
              "Выбор параметров для редактирования:\n"
              " 1. Толщина линии\n"
              " 2. Цвет обводки\n"
              " 3. Скорость\n"
              " 4. Цвет фона\n"
              " 5. Цвет заливки сердца\n")

        choice = input(f"Введите {point} символа (1/0): ").strip()
        choice = choice[:point].ljust(point, "0")

        if all(i in ("0", "1") for i in choice):
            break
    return True

print(choicesDef())
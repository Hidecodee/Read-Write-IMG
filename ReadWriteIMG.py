def Read(FileName):
    try:
        with open(FileName, "rb") as File:
            Count = 0
            Byte = File.read(1)
            while Byte:
                    try:
                        Byte = File.read(1).decode("utf-8")
                    except BaseException:
                        continue
                    print(Byte, end="")
                    Count += 1
    except FileNotFoundError:
        print("Файл не найден")
        raise SystemExit
    else:
        print("\n[!]Количество байт в файле "+str(FileName)+": "+str(Count))


def Write(FileName, Text):
    try:
        with open(FileName, "ab") as File:
            File.write(Text.encode("utf-8"))
    except FileNotFoundError:
        print("Файл не найден")
        raise SystemExit
    except BaseException:
        print("Какая-то ошибка")
        raise SystemExit
    else:
        print("\nФайл успешно записан!")


Help = (
    "|Стеганография!\n|Основые функции: \n|Read - вывести содержание картинки в "
    "байтах(FileName)\n|Write - Записать текст в конец картинки(FileName, Text)"
    "\n|Пример: Read$test.jpg\n|Пример: Write$test.exe/Text kotoriy ho4y spratat"
    )
print(Help)
while True:
    Step = input(str("[?]Введите функцию и аргументы: "))
    Step = Step.split("$")
    if Step[0] == "Read":
        Read(Step[1])
    elif Step[0] == "Write":
        Write(Step[1], Step[2])
    elif Step[0] == "Help":
        print(Help)
    else:
        print("[!]Неправильно введена команда")

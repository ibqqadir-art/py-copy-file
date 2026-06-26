import os


def copy_file(command: str) -> None:
    # Проверяем, что строка не пустая
    if not command:
        return

    parts = command.split(" ")

    # Проверяем, что команда начинается с "cp" и есть 3 части
    if parts[0] != "cp" or len(parts) != 3:
        return

    source = parts[1]
    destination = parts[2]

    # Проверяем, что имена файлов разные
    if source == destination:
        return

    # Проверяем, что исходный файл существует
    if not os.path.exists(source):
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        content = file_in.read()
        file_out.write(content)

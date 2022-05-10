import os

path = "my_project"

# Создает папку
os.mkdir("templates")
path_dirs = "templates"

for i in os.listdir(path):
    # Выборка папки из listdir
    if os.path.isdir(path + "//" + i):
        # Когда открыли папки приложений Django
        if os.path.isdir(path + "//" + i + "//" + "templates"):
            # Задаем путь где брать файлы
            dir = path + "//" + i + "//" + "templates" + "//"
            # Перенос папки с HTML файлами в главную templates
            for g in os.listdir(dir):
                os.replace(dir + g, path_dirs + "//" + g)

import os

dirs = ['settings', 'mainapp', 'adminapp', 'authapp']

os.mkdir('my_project')
path = "my_project"

for i in dirs:
    os.mkdir(f"{path}//{i}")

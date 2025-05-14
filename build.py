import subprocess
import os


if os.path.exists("lista-da-vanessador.spec"):
    subprocess.run(["pyinstaller", "lista-da-vanessador.spec"])

subprocess.run(["pyinstaller", "--noconfirm", "--onefile", "--windowed","-n","lista-da-vanessador",  "run.py"])

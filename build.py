import subprocess

subprocess.run(["pyinstaller", "--noconfirm", "--onefile", "--windowed", "run.py"])
"""
pyinstaller --noconfirm --onefile --windowed  "/home/pedrogiroldo/Documentos/Projetos/lista-da-wanessador/run.py"
"""
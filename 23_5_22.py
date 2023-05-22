##打印彩色酷炫文字
##pip install colorama
##pip install termcolor
##pip install prettytable
##pip install progressbar
##pip install pyfiglet

import colorama
from termcolor import colored
from prettytable import PrettyTable
import progressbar
import pyfiglet

print(colored('hello','red'),colored('world','green'))

print(colored('hello','red',attrs=['reverse','blink']))


print(colored(pyfiglet.figlet_format('hello world'),'red'))
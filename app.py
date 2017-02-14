from requests import get
from time import sleep
from random import randint
from sys import stdout, argv
from termcolor import colored

site = "{}".format(argv[1])

with open("words_for_parse.txt") as openfile:
    list_ = openfile.readlines()

numWords = len(list_)
free = []
owned = []

def wait():
    sleep(randint(3,5))

for idx, x in enumerate(list_, 1):
    link = "https://" + site + "/" + x
    q = get(link)
    if 200 != q.status_code:
        free.append(x.rstrip())
        wait()
    else:
        owned.append(x.rstrip())
        wait()
    stdout.write('\r')
    part = float(idx)/(numWords)
    symbols_num = int(30 * part)
    stdout.write("[%-30s] %3.2f%%" % ('='*symbols_num, part*100))
    stdout.flush()

print("\n{0}".format(colored("Free words for " + site + ":", 'green', 'on_white', attrs=['underline'])))
with open("freeLoginsFor_{0}.txt".format(), "a") as f:
    for i in free:
        f.write(i)
        print(i)
print("\n{0}\n".format(colored("Owned words for " + site + ":", 'red', 'on_white', attrs=['underline'])))
for i in owned:
    print(i)

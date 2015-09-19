import requests
import time
import random
import sys
from termcolor import colored

###
platform = "{}".format(sys.argv[1])
li = []
###

free = []
owned = []
lenLi = len(li)

buildTextFree = "Free words for " + platform + ":"
textFree = colored(buildTextFree, 'green', 'on_white', attrs=['underline'])
buildTextOwned = "Owned words for " + platform + ":"
textOwned = colored(buildTextOwned, 'red', 'on_white', attrs=['underline'])

def wait():
    time.sleep(random.randint(2,3))

for step_number, x in enumerate(li, 1):
	link = "https://" + platform + "/" + x
	q = requests.get(link)
	stat = q.status_code
	if 200 != stat:
		free.append(x.rstrip())
		#print(x)
		wait()
	else:
		owned.append(x.rstrip())
		#print(x)
		wait()
	sys.stdout.write('\r')
	part = float(step_number)/(lenLi)
	symbols_num = int(30 * part)
	sys.stdout.write("[%-30s] %3.2f%%" % ('='*symbols_num, part*100))
	sys.stdout.flush()

print("\n")
print(textFree)
for i in free:
	print(i)
print("\n")
print(textOwned)
for i in owned:
        print(i)
print('\n')

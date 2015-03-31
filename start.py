import requests
import time
import random
import sys

li = ["25min", "tester", "testsetset"]

status404 = []
status200 = []
lenLi = len(li) + 1
def wait():
    time.sleep(random.randint(2,3))

for x in li:
	
	link = "https://vk.com" + x
	q = requests.get(link)
	stat = q.status_code
	if 200 != stat:
		status404.append(x.rstrip())
		wait()
	else:
		status200.append(x.rstrip())
		wait()
	for i in range(lenLi):
		sys.stdout.write('\r')
		sys.stdout.write("[%-30s] %d%%" % ('='*i, i))
		sys.stdout.flush()

print("404 status")
for i in status404:
	print(i)
print("\n")
print("- - - - -\n")
print("200 status:")
for i in status200:
        print(i)

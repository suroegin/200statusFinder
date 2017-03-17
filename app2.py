from requests import get
from time import sleep
from random import randint
from sys import argv

domain = "{}".format(argv[1])
if argv[2]:
    chk_list = argv[2]
full_link = "https://" + domain + "/"
file_with_results = "~/Yandex.Disk/Research/" + domain + "_free_names.txt"

if chk_list:
    with open(chk_list) as openfile:
        list_ = openfile.readlines()
else:
    with open("check_list.txt") as openfile:
        list_ = openfile.readlines()

def wait():
    sleep(randint(5,8))

with open(file_with_results, "w") as f:
    f.write("Free names for {0}\n\n".format(domain))

for name in list_:
    print("Checking name '{0}' for domain '{1}'".format(name.strip(), domain))
    if get(full_link + name.strip()).status_code != 200:
        print("{0} is free!".format(name.strip()))
        with open(file_with_results, "a") as f:
            f.write("{0} --- {1}{2} --- {3}\n".format(name.strip(), full_link, name.strip(), len(name.strip())))
            wait()
    else:
        wait()
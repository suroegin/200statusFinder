from requests import get
from time import sleep
from random import randint
from sys import argv
import os

TXT_FILES_DIR = "./txt_files/"
domain = "{0}".format(argv[1])
if argv[2]:
    chk_list = "{0}".format(argv[2])
    file_with_results = "/root/Yandex.Disk/Research/{0}_free_names_from_file_{1}.txt".format(domain, chk_list)
else:
    file_with_results = "/root/Yandex.Disk/Research/{0}_free_names_from_file_{1}.txt".format(domain, file_)
full_link = "https://" + domain + "/"


def get_list_from_obj(obj):
    with open(obj) as openfile:
        list_ = openfile.readlines()
        return list_

def wait():
    sleep(randint(5,8))

def check_process(list_):
    for name in list_:
        print("Checking name '{0}' for domain '{1}'".format(name.strip(), domain))
        if get(full_link + name.strip()).status_code != 200:
            print("{0} is free!".format(name.strip()))
            with open(file_with_results, "a") as f:
                f.write("{0} --- {1}{2} --- {3}\n".format(name.strip(), full_link, name.strip(), len(name.strip())))
                wait()
        else:
            wait()

if chk_list:
    list_ = get_list_from_obj(chk_list)
    with open(file_with_results, "w") as f:
        f.write("Free names for {0}\nFile: {1}\n\n".format(domain, chk_list))
    check_process(list_)
else:
    files = os.listdir(TXT_FILES_DIR)
    for file_ in files:
        list_ = get_list_from_obj(file_)
        with open(file_with_results, "w") as f:
            f.write("Free names for {0}\nFile: {1}\n\n".format(domain, file_))
        check_process(list_)

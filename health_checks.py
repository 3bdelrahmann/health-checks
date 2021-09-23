#!/usr/bin/env python3

import shutil
import psutil

#Function the will recieve a disk check and
#returns true if there's more the 20% free or false if its less
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total *100
    return free > 20

#Function to check the usage for a whole second and
#returns true if the cpu_usage is less than 75% or false if its more
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or  not check_cpu_usage():
    print("Danger".upper())
else:
    print(":) Your computer is healthy ;)".upper())

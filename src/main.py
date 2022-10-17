#! /usr/bin/env python

import platform
import os
import psutil


# gpu info
gpu_unix_command = "lspci | grep VGA"
cpu_unix_command = "cat /proc/cpuinfo | grep name"

result = os.popen(gpu_unix_command).readlines()
cpu_info = os.popen(cpu_unix_command).read().split('\n')

gpus = ""

for i in result:
    gpus += str(i.split(":")[2]).split('(')[0]

os_name = platform.node()
kernel = platform.release()


memory = {
        'total':round(psutil.virtual_memory().total/(1024*1024)),
        'free':round(psutil.virtual_memory().free/(1024*1024)),
        'used':round(psutil.virtual_memory().used/(1024*1024)),
}

fetch = f"""        OS: {os_name}
        Kernel: {kernel}
        DE: {os.environ.get("DESKTOP_SESSION")}
        CPU: {cpu_info[0].split(':')[1]}
        GPU: {gpus}
        Memory: {memory['used']} MiB / {memory['total']} MiB"""

print(fetch)

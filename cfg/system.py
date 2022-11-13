import psutil

cpu_per = int(psutil.cpu_percent(1))
mem_info = int(psutil.virtual_memory()[2])

HOST = ""
PORT = 
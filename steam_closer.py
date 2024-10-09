import os, re, signal
from datetime import datetime


exe = 'Telegram.exe'
exe = 'steam'



while True:
    def get_pid(exe_name):
        pid_list =os.popen(f'wmic process get description, processid | findstr {exe}').read()
        reg_pid_list = re.findall(r'\d+', pid_list)
        return reg_pid_list

    pids = get_pid(exe)
    
    if datetime.now().hour >= 17:
        break
    if len(pids) < 1:
        continue
    elif len(pids) == 1:
        os.system(f'taskkill /PID {pids[0]} /F')
        pids = []
    else:
        for pid in pids:
            os.system(f'taskkill /PID {pid} /F')
            pids = []
        
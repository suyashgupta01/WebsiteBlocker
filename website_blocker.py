import sys
import ctypes
import inspect
import time
import socket

if not hasattr(sys.modules[__name__], '__file__'): # to create a __file__ variable to store a file name (wasn't being created due to some reason)
    __file__ = inspect.getfile(inspect.currentframe())

def is_admin(): # check if the script has admin privileges
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def website_blocker():        
    f = open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'a+')
    while True:
        choice = input("\n\nWhat do you want to do? \n1: block\n2: redirect\n3: remove block/ redirect\n4: exit\n\n")
        if choice == '1':
            website = input("Enter the website to block: ")
            with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "a+") as f:    
                f.write("127.0.0.1     " + website + "\n") # creating an entry having a false ip (using local host) for a domain name
            print(website + " blocked successfully!")
        elif choice == '2':
            website1 = input("Enter the website from which redirection has to occur: ")
            website2 = input("Enter the website to which redirection has to occur: ")
            ip_of_website2 = socket.gethostbyname(website2)
            with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "a+") as f:
                f.write(ip_of_website2 + "     " + website1 + "\n")
            print(website1 + " redirected successfully to " + website2 + "!")
        elif choice == '3':
            website = input("Enter the website to unblock/ remove redirect: ")
            with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "r") as f:
                content = f.read()
            if website in content:
                x = content.split("\n")
                for item in x:
                    if website in item:
                        x.remove(item)
                        # now converting content to a string to overwrite the file with it
                        content_string = ""
                        for item in x:
                            content_string = content_string + item + "\n"
                        with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "w") as f:
                            f.write(content_string)
                        print(website + " unblocked successfully!")
            else:
                print(website + " was never blocked/redirected! It was and remains accessible from this PC!")
        elif choice == '4':
            print("\n\n\nThank you for using Suyash's Website Blocker!\n\n\n")
            print("Closing in 3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            break
        else:
            print("invalid choice! Try again!")


def main():
    if is_admin():
        website_blocker()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


main()
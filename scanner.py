import sys
from datetime import datetime as dt
import socket
import threading

def scan_port (target,port):
    try :
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        result=s.connect_ex((target,port))#error indicator-if port is open then result is 0
        if result==0 :
            print (f"the port {port} is open")
        s.close()
    except socket.error as e :
        print(f"error on port {port}: {e}")
    except Exception as e :
        print (f"unexpected error on port {port} : {e}")


#main function-target definition and argument validation 
def main ():
    if len(sys.argv)==2 :
        target=sys.argv[1]
    else :
        print("invalid arguments")
        print("argumnts should be in the form of : python.exe scanner.py <target>")
        sys.exit(1)
    #resolving the target hostname to an ip address 
    try:
        target_ip=socket.gethostbyname(target)
    except socket.gaierror :
        print("error: couldnt resolve the hostname")
    
    print("-" *50 )
    print (f"scanning target{target_ip}")
    print (f"start time {dt.now()}")
    print ("-" *50 )

    #this next part is going to use multithreading which allows us to scan more than one port at once
    #and makes this script alot more faster snce there are alot of ports to scan
    try: 
        threads=[]
        for port in range(1,65536):
            thread=threading.Thread(target=scan_port , args=(target_ip,port))
            threads.append(thread)
            thread.start()

    # making sure all threads are completed
        for thread in threads:
            thread.join()

            
    except KeyboardInterrupt :
        print("\nexiting program")
        sys.exit(0)
    except socket.error as e:
        print(f"socket error : {e}")
        sys.exit(1)
    print("-" *50)
    print("scan completed")
    print("-" *50)
#this next step insures that our code will onlyrun on this fuile
#this step wont allow it to be imported anywhere else
#this is just best practice
#if u want it to be imported somewhere else just remove the if
if __name__=="__main__":
    main()


"""
okay so, quick recap 
i firstly made the scan port function which is going to scan every single port,
from 1 t 65535,
then it will be providing the target which can be a host name or ip
if the error indicator is 0 that means our port is open,
if it is open we will close the connection and do it all over again for the next port
if we have an error it ll print the error
if we have an exception it will print the exception error
to run the code you will get this error message here :
PS C:\Users\user\Desktop\python_programming_100> & C:/Users/user/Desktop/python_programming_100/.venv/Scripts/python.exe c:/Users/user/Desktop/python_programming_100/scanner.py
and you will need t go to the CLI and press the up arrow, and type in ur ip address
u can get ur ip from the cmd bby using ip config
and it will scan for your open ports
"""






        
                     


    
# Imporing OS for executing the Linux Commands 
import os
#importing getpass for echo back less authentication
import getpass


from aws import aws
from devops import docker 
from linux_basic import lvm
#from hadoop import
#from mlops import


####################             Credits              ####################
def credits():
    os.system("tput setaf 11")
    print("\t\t\t\t\t\t\t\t\t\t\t    Made by :")
    print("\t\t\t\t\t\t\t\t\t\t\t Janhavi Jain, kodgire Ashutosh")
    print("\t\t\t\t\t\t\t\t\t  Akshit Modi, Gursimar Singh, Sourav Pattnaik")
    os.system("tput setaf 7")




#################                Functions             ###################


#Username Password Auth Function
def auth():
    os.system("tput setaf 3")
    passwd = getpass.getpass("Enter your Password to login to console:")
    apass = "redhat"
    if passwd != apass:
        print("\n")
        os.system("tput setaf 1")
        print("Incorrect Password!")
        print("Try Again.....")
        os.system("tput setaf 7")
        exit()
    else:
        target()
        os.system("tput setaf 2")
        print("Logging to the console")
        credits()

##################            local// remote           ###################

def target():
    os.system("tput setaf 2")
    print("Where do you want to perform your job?(remote/local)")
    location=input()
    global loc
    global ip
    global user
    global password
    if location=="remote" or location=="Remote" or location=="r" or location=="R":
        loc="r"
        os.system("tput setaf 3")
        ip=input("Enter your IP address:")
        user=input("Enter username:")
        #os.system("tput setaf 0")
        #password=input()
        password=getpass.getpass("Enter password of {} user: ".format(user))

    elif location=="local" or location=="Local" or location=="l" or location=="L":
        loc="l"
        ip="0.0.0.0"
        user="root"
        password="NA"
    else:
        print("Please enter a valid location")
        target()
#########################
def exited():
    os.system("clear")
    os.system("tput setaf 2")
    print("\t\t\t\t\t\t\tThank You ")
    print("\t\t\t\t\t\tExiting from Our system")
    os.system("tput setaf 3")
    print("----------------------------------------------------------------------------------------------------------------------")
    credits()
    os.system("tput setaf 3")
    input("Press Enter to continue....")
    os.system("tput setaf 7")
    os.system("clear")



###############################################
def menu():
    head()
    global ch
    os.system("tput setaf 2")
    print("\t\t\t\t\tWhich service You want to access?")
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.AWS
        \t\t\t\t2.Hadoop
        \t\t\t\t3.devops
        \t\t\t\t4.docker
        \t\t\t\t5.Web Server
        \t\t\t\t6.Machine Learning
        \t\t\t\t7.Basics of Linux
        \t\t\t\t8.Exit
        ''')
    os.system("tput setaf 7")
    ch = int(input("What do you want to do:"))



#################################################
def main():
    while True:
        menu()
        if ch==1:
            aws.run()
            #continue    
        elif ch==2:
            #hadoop.hadoop()
            print("Hadoop")
        elif ch==3:
            print("devops")
        elif ch==4:
            print("docker")
            docker.run(loc,ip,user,password)
        elif ch==5:
            print("webserver")
        elif ch==6:
            print("machine learning")   
        elif ch==7:
            lvm.run(loc,ip,user,password)
            print("basic linux")       
        elif ch==8:
            exited()
            break
        else:
            os.system("tput setaf 1")
            print("Please enter a valid option")
            os.system("tput setaf 3")
            input("Press enter to show menu again")
            menu()



#################################

# Heading Display function
def head():
    os.system("clear")
    print("\n")
    os.system("tput setaf 1")
    print("\t\t\t\t\t\tHey! Welcome to our System")
    os.system("tput setaf 7")
    print("----------------------------------------------------------------------------------------------------------------------")



###########################


################               Authentication            ######################
head()
auth()
os.system("sleep 1 ")
################               Main functions             #####################
main()
os.system("clear")
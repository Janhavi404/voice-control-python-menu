import os
####################             Credits              ####################

def credits():
    os.system("tput setaf 11")
    print("\t\t\t\t\t\t\t\t\t\t\t    Made by :")
    print("\t\t\t\t\t\t\t\t\t\t\t Janhavi Jain, kodgire Ashutosh")
    print("\t\t\t\t\t\t\t\t\t  Akshit Modi, Gursimar Singh, Sourav Pattnaik")
    os.system("tput setaf 7")

#######################        functions          #######################
###########################    disk detail         #############
def disk_detail():
    os.system("fdisk -l")

def ssh_disk_detail():
    os.system("sshpass -p {2} ssh {1}@{0} fdisk -l".format(ip,user,passwd))


##################             create vg         #################
def create_vg(device_name,vname):
    os.system("vgcreate {1} /dev/{0}".format(device_name,vname))

def ssh_create_vg(device_name,vname):
    os.system("sshpass -p {4} ssh {3}@{2} vgcreate {1} /dev/{0}".format(device_name,vname,ip,user,passwd))


    ##############          Extend  vg        #####################
def extend_vg(device_name,vname):
    os.system("vgextend {1} /dev/{0}".format(device_name,vname))

def ssh_extend_vg(device_name,vname):
    os.system("sshpass -p {4} ssh {3}@{2} vgextend {1} /dev/{0}".format(device_name,vname,ip,user,passwd))


#################      display vg       ################
def display_vg(vname):
    os.system("vgdisplay {}".format(vname))

def ssh_display_vg(vname):
    os.system("sshpass -p {3} ssh {2}@{1} vgdisplay {0}".format(vname,ip,user,passwd))


#################      display all vg       ################
def display_all_vg():
    os.system("vgdisplay")

def ssh_display_all_vg():
    os.system("sshpass -p {2} ssh {1}@{0} vgdisplay".format(ip,user,passwd))


    ##############          remove  vg        #####################
def remove_vg(vname):
    os.system("vgremove {} ".format(vname))

def ssh_remove_vg(vname):
    os.system("sshpass -p {3} ssh {2}@{1} vgextend {0}".format(vname,ip,user,passwd))

###################         create logical volume   ####################

def create_lvm(size,vname,lname):
    os.system("lvcreate --size {2} --name {1} {0}".format(vname,lname,size))

def ssh_create_lvm(size,vname,lname):
    os.system("sshpass -p {5} ssh {4}@{3} lvcreate --size {2} --name {1} {0}".format(vname,lname,size,ip,user,passwd))

###################           mount lvm              #################

def format_lvm(lname,vname):
    os.system("mkfs.ext4 /dev/{1}/{0}".format(lname,vname))
def mount_lvm(lname,vname,fname):
    os.system("mkdir /{}".format(fname))
    os.system("mount /dev/{2}/{1} /{0}".format(fname,lname,vname))

def ssh_format_lvm(lname,vname):
    os.system("sshpass -p {4} ssh {3}@{2} mkfs.ext4 /dev/{1}/{0}".format(lname,vname,ip,user,passwd))
def ssh_mount_lvm(lname,vname,fname):
    os.system("sshpass -p {3} ssh {2}@{1} mkdir /{0}".format(fname,ip,user,passwd))
    os.system("sshpass -p {5} ssh {4}@{3} mount /dev/{2}/{1} /{0}".format(fname,lname,vname,ip,user,passwd))

##################                  display lvm        ###############
def display_lvm(lname,vname):
    os.system("lvdisplay /dev/{1}/{0}".format(lname,vname))

def ssh_display_lvm(lname,vname):
    os.system("sshpass -p {4} ssh {3}@{2} lvdisplay /dev/{1}/{0}".format(lname,vname,ip,user,passwd))


##################                  display all lvm        ###############
def display_all_lvm(lname,vname):
    os.system("lvdisplay")

def ssh_display_all_lvm(lname,vname):
    os.system("sshpass -p {2} ssh {1}@{0} lvdisplay".format(ip,user,passwd))

####################              Extend lvm             #################

def extend_lvm(lname,vname,size):
    os.system("lvextend --size {2} /dev/{1}/{0}".format(lname,vname,size))

def ssh_extend_lvm(lname,vname,size):
    os.system("sshpass -p {5} ssh {4}@{3} lvextend --size {2} /dev/{1}/{0}".format(lname,vname,size,ip,user,passwd))

############################
def menu_style():
        os.system("clear")
        print("\n")
        os.system("tput setaf 2")
        print("\t\t\t\t\t\tWelcome to LVM console")
        os.system("tput setaf 7")
        print("----------------------------------------------------------------------------------------------------------------------")
#######################

def menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.See all disk details
        \t\t\t\t2.Create Volume Group(VG)
        \t\t\t\t3.Add more space to VG
        \t\t\t\t4.Display VG
        \t\t\t\t5.Display all VG
        \t\t\t\t6.Remove VG
        \t\t\t\t7.Crete logical volume
        \t\t\t\t8.Format and Mount partition
        \t\t\t\t9.Diplay lvm
        \t\t\t\t10.Display all lvm
        \t\t\t\t11.Extend lvm size
        \t\t\t\t12.Exit
        ''')
    os.system("tput setaf 7")
    global ch
    ch = int(input("What do you want to do:"))

################################################
def exited():
    os.system("clear")
    os.system("tput setaf 2")
    print("\t\t\t\t\t\t\tThank You ")
    print("\t\t\t\t\t\tExiting from LVM console")
    os.system("tput setaf 3")
    print("----------------------------------------------------------------------------------------------------------------------")
    credits()
    os.system("tput setaf 3")
    input("Press Enter to continue....")
    os.system("tput setaf 7")
    os.system("clear")


#############################
def run(loc,ip12,user12,passwd12):
    global user
    global passwd
    global ip
    user=user12
    passwd=passwd12
    ip=ip12
    n=1
    if loc=="l":
        os.system("tput setaf 2")
        print("Installing lvm dependencies...")
        os.system("dnf install lvm2-8:2.03.02-6.el8.x86_64")
        os.system("tput setaf 7")
    else:
        os.system("tput setaf 2")
        print("Installing lvm dependencies...")
        os.system("sshpass -p {2} ssh {1}@{0} dnf install lvm2-8:2.03.02-6.el8.x86_64".format(ip,user,passwd))
        os.system("tput setaf 7")
    while n>0:
        if loc=="l":
            menu()
            if ch==1:
                disk_detail()
            elif ch==2:
                vname=input("Enter new Volume Group name:")
                device_name=input("Enter device name (Eg. xvdh):")
                create_vg(device_name,vname)
            elif ch==3:
                vname=input("Enter VG name:")
                device_name=input("Enter device name - space you want to add (Eg. xvdh):")
                extend_vg(device_name,vname)
            elif ch==4:
                vname=input("Enter name of your VG:")
                display_vg(vname)
            elif ch==5:
                display_all_vg()
            elif ch==6:
                vname=input("Enter VG name:")
                remove_vg(vname)
            elif ch==7:
                lname=input("Enter name of lvm you want to give:")
                size=input("How much size of lvm you want? (Eg. 50MB):")
                vname=input("From which vg you want to get space:")
                create_lvm(size,vname,lname)
            elif ch==8:
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                format_lvm(lname,vname)
                fname=input("Enter folder name where you want to mount:")
                mount_lvm(lname,vname,fname)
            elif ch==9:
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                display_lvm(lname,vname)
            elif ch==10:
                display_all_lvm()
            elif ch==11:
                size=input("How much size you want to add:")
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                extend_lvm(lname,vname,size)
            elif ch==12:
                exited()
                break
            else:
                os.system("tput setaf 1")
                print("Please enter a valid option")
                os.system("tput setaf 3")
                input("Press enter to show menu again")
                menu()
            input("Press Enter to continue....")
            os.system("clear")

        else:
            menu()
            if ch==1:
                ssh_disk_detail()
            elif ch==2:
                vname=input("Enter new Volume Group name:")
                device_name=input("Enter device name (Eg. xvdh)")
            elif ch==3:
                vname=input("Enter VG name:")
                device_name=input("Enter device name - space you want to add (Eg. xvdh):")
                ssh_extend_vg(device_name,vname)
            elif ch==4:
                vname=input("Enter name of VG:")
                display_vg(vname)
            elif ch==5:
                ssh_display_all_vg()
            elif ch==6:
                vname=input("Enter VG name:")
                ssh_remove_vg(vname)
            elif ch==7:
                lname=input("Enter name of lvm you want to give:")
                size=input("How much size of lvm you want? (Eg. 50MB):")
                vname=input("From which vg you want to get space:")
                ssh_create_lvm(size,vname,lname)
            elif ch==8:
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                ssh_format_lvm(lname,vname)
                fname=input("Enter folder name where you want to mount:")
                ssh_mount_lvm(lname,vname,fname)
            elif ch==9:
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                ssh_display_lvm(lname,vname)
            elif ch==10:
                ssh_display_all_lvm()
            elif ch==11:
                size=input("How much size you want to add:")
                lname=input("Enter name of lvm:")
                vname=input("Which VG lvm belongs to:")
                ssh_extend_lvm(lname,vname,size)
            elif ch==12:
                exited()
                break
            else:
                os.system("tput setaf 1")
                print("Please enter a valid option")
                os.system("tput setaf 3")
                input("Press enter to show menu again")
                menu()
            input("Press Enter to continue....")
            os.system("clear")
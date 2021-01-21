import os
####################             Credits              ####################
def credits():
    os.system("tput setaf 11")
    print("\t\t\t\t\t\t\t\t\t\t\t    Made by :")
    print("\t\t\t\t\t\t\t\t\t\t\t Janhavi Jain, kodgire Ashutosh")
    print("\t\t\t\t\t\t\t\t\t  Akshit Modi, Gursimar Singh, Sourav Pattnaik")
    os.system("tput setaf 7")

##################          services start -stop        ###################

def start_docker():
    os.system("tput setaf 2")
    print("Starting docker services...")
    os.system("systemctl start docker")
    os.system("systemctl enable docker")
    print("Docker services are permanently started")
    os.system("tput setaf 7")

def ssh_start_docker(ip):
    os.system("tput setaf 2")
    print("Starting docker services in remote host...")
    os.system("sshpass -p {2} ssh {1}@{0} systemctl start docker".format(ip,user,passwd))
    os.system("sshpass -p {2} ssh {1}@{0} systemctl enable docker".format(ip,user,passwd))
    print("Docker services are permanently started")
    os.system("tput setaf 7")


##################
def stop_docker():
    os.system("tput setaf 1")
    print("Stopping docker services...")
    os.system("systemctl stop docker")
    os.system("systemctl disable docker")
    print("Docker services are permanently stopped")
    os.system("tput setaf 7")


def ssh_stop_docker(ip):
    os.system("tput setaf 1")
    print("Stopping docker services in remote host...")
    os.system("sshpass -p {2} ssh {1}@{0} systemctl stop docker".format(ip,user,passwd))
    os.system("sshpass -p {2} ssh {1}@{0} systemcyl disable docker".format(ip,user,passwd))
    print("Docker services are permanently stopped")
    os.system("tput setaf 7")


#################                 CONTAINER              ###################
def new_con(name,image):
    os.system("tput setaf 2")
    os.system("docker container run -dit --name {0} {1}".format(name,image)) 
    os.system("tput setaf 7")
def ssh_new_con(name,image,ip):
    os.system("tput setaf 2")
    os.system("sshpass -p {4} ssh {3}@{2} docker container run -dit --name {0} {1}".format(name,image,ip,user,passwd)) 
    os.system("tput setaf 7")
#2
def attach_con(name):
    os.system("tput setaf 2")
    os.system("docker container start {}".format(name))
    os.system("docker container attach {}".format(name))
    os.system("tput setaf 7")
def ssh_attach_con(name,ip):
    os.system("tput setaf 2")
    os.system("sshpass -p {3} ssh {2}@{1} docker container start {0}".format(name,ip,user,passwd))
    os.system("sshpass -p {3} ssh {2}@{1} docker container attach {0}".format(name,ip,user,passwd))
    os.system("tput setaf 7")
#3
def list_run_con():
    os.system("docker container ls")
def ssh_list_run_con(ip):
    os.system("sshpass -p {2} ssh {1}@{0} docker container ls".format(ip,user,passwd))
#4
def list_stop_con():
    os.system("docker container ls -a")
def ssh_list_stop_con(ip):
    os.system("sshpass -p {2} ssh {1}@{0} docker container ls -a".format(ip,user,passwd))
#5
def inspect_con(name):
    os.system("docker container inspect {} ".format(name))
def ssh_inspect_con(name,ip):
    os.system("sshpass -p {3} ssh {2}@{1} docker container inspect {0} ".format(name,ip,user,passwd))
#6
def stop_con(name):
    os.system("tput setaf 1")
    os.system("docker container stop {}".format(name))
    os.system("tput setaf 7")
def ssh_stop_con(name,ip):
    os.system("tput setaf 1")
    os.system("sshpass -p {3} ssh {2}@{1} docker container stop {0}".format(name,ip,user,passwd))
    os.system("tput setaf 7")
#7
def rename_con(name,new):
    os.system("docker container rename {0} {1}".format(name,new))
def ssh_rename_con(name,new,ip):
    os.system("sshpass -p {4} ssh {3}@{2} docker container rename {0} {1}".format(name,new,ip,user,passwd))
#8
def rm_con(name):
    os.system("tput setaf 1")
    os.system("docker container rm -f {}".format(name))
    os.system("tput setaf 7")
def ssh_rm_con(name,ip):
    os.system("tput setaf 1")
    os.system("sshpass -p {3} ssh {2}@{1} docker container rm -f {0}".format(name,ip,user,passwd))
    os.system("tput setaf 7")
#9
def rm_all_con():
    os.system("tput setaf 1")
    os.system("docker container rm -f $(docker ps -a -q)")
    os.system("tput setaf 7")
def ssh_rm_all_con(ip):
    os.system("tput setaf 1")
    os.system("sshpass -p {2} ssh {1}@{0} docker container rm -f $(sshpass -p {2} ssh {1}@{0} docker ps -a -q)".format(ip,user,passwd))
    os.system("tput setaf 7")
#10
def img_con(name,img):
    os.system("docker commit {0} {1} ".format(name,img))
def ssh_img_con(name,img,ip):
    os.system("sshpass -p {4} ssh {3}@{2} docker commit {0} {1} ".format(name,img,ip,userpasswd))

##################                IMAGES            #####################
#1
def pull_img(name):
    os.system("docker pull {}".format(name))
def ssh_pull_img(name,ip):
    os.system("sshpass -p {3} ssh {2}@{1} docker pull {0}".format(name,ip,user,passwd))
#2
def list_img():
    os.system("docker image ls")
def ssh_list_img(ip):
    os.system("sshpass -p {2} ssh {1}@{0} docker image ls".format(ip,user,passwd))
#3
def rm_img(name):
    os.system("tput setaf 1")
    os.system("docker image rm {}".format(name))
    os.system("tput setaf 7")
def ssh_rm_img(name,ip):
    os.system("tput setaf 1")
    os.system("sshpass -p {3} ssh {2}@{1} docker image rm {0}".format(name,ip,user,passwd))
    os.system("tput setaf 7")
#4
def inspect_img(name):
    os.system("docker image inspect {}".format(name))
def ssh_inspect_img(name,ip):
    os.system("sshpass -p {3} ssh {2}@{1} docker image inspect {0}".format(name,ip,user,passwd))
#def push_img(name):
    #os.system("docker image ls")
###################                 NETWORK            ########################
#1
def new_network(network,driver):
    os.system("tput setaf 2")
    os.system("docker network create -d {0} {1} ".format(driver,network))
    os.system("tput setaf 7")
def ssh_new_network(network,driver,ip):
    os.system("tput setaf 2")
    os.system("sshpass -p {4} ssh {3}@{2} docker network create -d {0} {1} ".format(driver,network,ip,user,passwd))
    os.system("tput setaf 7")
#2                
def list_network():
    os.system("docker network ls")
def ssh_list_network(ip):
    os.system("sshpass -p {2} ssh {1}@{0} docker network ls".format(ip,user,passwd))
#3
def inspect_network(name):
    os.system("docker network inspect {}".format(name))
def ssh_inspect_network(name,ip):
    os.system("sshpass -p {3} ssh {2}@{1} docker network inspect {0}".format(name,ip,user,passwd))
#4              
def disconnect_network(name,network):
    os.system("tput setaf 1")
    os.system("docker network disconnect -f {0} {1}".format(network,name))
    os.system("tput setaf 7")
def ssh_disconnect_network(name,network,ip):
    os.system("tput setaf 1")
    os.system("sshpass -p {4} ssh {3}@{2} docker network disconnect -f {0} {1}".format(network,name,ip,user,passwd))
    os.system("tput setaf 7")
#5                
def connect_network(name,network):
    os.system("tput setaf 2")
    os.system("docker network connect {0} {1}".format(network,name))
    os.system("tput setaf 7")
def ssh_connect_network(name,network,ip):
    os.system("tput setaf 2")
    os.system("sshpass -p {4} ssh {3}@{2} docker network connect {0} {1}".format(network,name,ip,user,passwd))
    os.system("tput setaf 7")
#6
def rm_network(network):
    os.system("tput setaf 1")
    os.system("docker network rm {}".format(network))
    os.system("tput setaf 7")
def ssh_rm_network(network,ip):
    os.system("tput setaf 1")
    os.system("sshpass -p {3} ssh {2}@{1} docker network rm {0}".format(network,ip,user,passwd))
    os.system("tput setaf 7")
#################                 VOLUME               ######################
#1
def create_vol(vol):
    os.system("tput setaf 2")
    os.system("docker volume create {}".format(vol))
    os.system("tput setaf 7")
def ssh_create_vol(vol,ip):
    os.system("tput setaf 2")
    os.system("sshpass -p {3} ssh {2}@{1} docker volume create {0}".format(vol,ip,user,passwd))
    os.system("tput setaf 7")
#2
def list_vol():
    os.system("docker volume ls")
def ssh_list_vol(ip):
    os.system("sshpass -p {2} ssh {1}@{0} docker volume ls".format(ip,user,passwd))
#3
def inspect_vol(vol):
    os.system("docker volume inspect {}".format(vol))
def ssh_inspect_vol(vol,ip):
    os.system("sshpass -p {3} ssh {2}@{1} docker volume inspect {0}".format(vol,ip,user,passwd))
#4
def rm_vol(vol):
    os.system("tput setaf 1")
    os.system("docker volume rm {}".format(vol))
    os.system("tput setaf 7")
def ssh_rm_vol(vol,ip):
    os.system("tput setaf 1")
    os.system("sshpass -p {3} ssh {2}@{1} docker volume rm {0}".format(vol,ip,user,passwd))
    os.system("tput setaf 7")
################           MULTI-TIER Architecture         ##################
def multi_tier_architecture():
    os.system("tput setaf 3")
    os.system("docker-compose up -d")
def ssh_multi_tier_architecture(ip):
    os.system("tput setaf 3")
    os.system("sshpass -p {2} ssh {1}@{0} docker-compose up -d".format(ip,user,passwd))

##############            PUSH IMAGE TO DOCKER HUB         #################
def push_img(img,user_name):
    os.system("tput setaf 2")
    os.system("docker login")
    print("Creating a new image with tag for pushing to docker hub....")
    os.system("docker image tag {0} {1}/{0}".format(img,user_name))
    os.system("docker push {1}/{0}".format(img,user_name))
    os.system("tput setaf 7")

def ssh_push_img(img,user_name,ip):
    os.system("tput setaf 2")
    os.system("docker login")
    print("Creating a new image with tag for pushing to docker hub....")
    os.system("sshpass -p {4} ssh {3}@{2} docker image tag {0} {1}/{0}".format(img,user_name,ip,user,passwd))
    os.system("sshpass -p {4} ssh {3}@{2} docker push {1}/{0}".format(img,user_name,ip,user,passwd))
    os.system("tput setaf 7")
#############################################################################

def menu_style():
    os.system("clear")
    print("\n")
    os.system("tput setaf 2")
    print("\t\t\t\t\t\tWelcome to docker console")
    os.system("tput setaf 7") 
    print("----------------------------------------------------------------------------------------------------------------------")

#######################

def exited():
    os.system("clear")
    os.system("tput setaf 2")
    print("\t\t\t\t\t\t\tThank You ")
    print("\t\t\t\t\t\tExiting from Docker console")
    os.system("tput setaf 3")
    print("----------------------------------------------------------------------------------------------------------------------")

    credits()
    os.system("tput setaf 3")
    input("Press Enter to continue....")
    os.system("tput setaf 7")
    os.system("clear")

##############

def menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.Start docker service
        \t\t\t\t2.Stop docker service
        \t\t\t\t3.Container
        \t\t\t\t4.Images
        \t\t\t\t5.Networking
        \t\t\t\t6.Volume
        \t\t\t\t7.Create a multi-tier architecture
        \t\t\t\t8.Pull image to docker Hub
        \t\t\t\t9.push image to docker hub
        \t\t\t\t10.Exit
        ''')
    os.system("tput setaf 7")
    global ch
    ch = int(input("What do you want to do:"))

#############

def con_menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.Create a new container
        \t\t\t\t2.Attach conatainer
        \t\t\t\t3.List all running containers
        \t\t\t\t4.List all stopped containers
        \t\t\t\t5.Inspect container
        \t\t\t\t6.Stop running container
        \t\t\t\t7.Rename container
        \t\t\t\t8.Remove a container
        \t\t\t\t9.Remove all containers
        \t\t\t\t10.Create a new image from a container
        \t\t\t\t11.back
        ''')
    os.system("tput setaf 7")
    global op
    op=int(input("Enter your choice:"))
###############
def images_menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.Pull image from docker hub
        \t\t\t\t2.List all images
        \t\t\t\t3.Remove image
        \t\t\t\t4.Inspect image
        \t\t\t\t5.Create a new image from a container
        \t\t\t\t6.Push image to docker Hub
        \t\t\t\t7.back
        ''')
    os.system("tput setaf 7")
    global op
    op=int(input("Enter your choice:"))

############
def network_menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.Create a new network
        \t\t\t\t2.List all networks
        \t\t\t\t3.Inspect a network
        \t\t\t\t4.disconnect from a network
        \t\t\t\t5.Connect to a network
        \t\t\t\t6.Remove a network
        \t\t\t\t7.back
        ''')
    os.system("tput setaf 7")
    global op
    op=int(input("Enter your choice:"))
############
def volume_menu():
    menu_style()
    os.system("tput setaf 3")
    print('''
        \t\t\t\t1.Create a new volume
        \t\t\t\t2.List all volumes
        \t\t\t\t3.Inspect a volume
        \t\t\t\t4.Remove a volume
        \t\t\t\t5.back''')
    os.system("tput setaf 7")
    global op
    op=int(input("Enter your choice:"))

#############################################################################

def run(loc,ip,user12,passwd12):
    global user
    global passwd
    user=user12
    passwd=passwd12
    n=1
    while n>0:
        if loc=="l":
            menu()
            if ch==1:
                start_docker()
            elif ch==2:
                stop_docker()
###################                CONTAINER             ####################

            elif ch==3:
                con_menu()
                if op==1:
                    name=input("Enter name of container\nEg aks\n:") 
                    image=input("Enter name of image \nEg.centos:latest\n:")
                    new_con(name,image)
                elif op==2:
                    name=input("Enter a name of container you want to attach:")
                    attach_con(name)
                    break
                elif op==3:
                    list_run_con()
                elif op==4:
                    list_stop_con()
                elif op==5:
                    name=input("Enter a container name you want to inspect:")
                    inspect_con(name)
                elif op==6:
                    name=input("Enter a name of container you want to stop:")
                    stop_con(name)
                elif op==7:
                    name=input("Enter a name of container you want to rename:")
                    new=input("Enter a new name:")
                    rename_con(name,new)
                elif op==8:
                    name=input("Enter a name of container you want to remove:")
                    rm_con(name)
                elif op==9:
                    rm_all_con()
                elif op==10:
                    name=input("Enter container name:")
                    img=input("Enter a name of image you want to make:\nEg.myimage:v1\n:")
                    img_con(name,img)
                elif op==11:
                    continue
                else:
                    os.system("tput setaf 1")
                    print("Please enter a valid option")
                    os.system("tput setaf 3")
                    input("Press enter to show menu again")
                    con_menu()

######################             IMAGES             #######################


            elif ch==4:
                images_menu()
                if op==1:
                    name=input("Enter a image name you want to pull from docker hub:\nEg.centos:latest\n:")
                    pull_img(name)
                elif op==2:
                    list_img()
                elif op==3:
                    name=input("Enter a name of image you want to remove:")
                    rm_img(name)
                elif op==4:
                    name=input("Enter a name of image you want to inspect:")
                    inspect_img(name)
                elif op==5:
                    name=input("Enter container name:")
                    img=input("Enter a name of image you want to make:\nEg.myimage:v1\n:")
                    img_con(name,img)
                elif op==6:
                    menu_style()
                    img=input("Enter a name of image you want to push:")
                    user_name=input("Enter your docker repostory username:")
                    push_img(img,user_name)
                elif op==7:
                    continue
                else:
                    os.system("tput setaf 1")
                    print("Please enter a valid option")
                    os.system("tput setaf 3")
                    input("Press enter to show menu again")
                    images_menu()


####################                NETWORK          ########################


            elif ch==5:    
                network_menu()
                if op==1:
                    network=input("Enter a name of a network you want to create:")
                    driver=input("Enter a name of driver\nEg bridge\n:")
                    new_network(network,driver)
                elif op==2:
                    list_network()
                elif op==3:
                    name=input("Enter a name of network you want to inspect:")
                    inspect_network(name)
                elif op==4:
                    name=input("Enter name of container you want to disconnect:")
                    network=input("Enter network of {} container\nEg.bridge\n:".format(name))
                    disconnect_network(name,network)
                elif op==5:
                    name=input("Enter name of container you want to connect:")
                    network=input("Which network you want to connet\nEg.bridge\n:")
                    connect_network(name,network)
                elif op==6:
                    network=input("Enter a name of network you want to remove:")
                    rm_network(network)
                elif op==7:
                    continue
                else:
                    os.system("tput setaf 1")
                    print("Please enter a valid option")
                    os.system("tput setaf 3")
                    input("Press enter to show menu again")
                    network_menu()



#################                 VOLUME               ######################


             
            elif ch==6:
                volume_menu()
                if op==1:
                    vol=input("Enter a name of volume you want to create:")
                    create_vol(vol)
                elif op==2:
                    list_vol()
                elif op==3:
                    vol=input("Enter a name of volume you want to inspect:")
                    inspect_vol(vol)
                elif op==4:
                    vol=input("Enter a name of volume you want to remove:")
                    rm_vol(vol)
                elif op==5:
                    continue
                else:
                    os.system("tput setaf 1")
                    print("Please enter a valid option")
                    os.system("tput setaf 3")
                    input("Press enter to show menu again")
                    volume_menu()



################           MULTI-TIER Architecture         ##################

            
            elif ch==7:
                menu_style()
                os.system("tput setaf 3")
                print('''
                    1.Create a Multi-tier architecure of phpmyadmin-mysql
                    ''')
                os.system("tput setaf 3")
                multi_tier_architecture()
                os.system("tput setaf 7")


###################     Pull image from DOCKER HUB        ######################



            elif ch==8:
                name=input("Enter a image name you want to pull from docker hub:\nEg.centos:latest\n:")
                pull_img(name)



##############            PUSH IMAGE TO DOCKER HUB         ################


            elif ch==9:
                menu_style()
                img=input("Enter a name of image you want to push:")
                user_name=input("Enter your docker repostory username:")
                push_img(img,user_name)


###################                EXIT              #######################


            elif ch==10:
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


###################         remote access           ###############

        else:
            menu()
            if ch==1:
                ssh_start_docker(ip,)
            elif ch==2:
                ssh_stop_docker(ip)
###################                CONTAINER             ####################
            elif ch==3:
                con_menu()
                if op==1:
                    name=input("Enter name of container\nEg aks\n:") 
                    image=input("Enter name of image \nEg.centos:latest\n:")
                    ssh_new_con(name,image,ip)
                elif op==2:
                    name=input("Enter a name of container you want to attach:")
                    ssh_attach_con(name,ip)
                    break
                elif op==3:
                    ssh_list_run_con(ip)
                elif op==4:
                    ssh_list_stop_con(ip)
                elif op==5:
                    name=input("Enter a container name you want to inspect:")
                    ssh_inspect_con(name,ip)
                elif op==6:
                    name=input("Enter a name of container you want to stop:")
                    ssh_stop_con(name,ip)
                elif op==7:
                    name=input("Enter a name of container you want to rename:")
                    new=input("Enter a new name:")
                    ssh_rename_con(name,new,ip)
                elif op==8:
                    name=input("Enter a name of container you want to remove:")
                    ssh_rm_con(name,ip)
                elif op==9:
                    ssh_rm_all_con(ip)
                elif op==10:
                    name=input("Enter container name:")
                    img=input("Enter a name of image you want to make:\nEg.myimage:v1\n:")
                    ssh_img_con(name,img,ip)
                elif op==11:
                    continue
                else:
                    os.system("tput setaf 1")
                    print("Please enter a valid option")
                    os.system("tput setaf 3")
                    input("Press enter to show menu again")
                    con_menu()
                    

######################             IMAGES             #######################


            elif ch==4:
                images_menu()
                if op==1:
                    name=input("Enter a image name you want to pull from docker hub:\nEg.centos:latest\n:")
                    ssh_pull_img(name,ip)
                elif op==2:
                    ssh_list_img(ip)
                elif op==3:
                    name=input("Enter a name of image you want to remove:")
                    ssh_rm_img(name,ip)
                elif op==4:
                    name=input("Enter a name of image you want to inspect:")
                    ssh_inspect_img(name,ip)
                elif op==5:
                    name=input("Enter container name:")
                    img=input("Enter a name of image you want to make:\nEg.myimage:v1\n:")
                    ssh_img_con(name,img,ip)
                elif op==6:
                    menu_style()
                    img=input("Enter a name of image you want to push:")
                    user_name=input("Enter your docker repostory username:")
                    ssh_push_img(img,user_name,ip)
                elif op==7:
                    continue
                else:
                    os.system("tput setaf 1")
                    print("Please enter a valid option")
                    os.system("tput setaf 3")
                    input("Press enter to show menu again")
                    images_menu()


####################                NETWORK          ########################


            elif ch==5:    
                network_menu()
                if op==1:
                    network=input("Enter a name of a network you want to create:")
                    driver=input("Enter a name of driver\nEg bridge\n:")
                    ssh_new_network(network,driver,ip)
                elif op==2:
                    ssh_list_network(ip)
                elif op==3:
                    name=input("Enter a name of network you want to inspect:")
                    ssh_inspect_network(name,ip)
                elif op==4:
                    name=input("Enter name of container you want to disconnect:")
                    network=input("Enter network of {} container\nEg.bridge\n:".format(name))
                    ssh_disconnect_network(name,network,ip)
                elif op==5:
                    name=input("Enter name of container you want to connect:")
                    network=input("Which network you want to connet\nEg.bridge\n:")
                    ssh_connect_network(name,network,ip)
                elif op==6:
                    network=input("Enter a name of network you want to remove:")
                    ssh_rm_network(network,ip)
                elif op==7:
                    continue
                else:
                    os.system("tput setaf 1")
                    print("Please enter a valid option")
                    os.system("tput setaf 3")
                    input("Press enter to show menu again")
                    network_menu()


#################                 VOLUME               ######################


             
            elif ch==6:
                volume_menu()
                if op==1:
                    vol=input("Enter a name of volume you want to create:")
                    ssh_create_vol(vol,ip)
                elif op==2:
                    ssh_list_vol(ip)
                elif op==3:
                    vol=input("Enter a name of volume you want to inspect:")
                    ssh_inspect_vol(vol,ip)
                elif op==4:
                    vol=input("Enter a name of volume you want to remove:")
                    ssh_rm_vol(vol,ip)
                elif op==5:
                    continue
                else:
                    os.system("tput setaf 1")
                    print("Please enter a valid option")
                    os.system("tput setaf 3")
                    input("Press enter to show menu again")
                    volume_menu()



################           MULTI-TIER Architecture         ##################

            
            elif ch==7:
                menu_style()
                os.system("tput setaf 3")
                print('''
                    1.Create a Multi-tier architecure of phpmyadmin-mysql
                    ''')
                os.system("tput setaf 3")
                ssh_multi_tier_architecture(ip)
                os.system("tput setaf 7")


###################     Pull image from DOCKER HUB        ######################



            elif ch==8:
                name=input("Enter a image name you want to pull from docker hub:\nEg.centos:latest\n:")
                ssh_pull_img(name,ip)



##############            PUSH IMAGE TO DOCKER HUB         ################


            elif ch==9:
                menu_style()
                img=input("Enter a name of image you want to push:")
                user_name=input("Enter your docker repostory username:")
                ssh_push_img(img,user_name,ip)


###################                EXIT              #######################


            elif ch==10:
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
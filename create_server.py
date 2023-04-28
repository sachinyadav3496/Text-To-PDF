#!/usr/bin/python3
import os

PWD = os.getcwd()

##########################################
#            yum configuration
##########################################

repo = os.path.join(PWD, "server_data/rhel9.1/x86_64/dvd")
base_repo = os.path.join(repo, "BaseOS")
app_repo = os.path.join(repo, "AppStream")

repo_file=f"""
[BaseOS]
name=BaseOS
baseurl=file://{base_repo}
enabled=1
gpgcheck=0

[AppStream]
name=AppStream
baseurl=file://{app_repo}
enabled=1
gpgcheck=0
"""

os.system("rm -rf /etc/yum.repos.d/*")

with open("/etc/yum.repos.d/abc.repo", "w") as fp:
    fp.write(repo_file)
    fp.close()

os.system("yum repolist")
os.system("yum repoinfo")

print("\n\n\t\tYum Server Configured Sucessfully!\n\n")

#######################################################



#######################################################
#             HTTP Server Configuration
#######################################################

os.system("yum install -y httpd")

os.system(f"cp -rf {PWD}/server_data/* /var/www/html/")

os.system("firewall-cmd --permanent --add-service=http")	
os.system("firewall-cmd --permanent --add-port=80/tcp")	
os.system("firewall-cmd --reload")


os.system("systemctl enable httpd")
os.system("systemctl restart httpd")

print("\n\n\t\tHTTP Server Configured Sucessfully!\n\n")

repo_file=f"""
[BaseOS]
name=BaseOS
baseurl=http://localhost/rhel9.1/x86_64/dvd/BaseOS
enabled=1
gpgcheck=0

[AppStream]
name=AppStream
baseurl=http://localhost/rhel9.1/x86_64/dvd/AppStream
enabled=1
gpgcheck=0
"""

os.system("rm -rf /etc/yum.repos.d/*")
with open("/etc/yum.repos.d/abc.repo", "w") as fp:
    fp.write(repo_file)
    fp.close()

os.system("yum repolist")
os.system("yum repoinfo")

print("\n\n\t\tYum Server Configured Sucessfully!\n\n")
#######################################################



########################################################
#                  NFS Server Configuration
########################################################

os.system("yum install -y nfs-utils")

for sno in range(60):
    os.system(f"mkdir -p /our_home/netuser{sno}")
    os.system(f"chmod 777 /our_home/netuser{sno}")
    with open(f"/our_home/netuser{sno}/hello.txt", "w") as fp:
        fp.write("Hello World! If you can see this message\n")
        fp.write("\t\tIt means your autofs is configured sucessfully!")
        fp.write("\n\n\n\t\t\tBe Happy! Enjoy!\n")
        fp.close()
    with open(f"/etc/exports", "a") as fp:
        fp.write(f"/our_home/netuser{sno}    *(rw,sync)\n")
        fp.close()


os.system("chmod 777 -R /our_home")

os.system("firewall-cmd --permanent --add-service=nfs")	
os.system("firewall-cmd --permanent --add-service=mountd")	
os.system("firewall-cmd --reload")


os.system("systemctl restart nfs-server")
os.system("systemctl enable nfs-server")

os.system("exportfs -rv")


print("\n\n\tNFS Server Configured Sucessfully!\n\n")

#######################################################



#######################################################
#               disabling Selinux 
#######################################################

with open("/etc/selinux/config", "w") as fp:
    fp.write("SELINUX=permissive\n")
    fp.write("SELINUXTYPE=targeted\n")
    fp.close()

os.system("setenforce 0")

print("\n\n\t\tSelinux Configured Sucessfully!\n\n")


#######################################################

print("\n\nServer Initialized Sucessfully! Enjoy Learning\n\n")


#######################################################
#######################################################

# Text to PDF converter Application

### Build Application Image From Dockerfile using Following Command

`podman image build -t myapp .`

### List Created Image using Following Command

`podman image ls`

### Run a Container in Background using image we just created



`mkdir -p /data/input`

`mkdir -p /data/output`

`podman container run -d --name myapp  -v /data/input:/data/input:Z -v /data/output:/data/output:Z myapp`

### Verify Container is Running

`podman ps`

### Create Systemd Daemon of given Container

`mkdir -p ~/.config/systemd/user`

`cd ~/.config/systemd/user`

`podman generate systemd --name myapp --new --files`

`systemctl --user enable container-myapp.service`

`systemctl --user start container-myappp.service`

### Reboot System and check your container will be in running state

`podman ps`

### Check application is working or not by following command 

`echo "something into textfile to be converted into pdf file" > /data/input/hello.txt`

###### now check converted pdf file in output directory using following command

`ls -lh /data/output`

you can see podman application is converting input text file into pdf file! that's great

#### Happy Learning! :-)

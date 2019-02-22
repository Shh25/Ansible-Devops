<p align="center">
  <img width="200" height="200" src="https://upload.wikimedia.org/wikipedia/commons/e/e1/North_Carolina_State_University_Athletic_logo.svg">
</p>

# CSC519_Project Milestone 1
CSC-519 Spring 2019

## Authors
[Prayani Singh](https://github.ncsu.edu/psingh25)(psingh25@ncsu.edu) <br>
[Shefali Agarwal](https://github.ncsu.edu/Sdagarwa)(sdagarwa@ncsu.edu) <br>
[Sujal Sujal](https://github.ncsu.edu/ssujal)(ssujal@ncsu.edu) <br>
[Vaibhav Singh](https://github.ncsu.edu/vsingh7)(vsingh7@ncsu.edu) <br>


# Configuration Management and Build Milestone

In this milestone, you will complete the following tasks:

:white_check_mark: Provisioning and configuring an jenkins server (on a remote VM), automatically using ansible. <br>

:white_check_mark: Using a combination of jenkins-job-builder and ansible, automatically setup build jobs for two applications: <br>
>  * A nodejs web application [checkbox.io](https://github.com/chrisparnin/checkbox.io).
>  * An "enterprise" Java system [iTrust](https://github.ncsu.edu/engr-csc326-staff/iTrust2-v4)

:white_check_mark: Using a combination of mocha/pm2, create a test script that will start and stop the checkbox.io service on the server. A starting place might be [the App](https://github.com/CSC-DevOps/App/blob/master/test/simple.js) we used in the Pipelines workshop. <br>

:white_check_mark: Create a simple git hook or GitHub webhook to trigger a build when a push is made to the repo.   _You may use a forked/cloned version of the two systems._ Demonstrate a passing build for each job after a commit. <br>
  

## Clone repository
```
git clone https://github.ncsu.edu/ssujal/CSC519_Project.git
```

## Prerequisites
1. Install VirtualBox - version 5.2.* (Please install this version for baker to run smoothly. Vagrant can be used instead but extra setup and steps will be required to setup successfully)
2. Install Vagrant
3. Install Baker ([Baker website](https://docs.getbaker.io/installation/)) - latest stable version


## Installation and Instructions
1. Clone project from git repository
2. Create public and private key in ansible-srv directory from CLI using the command:
```
cd ansible-srv
ssh-keygen -t rsa -b 4096 -C "web-srv" -f web-srv
```
## Starting Web Server
1. Go into directory web-srv
```
cd web-srv
```
2. Create VM using baker (called from baker.yml).This will also save your public key in directory ~/.ssh/public_key which we need to add in authorized_keys once we are logged into the VM.
```
baker bake
```
3. Start VM using baker. Use command:
```
baker ssh
```
4. Set public key: (append key from public_key to authorized_keys)
```
cat ~/.ssh/public_key >> ~/.ssh/authorized_keys
```

## Starting Ansible Server
1. Go into directory ansible-srv
```
cd ansible-srv
```
2. Create VM using baker (called from baker.yml). This will also install ansible in the server directly and save your private key in directory ~/.ssh/web-srv which we need to add in in order to access the web server (Please do not share this key with anybody).
```
baker bake
```
3. Start VM using baker. Use command:
```
baker ssh
```
4. Change permission of private key
```
chmod 600 ~/.ssh/web-srv
```
5. Changed into linked directory for ansible server
```
cd /ansible-srv/
```
6. Call Ansible Playbook using inventory from main.yml file
```
ansible-playbook main.yml -i inventory
```

## ScreenCast link
//TO DO

## Link to project wiki
https://github.ncsu.edu/ssujal/CSC519_Project/wiki

## Link to forked repositories
https://github.com/Shh25/checkbox.io

https://github.ncsu.edu/vsingh7/iTrust2-v4



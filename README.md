<p align="center">
  <img width="200" height="200" src="https://upload.wikimedia.org/wikipedia/commons/e/e1/North_Carolina_State_University_Athletic_logo.svg">
</p>

# Devops_CSC519_Project
CSC-519 Spring 2019

## Authors
[Prayani Singh](https://github.ncsu.edu/psingh25)(psingh25@ncsu.edu) <br>
[Shefali Agarwal](https://github.ncsu.edu/Sdagarwa)(sdagarwa@ncsu.edu) <br>
[Sujal Sujal](https://github.ncsu.edu/ssujal)(ssujal@ncsu.edu) <br>
[Vaibhav Singh](https://github.ncsu.edu/vsingh7)(vsingh7@ncsu.edu) <br>

## Clone repository
```
git clone https://github.ncsu.edu/ssujal/CSC519_Project.git
```

# Devops_CSC519_Project Milestones 
<details><summary>MILESTONE 1</summary>

## Build Milestones

In this milestone, we have completed the following tasks:

:white_check_mark: Provisioning and configuring an jenkins server (on a remote VM), automatically using ansible. <br>

:white_check_mark: Using a combination of jenkins-job-builder and ansible, automatically setup build jobs for two applications: <br>
>  * A nodejs web application [checkbox.io](https://github.com/chrisparnin/checkbox.io).
>  * An "enterprise" Java system [iTrust](https://github.ncsu.edu/engr-csc326-staff/iTrust2-v4)

:white_check_mark: Using a combination of mocha/pm2, create a test script that will start and stop the checkbox.io service on the server. <br>

:white_check_mark: Create a simple git hook or GitHub webhook to trigger a build when a push is made to the repo. Demonstrate a passing build for each job after a commit. <br>

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
6. Open vars/common.yml in the project directory, add required credentials for database, jenkins, checkbox and iTrust.
A few variables have been supplied by us. These include a few URLs and plugins. Please do not make modifications to these existing variables as it may lead to incorrect installation of the project.

Note:
- For github credentials: please specify credentials from github.ncsu.com. These variables are used in our iTrust forked repository which is checked into https://github.ncsu.edu/. 
- For mail user and password, please specify credentials for any SMTP server (check for security measures if using server for non-standard protocols). 

7. Once the required credentials have been added, vault the common.yml file by calling this command:
````
ansible-vault encrypt vars/common.yml
````
This will encrypt your variable file and prompt for a password which can be used every time you want to run the Ansible playbook.

8. Call Ansible Playbook using inventory from main.yml file
```
ansible-playbook main.yml -i inventory --ask-vault-pass
```
This will prompt you for vault password. Enter password as added in step 7. This should run the Ansible Playbook.

9. Once everything is installed successfully, Jenkins can be accessed on the following port:
````
192.168.33.100:8080
````
It will prompt you for username and password, enter credentials as specified in vars/commons.yml for Jenkins. Once you are logged into Jenkins portal. You should see project builds for Checkbox and iTrust in a healthy state. To check working of the builds through Git hook, go to the next step.

## Jenkins Builds
To check Jenkins builds on commit, go into forked repository directory on web server. (as specified in vars/commons.yml). 
- CheckBox: Go into project directory where the server files are located. Commit a few changes into this repository and push it to the server. Open browser on Jenkins port as specified above.
Open jenkins on specified location above and check if the build is running.

- iTrust: Go into project directory where the server files are located. Commit a few changes into this repository and push it to the server. Open browser on Jenkins port as specified above.
Open jenkins on specified location above and check if the build is running.

## ScreenCast link
https://drive.google.com/drive/folders/1mXXmxJ1JYzsIzeRBpfsbZqc69qA-OorE?usp=sharing
</details>

## MILESTONE 2

## Build Milestones
In this milestone, we have completed the following tasks:

:white_check_mark: Code coverage, analysis for iTrust <br>
:white_check_mark: Fuzzer and Test Prioritization for iTrust <br>
:white_check_mark: Static Code Analysis for Checkbox <br>
:white_check_mark: Reports and Analysis <br>

## ChangeLog
1. Renamed main.yml > playbook.yml
2. var/common.yml > variables.yml (in root directory)
3. Added reports directory containing itrust and Checkbox reports

## Prerequisites
1. Setup web and ansible server as given in Milestone 1
2. Please make sure Milestone 1 along with the roles mentioned in scripts are up and running

## Starting Ansible Server
1. Changed into linked directory for ansible server
```
cd /ansible-srv/
```
2. Open variables.yml in the project directory, add required config and variable names for jenkins, checkbox and iTrust.
A few variables have been supplied by us. These include a few URLs and plugins. Please do not make modifications to these existing variables as it may lead to incorrect installation of the project.

3. Call Ansible Playbook using inventory from playbook.yml file
```
ansible-playbook playbook.yml -i inventory --ask-vault-pass
````

## Code Coverage, analysis for iTrust
1. Code coverage uses a plugin called [Jacoco](https://www.eclemma.org/jacoco/)
2. Static code analysis is conducted through plugin called [Checkstyle](http://checkstyle.sourceforge.net/)
2. Checkstyle analyses static code and Reports all warnings and errors. Report includes bugs, syntax warnings etc.
3. Configured through Jenkins and reports are displayed on Jenkins Job portal
4. Build fails when coverage is lesser than 50%

## Fuzzer and Test Prioritization for iTrust
1. There are 2 roles called Fuzzer and Test Prioritization. Fuzzer role is not included in playbook.yml and is run inside Test Prioritization role
2. Number of runs in variables.yml indicate how many times fuzzer will run
3. Number of seconds in variables.yml indicate the wait time before the next build is triggered. We have added the time as 250 seconds but it may differ based on system configuration
4. 

## Static Code Analysis for Checkbox
1. There is a single file called analysis.js that runs for analysisng all files in Checkbox
2. Build failing criteria is based on failing one of the following: 
- When a method is longer than 25 lines
- When there are more than 10 conditions in a function

## Reports and Analysis
https://github.ncsu.edu/ssujal/CSC519_Project/tree/master/reports
Includes:
1. Description Report
2. Test Prioritization Report
3. Sample Coverage Report
4. Checkbox Analysis Report

<details><summary>MILESTONE 3</summary>
  <p>
    ```python
    print("Coming soon!")
    ``` 
  </p> 
</details>

## Wiki and Repository Links

## Project Wiki
https://github.ncsu.edu/ssujal/CSC519_Project/wiki

## Forked Repositories
https://github.com/Shh25/checkbox.io

https://github.ncsu.edu/vsingh7/iTrust2-v4


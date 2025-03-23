In this project we will use Jenkins to create a simple workflow.

**#1 part: run on local Windows**

We will use port 8080 for Jenkins on Windows.

![image](https://github.com/user-attachments/assets/a14adfb8-038b-4362-ba62-ffb28e99b4ee)

Jenkinsfile for my pipeline can be checked [here](https://github.com/denisboboi492/CAPL-CANoe-Python/blob/main/Jenkins/WJenkinsfile).

Jenkinsfile is a configuration for a pipeline, which is a series of automated tasks. The pipeline is written in Groovy. My configuration consists of 3 stages:
1. Build - building the project
2. Setup Python - check if python is installed
3. Test Script - runs a python script

**#2 part: run on docker container**

Short info: A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings. Containers isolate software from its environment and ensure that it works uniformly despite differences for instance between development and staging.

For Docker Container, port 8082 will be used.



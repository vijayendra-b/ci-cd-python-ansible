# CI/CD workflow using Jenkins and Ansible with a Python application.


## Project Structure
```
ci-cd-python-demo/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│
├── tests/
│   └── test_app.py
│
├── Dockerfile
├── Jenkinsfile
│
├── ansible/
│   ├── inventory.ini
│   └── deploy.yml
│
└── README.md

```

## Tools Used

GitHub – Source code repository

Jenkins – CI/CD automation

Ansible – Deployment automation

Docker – Containerization

Docker Hub – Image registry

Python (Flask) – Demo application

# Configure Jenkins

Jenkins Setup

1. Install Jenkins

2. Install plugins:

- Git

- Docker Pipeline

- Ansible

3. Configure:

- Docker

- Docker Hub credentials

- GitHub access

## End-to-End Flow

1.  Developer commits code to GitHub

2. Jenkins pipeline is triggered

3. Jenkins:

- Pulls code

- Runs tests

- Builds Docker image

- Pushes image to Docker Hub

4. Jenkins triggers Ansible

5. Ansible deploys the Docker container

6. App is accessible at: http://localhost:5000

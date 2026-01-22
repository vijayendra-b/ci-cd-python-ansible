pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vijayendra1/python-cicd-demo"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/vijayendra-b/ci-cd-python-ansible.git'
            }
        }

        stage('Install Dependencies & Test') {
            steps {
                sh 'pip install pytest'
                sh 'pytest tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withDockerRegistry([url: 'https://index.docker.io/v1/', credentialsId: 'b799765c-9aab-4075-8537-541d450e7f9d']) {
                    sh 'docker push $DOCKER_IMAGE:latest'
                }
            }
        }

        stage('Deploy using Ansible') {
            steps {
                sh 'ansible-playbook ansible/deploy.yml -i ansible/inventory.ini'
            }
        }
    }
}

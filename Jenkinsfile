pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vijayendra1/python-cicd-demo"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vijayendra-b/ci-cd-python-ansible.git'
            }
        }

        stage('Install Dependencies & Test') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r app/requirements.txt
                    python3 -m pip install pytest
                    python3 -m pytest tests/
                '''
            }
        }

        stage('Verify Docker') {
            steps {
                sh '''
                which docker
                docker --version
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '/usr/local/bin/docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'b799765c-9aab-4075-8537-541d450e7f9d',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push vijayendra1/python-cicd-demo:latest
                    '''
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

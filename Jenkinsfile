pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "abhiyadav260/caps-shopping-app"
    }

    stages {

        stage('Clean Old Containers') {
            steps {
                sh '''
                docker stop caps-app || true
                docker rm caps-app || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                sh 'docker push $DOCKER_IMAGE:latest'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d -p 8000:8000 --name caps-app $DOCKER_IMAGE:latest
                '''
            }
        }
    }
}

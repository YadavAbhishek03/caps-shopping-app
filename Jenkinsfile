pipeline {
    agent any

    stages {

        stage('Clean Old Containers') {
            steps {
                sh '''
                docker stop caps-app || true
                docker rm caps-app || true
                docker rmi caps-app-image || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t caps-app-image .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name caps-app caps-app-image'
            }
        }
    }
}

pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "abhiyadav260/caps-shopping-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('SonarQube Analysis') {
            steps {
		script {
            	    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') {
                    	sh """
                    	${scannerHome}/bin/sonar-scanner \
                    	-Dsonar.projectKey=caps-shopping-app \
                    	-Dsonar.sources=.
                    	"""
                    }
            	}
	    }
        }

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
                sh '''
                docker build -t $DOCKER_IMAGE:$IMAGE_TAG .
                docker tag $DOCKER_IMAGE:$IMAGE_TAG $DOCKER_IMAGE:latest
                '''
            }
        }

	stage('Trivy Security Scan') {
    	    steps {
                sh '''
        	trivy image --severity HIGH,CRITICAL $DOCKER_IMAGE:latest
        	'''
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
                sh '''
                docker push $DOCKER_IMAGE:$IMAGE_TAG
                docker push $DOCKER_IMAGE:latest
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop caps-app || true
                docker rm caps-app || true
                docker run -d -p 8000:8000 --name caps-app $DOCKER_IMAGE:$IMAGE_TAG
                '''
            }
        }
    }
}

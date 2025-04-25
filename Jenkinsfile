pipeline {
    agent any
    
    environment {
        DOCKER_CREDS = credentials('docker-pass')
        DOCKER_REPO = "ranaalshehri/swe645-extracredit-app-amd64"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_REPO}:latest ."
                }
            }
        }
        
        stage('Push Docker Image') {
            steps {
                script {
                    sh """
                      docker login -u \$DOCKER_CREDS_USR -p \$DOCKER_CREDS_PSW
                      docker push ${DOCKER_REPO}:latest
                    """
                }
            }
        }

        stage('Updating Cluster Pods'){
            steps{
                script{
                    sh "kubectl rollout restart deployment survey-deployment"
                }
            }

        }
    }
    
    post {
        always {
            echo 'Cleaning up workspace...'
        }
        success {
            echo 'Docker image built and pushed successfully.'
        }
        failure {
            echo 'Build failed. Please check the console output for errors.'
        }
    }
}
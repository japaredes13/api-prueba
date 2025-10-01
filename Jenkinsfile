pipeline {
    agent any

    environment {
        IMAGE_NAME = "mi-fastapi"
        IMAGE_TAG  = "latest"
        CONTAINER_NAME = "fastapi-test"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Run container') {
            steps {
                sh "docker run -d --rm --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }

        stage('Verify service') {
            steps {
                script {
                    // Verificar que la app responda en /docs o /
                    sh """
                        sleep 5
                        curl -f http://localhost:8000/docs || (docker logs ${CONTAINER_NAME} && exit 1)
                    """
                }
            }
        }

        stage('Cleanup') {
            steps {
                sh "docker stop ${CONTAINER_NAME} || true"
            }
        }
    }
}

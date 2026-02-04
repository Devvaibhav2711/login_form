pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo "Cloning project..."
                git branch: 'main', url: 'https://github.com/your-repo-link.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                sh "docker build -t registration-form-app ."
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "Running Container..."
                sh "docker run -d -p 5000:5000 registration-form-app"
            }
        }
    }
}

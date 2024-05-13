pipeline {
    agent any

    environment {
        // Define environment variables
        GIT_URL = 'https://github.com/iqbal-faisal788/gde_devops.git'
        PARAM = 'Hello!'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo "Hello ${env.PARAM}"
                git branch:'main', url:env.GIT_URL
            }
        }
        
        stage('Build') {
            steps {
                sh 'echo build stage is running!'
            }
        }
    }
}

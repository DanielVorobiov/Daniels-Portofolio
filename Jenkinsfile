pipeline{
    agent agent {
        docker { image 'python:3.9.0' }
    }
    options {
        timestamps()
    }
    stages {
        stage('Build') { 
            steps { 
                sh 'make' 
            }
        }
    }
}

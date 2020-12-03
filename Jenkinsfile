pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('build'){
            steps{
                echo "Hello World"
                sh ' pip install --upgrade -r requirements.txt'
            }
        }
    }
}

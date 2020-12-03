pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('build'){
            steps{
                echo "Hello World"
                sh 'source venv/bin/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}

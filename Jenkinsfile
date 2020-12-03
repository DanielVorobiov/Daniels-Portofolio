pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('build'){
            steps{
                echo "Hello World"
                sh 'virtualenv env && source env/bin/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}

pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                echo "Hello World!"
                bat 'virtualenv env && source env/bin/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}


pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                echo "Hello World!"
                git clone 'https://github.com/DanielVorobiov/Daniels-Portofolio.git'
                bat 'virtualenv env && source env/bin/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}


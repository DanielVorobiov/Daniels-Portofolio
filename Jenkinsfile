pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                bat 'dir'
                
                git  'https://github.com/DanielVorobiov/Daniels-Portofolio.git'
        //        bat ' source venv/Scripts/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}


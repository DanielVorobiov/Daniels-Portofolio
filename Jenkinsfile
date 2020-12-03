pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                bat 'dir'
                bad 'cd Portofolio'
                bad 'dir'
                git  'https://github.com/DanielVorobiov/Daniels-Portofolio.git'
        //        bat ' source venv/Scripts/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}


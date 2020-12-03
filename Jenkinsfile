pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                bat 'dir'
                bat 'cd venv/Scripts/activate' // && pip install --upgrade -r requirements.txt && cd Portofolio && manage.py test Portofolio.tests'
                bat 'dir'
                
        //        bat ' source venv/Scripts/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}


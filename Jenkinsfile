pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                bat 'dir'
                bat 'pip install django && cd venv/Scripts/ && activate && cd .. && cd .. &&  cd Portofolio &&  manage.py test Portofolio.tests'
                bat 'dir'
                
        //        bat ' source venv/Scripts/activate && pip install --upgrade -r requirements.txt'assoc .py=Python.File
            }
        }
    }
}


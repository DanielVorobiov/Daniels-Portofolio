pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                bat 'dir'
                bat 'cd venv/Scripts/ && activate && cd .. && cd .. &&  cd Portofolio && assoc .py=Python.File && manage.py test Portofolio.tests'
                bat 'dir'
                
        //        bat ' source venv/Scripts/activate && pip install --upgrade -r requirements.txt'
            }
        }
    }
}


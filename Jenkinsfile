pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                bat 'dir'
                bat 'cd venv/Scripts/ && activate && cd .. && cd .. &&  cd Portofolio &&  python manage.py test tests.tests && python manage.py test tests.form_test'
                bat 'dir'
                
        //        bat ' source venv/Scripts/activate && pip install --upgrade -r requirements.txt'assoc .py=Python.File
            }
        }
    }
}


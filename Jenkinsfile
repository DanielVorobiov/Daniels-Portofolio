pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                bat 'dir'
                bat 'cd venv/Scripts/ && activate && cd .. && cd .. &&  cd Portofolio  && python manage.py test tests.form_test && python manage.py test tests.registrationtest  && python manage.py test tests.filetypetest'
                bat 'dir'
                
      
            }
        }
    }
    post {
        success {
             emailext body: 'SUCCESSFULL', 
                 to:'vorobiov.daniel@gmail.com', 
                 subject: 'Test'         
        }
        failure{
            emailext body: 'FAILURE', 
                 to:'vorobiov.daniel@gmail.com', 
                 subject: 'Test' 
        }
    }
}


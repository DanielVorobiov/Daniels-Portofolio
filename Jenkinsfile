pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                bat 'dir'
                bat 'cd venv/Scripts/ && activate && cd .. && cd .. &&  cd Portofolio  && python manage.py test tests.form_test && python manage.py test tests.registrationtest  && python manage.py test tests.filetypetest &&  python manage.py test tests.picsnumbertest'
                bat 'dir'
                
      
            }
        }
    }
    post {
        success {
             emailext body: 'SUCCESSFULL', 
                 to:'vorobiov.daniel@gmail.com balaurdorina@gmail.com eric199k@gmail.com prisacarimarina06@gmail.com', 
                 subject: 'Test'         
        }
        failure{
            emailext body: 'FAILURE', 
                 to:'vorobiov.daniel@gmail.com balaurdorina@gmail.com eric199k@gmail.com prisacarimarina06@gmail.com', 
                 subject: 'Test' 
        }
    }
}





pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                bat 'dir'
                bat 'cd venv/Scripts/ && activate && cd .. && cd .. &&  cd Portofolio &&  python manage.py test tests.tests && python manage.py test tests.form_test'
                bat 'dir'
                
      
            }
        }
    }
    post {
        always {
            mailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test

        }
    }
}


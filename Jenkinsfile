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
            emailext body: '''${SCRIPT, template="build-report.groovy"}''',
                subject: "[Jenkins] REPORT",
                to: "user@example.com"
        }
    }
}


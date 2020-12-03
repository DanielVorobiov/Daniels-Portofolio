pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('build'){
            steps{
                script{
                python manage.py test Portofolio.tests   
                }
            }
        }
    }
}

pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('build'){
            steps{
                script{
                manage.py test Portofolio.tests   
                }
            }
        }
    }
}

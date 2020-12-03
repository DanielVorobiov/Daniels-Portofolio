pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('build'){
            steps{
                step{
                manage.py test Portofolio.tests   
                }
            }
        }
    }
}

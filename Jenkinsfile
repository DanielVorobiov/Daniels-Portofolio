pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('build'){
            steps{
                manage.py test Portofolio.tests            
            }
        }
    }
}

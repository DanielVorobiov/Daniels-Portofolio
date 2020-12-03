pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('build'){
            steps{
                script{
                sh 'cd Portofolio && ls'
                //python manage.py test Portofolio.tests   
                }
            }
        }
    }
}

pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('build'){
            steps{
                print("Hello World");
                ./Portofolio.manage.py runserver
            }
        }
    }
}

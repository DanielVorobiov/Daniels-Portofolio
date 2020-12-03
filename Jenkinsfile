pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('build'){
            steps{
                print("Hello World")
                python manage.py runserver
            }
        }
    }
}

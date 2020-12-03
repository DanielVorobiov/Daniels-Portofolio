#!/bin/bash

pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('build'){
            steps{
                sh 'make'
                //python manage.py test Portofolio.tests   
                
            }
        }
    }
}

#!/bin/bash

pipeline{
    agent any
    options {
        timestamps()
    }
    stages {
        stage('Build') { 
            steps { 
                sh 'make' 
            }
        }
        }
    }
}

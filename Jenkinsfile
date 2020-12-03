pipeline{
    agent {
        label 'N1'
    }
    options {
        timestamps()
    }
    stage('Run Shell Script on Special Node') {
  steps {
    node('SpecialNodeLabel') {
      script {
        sh "ls -l"
      }
    }
  }
}

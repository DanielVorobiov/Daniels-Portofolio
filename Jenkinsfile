pipeline{
    agent {
        label 'N1'
    }
    options {
        timestamps()
    }stages{
    stage('Run Shell Script on Special Node') {
  steps {
    node('SpecialNodeLabel') {
      script {
        sh "ls -l"
      }
    }}}
  }
}

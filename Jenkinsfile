pipeline{
    agent none
    options {
        timestamps()
    }
    stages{
    stage('Run Shell Script on Special Node') {
  steps {
    node('SpecialNodeLabel') {
      script {
        sh "ls -l"
      }
    }}}
  }
}

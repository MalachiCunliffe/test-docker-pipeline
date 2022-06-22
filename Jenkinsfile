pipeline {
        agent {
            docker {
            alwaysPull true
            image 'python'
            args '--entrypoint='
            }
        }
        stages {
            stage('run hello world') {
                steps {
                    script {
                        sh 'python hello_world.py'
                    }
                }
            }
        }
    }

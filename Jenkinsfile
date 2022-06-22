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
                        sh 'hello_world.py'
                    }
                }
            }
            stage('Curl google') {
                steps {
                    script {
                        sh 'curl_google.py'
                    }
                }
            }
        }
    }

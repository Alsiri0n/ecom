pipeline {
    agent {label "ubuntu"}

    stages {
        stage('SCM Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: scm.branches,
                    doGenerateSubmoduleConfigurations: true,
                    extensions: scm.extensions + [[$class: 'SubmoduleOption', parentCredentials: true]],
                    userRemoteConfigs: scm.userRemoteConfigs
                ])
                sh 'sudo cp -rvf * /root/ecom'
            }
        }
        stage('Build') {
            steps {
                sh 'sudo docker-compose -f /root/ecom/docker-compose.yml build'
            }
        }
        stage('Deploy') {
            steps {
                sh 'sudo docker-compose -f /root/ecom/docker-compose.yml up -d'
            }
        }
    }
}

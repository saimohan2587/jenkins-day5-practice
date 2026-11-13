pipeline {
    agent any
    environment {
        PYTHONPATH = "/home/saimohan/.local/lib/python3.13/site-packages"
    }
    stages {
        stage('Validate Syntax') {
            steps {
                sh 'python3 -m py_compile push_network_configs.py get_device_info.py'
            }
        }
        stage('Deploy Protocols to GNS3') {
            steps {
                sh 'python3 push_network_configs.py'
            }
        }
        stage('Verify Device Health') {
            steps {
                sh 'python3 get_device_info.py'
            }
        }
    }
    post {
        always {
            echo "Day 7 Pipeline finished executing from Git!"
        }
    }


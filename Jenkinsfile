pipeline {
    agent any
    environment {
        PYTHONPATH = "/home/saimohan/.local/lib/python3.13/site-packages:."
    }
    stages {
        stage('Unit Testing') {
            steps {
                sh 'python3 -m pytest test_network.py -v --junitxml=reports/test-results.xml'
            }
        }
        stage('Deploy Protocols to GNS3') {
            steps {
                sh 'python3 push_network_configs.py'
            }
        }
        stage('Verify & Generate Report') {
            steps {
                sh 'python3 get_device_info.py'
            }
        }
    }
    post {
        always {
            // 1. Publish visual test reports in Jenkins UI
            junit 'reports/test-results.xml'

            // 2. Archive the device health report as a permanent artifact
            archiveArtifacts artifacts: 'device_health_report.txt', allowEmptyArchive: false
        }
    }
}

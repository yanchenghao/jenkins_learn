pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Building..'
                sh 'python3 /Users/yanchenghao/PycharmProjects/PycharmProjects/pythonProject/robot_learn/hello.py'
            }
        }
        stage('test') {
            steps {
                echo 'testing..'
            }
        }
    }
    post {
        always {
            junit 'build/report/1.xml'
        }

    }
}
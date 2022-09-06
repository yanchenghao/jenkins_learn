pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Building..'
                sh 'python3 /Users/yanchenghao/PycharmProjects/PycharmProjects/pythonProject/robot_learn/hello.py'
            }
        }
    }
    post {
        always {
            junit 'build/reports/**/*.xml'
        }

    }
}
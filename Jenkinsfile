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
      success {
        mail to: '1147889259@qq.com',
             subject: "Failed Pipeline: ",
             body: "Something is wrong with "
        }
      }

//     post {
//         always {
//             junit 'build/report/1.xml'
//         }
//     }
// # 这将会获得测试结果，Jenkins 会持续跟踪并计算测试的趋势和结果。 如果存在失败的测试用例，Pipeline 会被标记为 “UNSTABLE”，在网页上用黄色表示， 这不同于使用红色表示的 “FAILED” 失败状态。
//
// 当出现测试失败时，通常可以从 Jenkins 中获取构建结果报告进行本地分析和测试。 Jenkins 内置支持存储构建结果报告，在 Pipeline 执行期间生成记录文件。
}
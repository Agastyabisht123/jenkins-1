#!/usr/bin/groovy

pipeline{
    agent { docker { image 'python:3.5.1' } }
    parameters {
        string(name: 'NAME', defaultValue: 'Auto', description: 'Who is running build') 
        string(name: 'EMAIL', defaultValue: 'kshitij5043@gmail.com', description: 'Whom to notify on build report')
    }
    stages {
        stage('build') {
            steps {
                echo 'Building..'
                echo "Build done by ${params.NAME}"
                sh 'python3 -m py_compile src/add.py zip.py lambda_function.py'
       
               
                
            }
        }
        stage('test') {
            steps {
                echo 'Testing..'
                sh 'python3 -m unittest'
            }
        }
      stage('deploy') {
            steps {
                echo 'Deploying..'
                sh 'python3 zip.py'
            }
        }
    }
post {
    success {
            echo 'SUCCESS'
            //mail to: "${params.EMAIL}",
            //subject: "Build Success ${currentBuild.fullDisplayName}",
            //body: " Build Success\n Build by: ${params.NAME}\n Build Name:  ${currentBuild.fullDisplayName} \n Build Url: ${env.BUILD_URL} "
        }
        failure {
            echo 'Failed.'
            //mail to: "${params.EMAIL}",
            //subject: "Pipeline has failed: ${currentBuild.fullDisplayName}",
            //body: "Error !! \n Build by: ${params.NAME}\n Build Name:  ${currentBuild.fullDisplayName} \n Build Url: ${env.BUILD_URL} "
        }
    }
}

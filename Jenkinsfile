	

pipeline{
    agent none
    parameters {
        string(name: 'NAME', defaultValue: 'Github Auto Build', description: 'Who is running build') 
        string(name: 'EMAIL', defaultValue: 'kshitij5043@gmail.com', description: 'Whom to notify on build report')
        
    }
    stages {
        stage('Setup'){
           agent  { label 'master' }
           steps{
	           echo 'Setting Up...'
               sh 'sudo apt-get install awscli'
               sh 'aws --version'
            }
        }
        stage('build') {
            agent  { docker { image 'python:3.5.1' } }
            steps {
                echo 'Building...'
                echo "Build done by ${params.NAME}"
                sh 'python3 -m py_compile src/add.py lambda_function.py'
            }
        }
        stage('test') {
            agent  { docker { image 'python:3.5.1' } }
            steps {
                echo 'Testing..'
                sh 'python3 -m unittest'
            }
        }
     
        
        stage('Deploy'){
           agent  { label 'master' }
           steps{
	       echo 'Deploying'
               sh 'zip -r  Jenkins.zip *'
               sh 'ls -all'
               sh 'aws lambda update-function-code --function-name python-cicd --zip-file fileb://Jenkins.zip'
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

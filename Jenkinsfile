@Library('web-service-helper-lib') _

pipeline {

	agent any
	
	environment {
        DOCKER_TARGET = 'e-learning-by-sse/search-l3s_search-service:latest'
		DEMO_SERVER = 'staging.sse.uni-hildesheim.de'
        DEMO_SERVER_USER = "elscha"
        
        dockerImage = ''
        REMOTE_UPDATE_SCRIPT = '/staging/update-compose-project.sh search-l3s-stack'
    }

    stages {

        stage('Git') {
            steps {
                cleanWs()
                git branch: 'main', url: 'https://github.com/e-Learning-by-SSE/search-l3s_search_service.git'
            }
        }
		
		stage('Check') {
            steps {
                sh 'python3 -m py_compile *.py'
            }
        }
		
		stage('Build') {
            steps {
                script {
                    // Based on:
                    // - https://e.printstacktrace.blog/jenkins-pipeline-environment-variables-the-definitive-guide/
                    // - https://stackoverflow.com/a/13245961
                    // - https://stackoverflow.com/a/51991389
                    env.API_VERSION = sh(script: 'grep -Po "(?<=    version=\\").*(?=\\",)" setup.py', returnStdout: true).trim()
                    echo "API: ${env.API_VERSION}"
                    dockerImage = docker.build 'e-learning-by-sse/search-l3s_search-service'
                    docker.withRegistry('https://ghcr.io', 'github-ssejenkins') {
                        dockerImage.push("${env.API_VERSION}")
                        dockerImage.push('latest')
                    }
                }
            }
        }
				
        // Based on: https://medium.com/@mosheezderman/c51581cc783c
        stage('Deploy') {
            steps {
                sshagent(['STM-SSH-DEMO']) {
                    sh "ssh -o StrictHostKeyChecking=no -l ${DEMO_SERVER_USER} ${env.DEMO_SERVER} bash ${REMOTE_UPDATE_SCRIPT}"
                }
            }
        }
		
		stage('Starting Post Build Actions') {
            parallel {

                stage('Deploy') {
                    steps {
                        stagingDeploy env.REMOTE_UPDATE_SCRIPT
                    }
                }
                /*
                stage('Publish Swagger Clients') {
                     options {
                        timeout(time: 200, unit: 'SECONDS')
                    }
                    environment {
                        APP_URL = "http://localhost:9043/l3s-search/swagger.json"
                    }
                    steps {
                        script {
                            sh 'rm -f competence_repository*.zip'
                            docker.image(env.DOCKER_TARGET).withRun("-p 9043:9043") {
                                // Wait for the application to be ready (after container was started)  
                                sleep(time:30, unit:"SECONDS")
                
                                generateSwaggerClient("${env.APP_URL}", "${API_VERSION}", 'search-l3s', "search_service", ['python'])
                            }
                        }
                    }
                }
                */
            }
        }
    }
}
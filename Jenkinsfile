pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                script {
                    if (isUnix()) {
                        // For Unix-based systems
                        sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                        '''
                    } else {
                        // For Windows systems
                        bat '''
                        python -m venv venv
                        venv\\Scripts\\activate
                        pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                script {
                    if (isUnix()) {
                        // For Unix-based systems
                        sh 'python3 -m unittest discover -s .'
                    } else {
                        // For Windows systems
                        bat 'python -m unittest discover -s .'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                script {
                    if (isUnix()) {
                        // For Unix-based systems
                        sh '''
                        mkdir -p ${WORKSPACE}/python-app-deploy
                        cp ${WORKSPACE}/app.py ${WORKSPACE}/python-app-deploy/
                        '''
                    } else {
                        // For Windows systems
                        bat '''
                        mkdir ${WORKSPACE}\\python-app-deploy
                        copy ${WORKSPACE}\\app.py ${WORKSPACE}\\python-app-deploy\\
                        '''
                    }
                }
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running application...'
                script {
                    if (isUnix()) {
                        // For Unix-based systems
                        sh '''
                        nohup python3 ${WORKSPACE}/python-app-deploy/app.py > ${WORKSPACE}/python-app-deploy/app.log 2>&1 &
                        echo $! > ${WORKSPACE}/python-app-deploy/app.pid
                        '''
                    } else {
                        // For Windows systems
                        bat '''
                        start /B python ${WORKSPACE}\\python-app-deploy\\app.py > ${WORKSPACE}\\python-app-deploy\\app.log 2>&1
                        echo %PROCESS_ID% > ${WORKSPACE}\\python-app-deploy\\app.pid
                        '''
                    }
                }
            }
        }

        stage('Test Application') {
            steps {
                echo 'Testing application...'
                script {
                    if (isUnix()) {
                        // For Unix-based systems
                        sh '''
                        python3 ${WORKSPACE}/test_app.py
                        '''
                    } else {
                        // For Windows systems
                        bat 'python ${WORKSPACE}\\test_app.py'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for more details.'
        }
    }
}

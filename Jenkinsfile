pipeline {
    agent any

    environment {
        // Define any necessary environment variables here
        VENV_DIR = "${WORKSPACE}/venv"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                echo 'Checking out code...'
                git 'https://github.com/hjbjbnkjnnkn/jenkinsexample.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                sh '''
                python3 -m venv ${VENV_DIR}
                source ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh '''
                source ${VENV_DIR}/bin/activate
                python3 -m unittest discover -s .
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                mkdir -p ${WORKSPACE}/python-app-deploy
                cp ${WORKSPACE}/app.py ${WORKSPACE}/python-app-deploy/
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running the application...'
                sh '''
                nohup python3 ${WORKSPACE}/python-app-deploy/app.py > ${WORKSPACE}/python-app-deploy/app.log 2>&1 &
                echo $! > ${WORKSPACE}/python-app-deploy/app.pid
                '''
            }
        }

        stage('Test Application') {
            steps {
                echo 'Testing the application...'
                sh '''
                source ${VENV_DIR}/bin/activate
                python3 ${WORKSPACE}/test_app.py
                '''
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


pipeline {
    agent any
    options { disableConcurrentBuilds() }
    parameters {
        string(defaultValue: 'True', description: '"True": initial cleanup: remove container and volumes; otherwise leave empty', name: 'start_clean')
        string(description: '"True": "Set --nocache for docker build; otherwise leave empty', name: 'nocache')
        string(description: '"True": push docker image after build; otherwise leave empty', name: 'pushimage')
        string(description: '"True": keep running after test; otherwise leave empty to delete container and volumes', name: 'keep_running')
    }

    stages {
        stage('Config ') {
            steps {
                sh '''
                   if [[ "$DOCKER_REGISTRY_USER" ]]; then
                        echo "  Docker registry user: $DOCKER_REGISTRY_USER"
                        ./dcshell/update_config.sh dc.yaml.default > docker-compose.yaml
                    else
                        cp docker-compose.yaml.default docker-compose.yaml
                    fi
                    head docker-compose.yaml
                '''
            }
        }
        stage('Cleanup ') {
            when {
                expression { params.$start_clean?.trim() != '' }
            }
            steps {
                sh '''
                    docker-compose down -v 2>/dev/null | true
                '''
            }
        }
        stage('Build') {
            steps {
                sh '''#!/bin/bash
                    [[ "$nocache" ]] && nocacheopt='-c' && echo 'build with option nocache'
                    export MANIFEST_SCOPE='local'
                    export PROJ_HOME='.'
                    ./dcshell/build $nocacheopt
                    echo "=== build completed with rc $?"
                '''
            }
        }
        stage('Push ') {
            when {
                expression { params.pushimage?.trim() != '' }
            }
            steps {
                sh '''
                    default_registry=$(docker info 2> /dev/null |egrep '^Registry' | awk '{print $2}')
                    echo "  Docker default registry: $default_registry"
                    export MANIFEST_SCOPE='local'
                    export PROJ_HOME='.'
                    ./dcshell/build -P
                '''
            }
        }
    }
    post {
        always {
            sh '''
                if [[ "$keep_running" ]]; then
                    echo "Keep container running"
                else
                    echo 'Remove container, volumes'
                    docker-compose rm --force -v 2>/dev/null || true
                    docker rm --force -v shibsp 2>/dev/null || true  # in case docker-compose fails ..
                fi
            '''
        }
    }
}

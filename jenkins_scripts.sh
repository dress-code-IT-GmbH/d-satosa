#!/bin/bash -exv
PS4='+(${BASH_SOURCE}:${LINENO}): ${FUNCNAME[0]:+${FUNCNAME[0]}(): }'

# assure that python env has jeinja2, pytest and pyyaml installed
source /usr/local/virtualenv/d.c/bin/activate

remove_container_if_not_running() {
    local container=$1
    echo 'remove container if no running'
    local status=$(docker container inspect -f '{{.State.Status}}' $container 2>/dev/null || echo '')
    if [[ "$status" ]]; then
        docker container rm -f $container >/dev/null 2>&1 || true # remove any stopped container
    fi
}


remove_containers() {
    echo 'remove containers'
    for cont in $*; do
        local container_found=$(docker container inspect -f '{{.Name}}' $cont 2>/dev/null || true)
        if [[ "$container_found" ]]; then
            docker container rm -f $container_found -v |  perl -pe 'chomp; print " removed\n"'
        fi
    done
}


remove_volumes() {
    echo 'removing volumes'
    for vol in $*; do
        local volume_found=$(docker volume ls --format '{{.Name}}' --filter name=^$vol$)  # fail job on command error
        if [[ "$volume_found" ]]; then
            docker volume rm $vol |  perl -pe 'chomp; print " removed\n"'
        fi
    done
}

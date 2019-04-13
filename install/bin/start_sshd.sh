#!/usr/bin/env bash

main() {
    get_commandline_opts $@
    patch_sshd_config
    create_sshd_keys
    start_sshd
}


get_commandline_opts() {
    daemonmode='-D'
    while getopts ":dh" opt; do
      case $opt in
        d) daemonmode='';;
        *) usage; exit 0;;
      esac
    done
}


usage() {
    echo "usage: $0 [-d] [-h]
       -d  start in background (default: foreground)
       -h  print this help text
       "
}


patch_sshd_config() {
    if [[ ! -e /opt/etc/ssh/sshd_config ]]; then
        mkdir -p /opt/etc/ssh
        cp -p /etc/ssh/sshd_config /opt/etc/ssh/sshd_config
        echo 'GSSAPIAuthentication no' >> /opt/etc/ssh/sshd_config
        echo 'useDNS no' >> /opt/etc/ssh/sshd_config
        sed -i -e 's/#Port 22/Port 2022/' /opt/etc/ssh/sshd_config
        sed -i -e 's/^HostKey \/etc\/ssh\/ssh_host_/HostKey \/opt\/etc\/ssh\/ssh_host_/' /opt/etc/ssh/sshd_config
        #sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /opt/etc/ssh/sshd_config
    fi
}

create_sshd_keys() {
    [[ -e /opt/etc/ssh/ssh_host_rsa_key ]] || ssh-keygen -q -N '' -t rsa -f /opt/etc/ssh/ssh_host_rsa_key
    [[ -e /opt/etc/ssh/ssh_host_ecdsa_key ]] || ssh-keygen -q -N '' -t ecdsa -f /opt/etc/ssh/ssh_host_ecdsa_key
    [[ -e /opt/etc/ssh/ssh_host_ed25519_key ]] || ssh-keygen -q -N '' -t ed25519 -f /opt/etc/ssh/ssh_host_ed25519_key
}


start_sshd() {
    echo 'starting sshd'
    /usr/sbin/sshd ${daemonmode} -f /opt/etc/ssh/sshd_config
    # login like 'ssh -o "StrictHostKeyChecking no" -i ~/.ssh/id_ed25519_loopback -p 2022 <someuser>@thishost'
}


main "$@"

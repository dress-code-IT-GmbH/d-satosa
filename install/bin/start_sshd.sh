#!/bin/bash

[[ -f '/etc/ssh/ssh_host_ed25519_key' ]] || ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key
/usr/sbin/sshd
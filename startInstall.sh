#!/bin/bash

ansible-playbook -b -u volumio -i RadioRaspi, ansible_install.yml --extra-vars "ansible_sudo_pass=volumio"
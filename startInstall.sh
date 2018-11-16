#!/bin/bash

ansible-playbook -b -u volumio -i RadioRaspi, ansible_install.yml --ask-sudo-pass
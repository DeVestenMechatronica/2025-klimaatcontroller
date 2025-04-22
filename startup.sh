#!/bin/bash 

#   startup.sh
#   Dit script start ons Python programma. Dit script wordt
#   gebruikt door de systemd service

# We starten de virual environment voor Python
source /home/mechatronica/klimaatcontroller/venv/bin/activate
# We starten ons Python programma
python /home/mechatronica/klimaatcontroller/project.py
#!/bin/bash
source .env/bin/activate
python infosec_board.py > infosec_board.log
deactivate

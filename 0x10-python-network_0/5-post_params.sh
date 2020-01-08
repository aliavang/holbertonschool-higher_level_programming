#!/bin/bash
#Send POST request and display body of response
curl -sX "POST" -F "email=hr@holbertonschool.com"
-F "subject=I will always be here for PLD" $1

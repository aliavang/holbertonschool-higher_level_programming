#!/bin/bash
#Display all accepetd HTTP methods
curl -siX "OPTIONS" $1 | grep Allow: | cut --complement -d ' ' -f 1

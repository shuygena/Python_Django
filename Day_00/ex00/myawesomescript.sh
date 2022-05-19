#!/bin/sh

curl -sI $1 | grep -i "Location:" | cut -f2 -d ' '
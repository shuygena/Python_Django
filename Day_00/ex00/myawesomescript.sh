#!/bin/sh

curl -s $1 | grep "href=" | cut -f2 -d '"'
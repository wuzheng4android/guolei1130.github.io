#!/bin/bash


hexo new $1
chmod a+x ./insert.py
./insert.py $1
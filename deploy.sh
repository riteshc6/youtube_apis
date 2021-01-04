#! /bin/bash

set -e
set -x

echo "*********************** pull latest code from master branch ***********************"
sudo git pull --rebase origin master

sudo docker build -t "youtube_apis:development-build" .
sudo docker rm -f $(sudo docker ps -a -q) || true           # To prevent error code in case there is no container
sudo docker run -t -d -p 8000:8000 -p 9200:9200 -p 9300:9300 "youtube_apis:development-build"
sudo docker system prune -f
sleep 10
sudo docker ps
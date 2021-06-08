#!/bin/sh
docker stop amphora-wiki
docker rm amphora-wiki
docker build . -t tiyn/amphora-wiki
docker run --name amphora-wiki \
    --restart unless-stopped \
    -p "5000:5000" \
    -e FLASK_ENV=development \
    -d tiyn/amphora-wiki

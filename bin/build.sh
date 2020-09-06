#! /bin/bash
# Build a docker image
cd ..
docker build -t pyengine/server-mockup .
docker tag pyengine/server-mockup pyengine/server-mockup:1.0

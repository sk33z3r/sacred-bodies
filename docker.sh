#!/usr/bin/env bash

docker build --tag sacred-bodies .
docker run -it --rm --name sacred-bodies -v $PWD:/sacred-bodies:rw sacred-bodies
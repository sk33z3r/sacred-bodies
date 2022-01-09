#!/usr/bin/env bash

container="sacred-node"

case $1 in
    build) docker build -t $container .;;
    run) docker run -it --name $container -v $PWD:/sacred-nft -w /sacred-nft $container;;
    attach) docker exec -it $container bash;;
    remove) docker rm -f $container;;
    *) echo "Invalid command, expecting [build|run|attach|remove]"; exit 1;;
esac

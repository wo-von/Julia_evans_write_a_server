#!/usr/bin/bash
set e
for i in `seq 1 150`
do 
    curl localhost:8080 &
done
wait
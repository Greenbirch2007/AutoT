#!/bin/bash
step=10
for (( i = 0; i < 60; i = (i+step) )); do
    /usr/local/bin/python3.6 /root/SP500_.py
    sleep $step
done

exit 0
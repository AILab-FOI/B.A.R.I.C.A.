#!/bin/bash

# Function to start screen sessions
start_sessions() {
    for dir in $(find . -maxdepth 1 -type d)
    do
        if [ "$dir" != "." ]
        then
            cd $dir
            session_name=$(basename $dir)
            echo "Starting session $session_name"
            screen -d -m -S $session_name python3 wss.py
            cd ..
        fi
    done
}

# Function to stop screen sessions
stop_sessions() {
    for dir in $(find . -maxdepth 1 -type d)
    do
        if [ "$dir" != "." ]
        then
            session_name=$(basename $dir)
            echo "Stopping session $session_name"
            screen -X -S $session_name quit
        fi
    done
}

# Check the argument
if [ "$1" == "start" ]
then
    start_sessions
elif [ "$1" == "stop" ]
then
    stop_sessions
else
    echo "Invalid argument. Please use start or stop."
fi


#!/bin/bash

IPMI=$1

qdbus $KONSOLE_DBUS_SERVICE $KONSOLE_DBUS_SESSION setTitle 1 ${DEST}

while true
do
    ipmitool -I lanplus -H ${IPMI} -U root -P strato sol deactivate instance=3 
    sleep 1
    for i in {1..10}
    do
        ipmitool -I lanplus -H ${IPMI} -U root -P strato sol activate instance=3
            if [ $? -eq 0 ]; then
                exit 0
            fi
        sleep 1
    done
done

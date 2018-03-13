#!/bin/bash

i=1;
while [ $i -le $1 ];
do
echo $i; i=$((i+1));
done

xte 'key Return'
xte 'usleep 100000'
xte 'key Return'
xte 'usleep 100000'
xte 'key Up'
xte 'usleep 100000'
xte 'key Up'
xte 'usleep 100000'
xte 'key Return'
xte 'usleep 100000'
xte 'key Down'
xte 'usleep 100000'
xte 'key Return'
xte 'usleep 100000'

i=1;
while [ $i -le $1 ];
do
xte 'key Right'
xte 'usleep 100000'
i=$((i+1));
done

xte 'key Return'
xte 'usleep 100000'
xte 'key Return'
xte 'usleep 100000'
xte 'key Return'
xte 'key Up'
xte 'usleep 100000'
xte 'key Return'
xte 'usleep 100000'
#!/bin/bash
echo "Current User:$USER"
echo "IP:$(ifconfig ens33 |grep 'inet addr'|awk -F ":" '{print $2}'|awk '{print $1}')"
echo "Kernel:`uname -r`"
echo "Hostname:$HOSTNAME"
echo "Current Time:`date +'%Y-%m-%d %H:%M:%S'` "
os=`/usr/bin/lsb_release -a |grep "Des"|sed 's@^.*on:@@g'`
echo "Host OS:`echo $os`"
cpu=`/bin/cat /proc/cpuinfo|grep "name"|uniq -c|sed 's@^.*:@@g'`
echo "CPU:`echo $cpu`"

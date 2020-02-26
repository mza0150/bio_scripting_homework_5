#!/bin/bash

# This script will invoke current time  and date, a list of all logged-in users id and the system uptime.
date_var=`date|cut -d " " -f1-3,4|awk '{print "Current Time is: " $4 "--------------------" " and Todays Date is: " $2,$1,$3}'`
echo ${date_var} > time_date_logged_id_uptime.log

echo "*******************************" >> time_date_logged_id_uptime.log

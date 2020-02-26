#!/bin/bash

# This script will invoke current time  and date, a list of all logged-in users id and the system uptime.
echo >> time_date_logged_id_uptime.log
echo >> time_date_logged_id_uptime.log
date_var=`date|cut -d " " -f1-3,4|awk '{print "Current Time is: " $4 "--------------------" " and Todays Date is: " $2,$1,$3}'`
echo ${date_var} >> time_date_logged_id_uptime.log
echo >> time_date_logged_id_uptime.log
echo >> time_date_logged_id_uptime.log
echo "*******************************" >> time_date_logged_id_uptime.log
# Find logged-in user-ID:
logged_user=`who | cut -d' ' -f1 | sort | uniq`

echo "Currently logged users name:" >> time_date_logged_id_uptime.log
echo  "$logged_user " >> time_date_logged_id_uptime.log
echo >> time_date_logged_id_uptime.log
echo >> time_date_logged_id_uptime.log
#Get system uptime info:
system_uptime=`uptime`

echo "******************************" >> time_date_logged_id_uptime.log
echo >> time_date_logged_id_uptime.log
echo >> time_date_logged_id_uptime.log
echo "System Uptime: $system_uptime" >>  time_date_logged_id_uptime.log
echo >>  time_date_logged_id_uptime.log
echo >>  time_date_logged_id_uptime.log
echo "******************************" >>  time_date_logged_id_uptime.log


#!/bin/bash
# Add this to crontab
# @reboot sudo /root/TempLogger/RunTempLogger.sh
# chmod +x RunTempLogger.sh
while true
do
 python3 /root/TempLogger/TempLogger.py
 # Change this to change the interval between temperature readings, currently set to 5 seconds
 sleep 5
done

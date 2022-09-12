#!/bin/bash

#!/bash/python3

echo -e "checking if container is up and working\n"
sleep 2
thisIP=`hostname -I|awk '{print $1}'`
echo -e $thisIP
telnet $thisIP 49153
#os.system('telnet 192.168.68.110 49153'


#!/bin/bash
# echappement ^ $ \ | { } [ ] ( ) ? # ! + * .

#pour la date : \[\d{6}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]
REGEX_DATE = \[\d{6}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]

#minium 3 de taille ?
REGEX_PROTOCOL = \S+

REGEX_IP = ([0-9]{1,3}\.){3}[0-9]{1,3}

REGEX_PORT = [0-9]{1,5}

REGEX_MESSAGE = .*\n

MESSAGE = "Connection to server" 

tab-rule = ($REGEX_DATE \s+ $REGEX_PROTOCOL \s+ $REGEX_PROTOCOL \s+ $REGEX_IP \s+ $REGEX_IP \s+ $REGEX_PORT \s+ $REGEX_PORT \s+ $MESSAGE )


for i in ${tab-rule[@]}; 
do

 sudo echo ${tab-rule[i]} >> /etc/logcheck/ignore.d.server/local-rule ;

done





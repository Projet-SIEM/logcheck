#!/bin/bash
# echappement ^ $ \ | { } [ ] ( ) ? # ! + * .

#pour la date
REGEX_DATE="\[[0-9]{4}-[0-9]{2}-[0-9]{2}\s[0-9]{2}:[0-9]{2}:[0-9]{2}\]"

#minium 3 de taille ?
REGEX_PROTOCOL="\S+"

REGEX_IP="([0-9]{1,3}\.){3}[0-9]{1,3}"

REGEX_PORT="[0-9]{1,5}"

REGEX_MESSAGE=".*\n"

REGEX_ESPACE="(\s)+"

MESSAGE="Connection to server" 

RULE=$REGEX_DATE $REGEX_ESPACE $REGEX_PROTOCOL $REGEX_ESPACE $REGEX_PROTOCOL $REGEX_ESPACE $REGEX_IP $REGEX_ESPACE $REGEX_IP $REGEX_ESPACE $REGEX_PORT $REGEX_ESPACE $REGEX_PORT $REGEX_ESPACE $MESSAGE

sudo echo $RULE >> /etc/logcheck/ignore.d.server/local-rule ;

#for i in ${TAB[@]}; 
#do

#sudo echo ${TAB[i]} >> /etc/logcheck/ignore.d.server/local-rule ;

#done





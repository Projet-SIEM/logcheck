#!/bin/bash
# echappement ^ $ \ | { } [ ] ( ) ? # ! + * .

#pour la date : \[\d{6}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]
regex_date = \[\d{6}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]

#minium 3 de taille ?
regex_protocol = \S+

regex_ip = ([0-9]{1,3}\.){3}[0-9]{1,3}

regex_port = [0-9]{1,5}

regex_message = .*\n

message = "Connection to server" 

tab-rule = (regex_date \s+ regex_protocol \s+ regex_ip \s+ regex_ip \s+ regex_port \s+ regex_port \s+ message )


for i in ${tab-rule[@]}; 
do

 sudo echo ${tab-rule[i]} >> /etc/logcheck/ignore.d.server/local-rule ;

done





#!/bin/bash

#sauvegarder les fichier de configuration
sudo cp /etc/logcheck/logcheck.conf{,.ori};
sudo cp /etc/logcheck/logcheck.logfiles{,.ori};

#modification du fichier de configuration
command /bin/sed -i -r 's|^SENDMAILTO=.*$|SENDMAILTO="mann.dcl@yahoo.com"|' /etc/logcheck/logcheck.conf


#ajout des fichiers de logs a analyser
sudo echo /home/vagrant/Malilog/Logs/logs.log >> /etc/logcheck/logcheck.logfiles

#Pour lancer directement logcheck
#sudo -u logcheck logcheck
#egrep -f /etc/logcheck/ignore.d.server/local-rules /home/vagrant/Malilog/Logs/logs.log

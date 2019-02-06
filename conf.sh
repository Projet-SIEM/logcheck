#!/bin/bash

#sauvegarder les fichier de configuration
sudo cp /etc/logcheck/logcheck.conf{,.ori};
sudo cp /etc/logcheck/logcheck.logfiles{,.ori};

#modification du fichier de configuration
command /bin/sed -i -r 's|^SENDMAILTO=.*$|SENDMAILTO="mann.dcl@yahoo.com"|' /etc/logcheck/logcheck.conf


#ajout des fichiers de logs a analyser
sudo echo le-chemin-du-fichier-de-generation-du-fichier-de-log-de-alexis >> /etc/logcheck/logcheck.logfiles



#!/usr/bin/env python3
import argparse

# TODO: inclusif

espace = "\s"

def date(annee,mois,jour,heure,minutes,secondes):
    return "\["+annee+"-"+mois+"-"+jour+espace+heure+"-"+minutes+"-"+secondes+"\]"

def protocol(nom="\S+"):
    return nom

def addresse_ip(solt1 = "[0-9]{1,3}",solt2 = "[0-9]{1,3}",solt3 = "[0-9]{1,3}"):
    return solt1+"\."+solt2+"\."+solt3

def port(p = "[0-9]{1,5}"):
    return p

def message(m = ".*"):
    return m + "\n"



def main():#TODO: faire les fichier+ binaire ou tout type de fichier
    parser = argparse.ArgumentParser()
    date = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('--annee','-a',dest="annee",action='store',default="[0-9]{4}", help="annee cibler")
    parser.add_argument('--mois','-mo',dest="mois",action='store', default="[0-9]{2}", help="mois cibler")
    parser.add_argument('--jour','-j',dest="jour",action='store', default="[0-9]{2}", help="jour cibler")
    parser.add_argument('--heure','-h',dest="heure",action='store', default="[0-9]{2}", help="heure cibler")
    parser.add_argument('--minutes','-mi',dest="minutes",action='store', default="[0-9]{2}", help="minutes cibler")
    parser.add_argument('--secondes','-s',dest="secondes",action='store', default="[0-9]{2}", help="secondes cibler")

    parser.add_argument('--protocolCouche3','-pc3',dest="protocolCouche3", default="\S+",action='store', help="protocol de la couche 3 a cibler")
    parser.add_argument('--protocolCouche4','-pc4',dest="protocolCouche4", default="\S+", action='store', help="protocol de la couche 4 a cibler")

    parser.add_argument('--addrIPSource','-ipS',dest="IPSource",action='store', default="[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}", help="IP source a cibler")
    parser.add_argument('--addrIPDestination','-ipD',dest="IPDest",action='store', default="[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}", help="IP destination a cibler")

    parser.add_argument('--portSource','-pS',dest="portSource",action='store', default="[0-9]{1,5}" help="port source a cibler")
    parser.add_argument('--portDestination','-pD',dest="portDest",action='store', default="[0-9]{1,5}" help="port destination a cibler")

    parser.add_argument('--message','-m',dest="mess",action='store',default=".*" help="Le message a cibler")

    args = parser.parse_args()

#ip parser

    tabIPS = IPSource.split('.')
    tabIPD = IPDest.split('.')


    rule = date(annee,mois,jour,heure,minutes,secondes)+ espace+"+"\
    +protocol(protocolCouche3)+ espace+"+"+protocol(protocolCouche4)+ espace+"+"\
    +addresse_ip(tabIPS[0],tabIPS[1],tabIPS[2])+ espace+"+"\
    +addresse_ip(tabIPD[0],tabIPD[1],tabIPD[2])+ espace+"+"\
    +port(portSource)+ espace+"+"+port(portDest)+ espace+"+"\
    +message(mess)

#TODO: verifier si la regle nest pas deja presente
    with open("/etc/logcheck/ignore.d.server/local-rule", "a") as f:
        f.write(rules)

    print("Nouvelle regles ecrite:")
    print(rule)

if __name__ == "__main__" :
    main()
#

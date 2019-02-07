#!/usr/bin/env python3

# TODO: inclusif

espace = "\s"

def date(annee = "[0-9]{4}",mois = "[0-9]{2}",jour = "[0-9]{2}",heure = "[0-9]{2}",minutes = "[0-9]{2}",secondes = "[0-9]{2}"):
    return "\["+annee+"-"+mois+"-"+jour+espace+heure+"-"+minutes+"-"+secondes+"\]"

def protocol(nom="\S+"):
    return nom

def addresse_ip(solt1 = "[0-9]{1,3}",solt2 = "[0-9]{1,3}",solt3 = "[0-9]{1,3}"):
    return solt1+"\."+solt2+"\."+solt3

def port(p = [0-9]{1,5}):
    return p

def message(m = ".*"):
    return m + "\n"



def main():#TODO: faire les fichier+ binaire ou tout type de fichier
    parser = argparse.ArgumentParser()
    date = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('--annee','-a',dest="annee",action='store', help="annee cibler")
    parser.add_argument('--mois','-mo',dest="mois",action='store', help="mois cibler")
    parser.add_argument('--jour','-j',dest="jour",action='store', help="jour cibler")
    parser.add_argument('--heure','-h',dest="heure",action='store', help="heure cibler")
    parser.add_argument('--minutes','-mi',dest="minutes",action='store', help="minutes cibler")
    parser.add_argument('--secondes','-s',dest="secondes",action='store', help="secondes cibler")

    parser.add_argument('--protocolCouche2','-pc2',dest="protocolCouche2",action='store', help="protocol de la couche 2 a cibler")
    parser.add_argument('--protocolCouche3','-pc3',dest="protocolCouche3",action='store', help="protocol de la couche 3 a cibler")

    parser.add_argument('--addrIPSource','-ipS',dest="IPSource",action='store', help="IP source a cibler")
    parser.add_argument('--addrIPDestination','-ipD',dest="IPDest",action='store', help="IP destination a cibler")

    parser.add_argument('--portSource','-pS',dest="portSource",action='store', help="port source a cibler")
    parser.add_argument('--portDestination','-pD',dest="portDest",action='store', help="port destination a cibler")

    parser.add_argument('--message','-m',dest="message",action='store', help="Le message a cibler")

    args = parser.parse_args()












if __name__ == "__main__" :
    main()
#

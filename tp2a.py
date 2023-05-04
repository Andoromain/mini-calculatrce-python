import os


cmd_status = 'C:\wamp\bin\apache\Apache2.4.4\bin\httpd -v'
cmd_restart = 'C:\wamp\bin\apache\Apache2.4.4\bin\httpd -k restart'
def checkApache():
    """ surveille l'Ètat du daemon Apache """
    status = os.popen(cmd_status).readlines()
     # recupere la deuxieme ligne et retire le saut de ligne
    stat=status[1].strip()
    print(stat)
    print(status)
    if stat ==  'Apache is *not* running.':
        # Tests sur le systeme
        # Apache doitetre relance
        os.popen(cmd_restart).read()
        status = os.popen(cmd_status).readlines()
        stat=status[1].strip()
        if stat == 'Apache is running.':
            print ('Apache relance avec succes')
        else:
            print ('Impossible de relancer Apache')
    else:
        print( '…tat OK : %s' % stat)
checkApache()

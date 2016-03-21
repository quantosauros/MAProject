'''
Created on 2016. 3. 18.

@author: jayjl
'''
from yahoo.session import Session

if __name__ == '__main__':
    y = Session('jihoonjaylee', 'dunk24ce', daemonic=True)
    y.connect()
    
    import time
    while 1:
        if y.logged:
            print "logged"
            y.send_msg(raw_input('who:'),raw_input('text:'))
        else :
            print "not logged"
        time.sleep(0.5)
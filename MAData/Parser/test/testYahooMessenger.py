import time
import pprint
import yahoo
from yahoo.session import Session, clear_tags
from yahoo.consts import *


class YahooClient(Session):
    def on_unknown_packet(self, p):
        print "Recieved unknown packet - svc id: 0x%X(%d)" % (p.svc,p.svc)
        #print repr(p)
        #if p.svc == 15:
        #    print repr(p)
    def on_message_packet(self, src, dst, msg):
        print "From <%s>: %s" % (src, clear_tags(msg))
    def on_notify_packet(self, src, msg, p):
        print "%s: %s." % (src,msg)
    def on_disconnect(self,err):
        if err == LOGIN_DUPL:
            print "Disconnected due to duplicate login."
        else:
            print "Disconnected for unkown reason."
        time.sleep(2)
        print "Reconnecting..."
        self.connect()
    def on_login(self):
        print "Contacts: ",
        pprint.pprint(self.contact_dict, indent=4)
        self.set_status('Powered by: %s ! http://ionel.zapto.org/browser/ym' % yahoo.__version__)
        #t.set_status(type='BRB')
        #
        #t.send_pk(SERVICE_ADDBUDDYVALIDATE, ['0',t.login_id])
        #t.send_pk(SERVICE_BUDDYREQ, ['1',t.login_id,'4','ionel_mc','13','2','14','wha'])
        time.sleep(1)
        print 'BAM'
        #t.send_pk(0x86, ['1',t.login_id,'7','ionel_mc','13','2','14','muie'], 0)
        #t.send_pk(SERVICE_ADDBUDDYVALIDATE, ['0',t.login_id],1)
        self.deny_add_req_ex('ionel_mc', 'aaaaaaaaaaaa')
        #t.rem_contact('ionel_mc','test')

        #t.rem_contact('cristian2104','test')
        #t.deny_add_req('cristian2104', '')
        for g in self.contact_dict.keys():
            print 'g:',g
            for c in self.contact_dict[g]:
                print 'c:',c
                self.rem_contact(c,g)
                time.sleep(1)
    def on_login_fail(self,err):
        print "Failed to login because:",
        if err == LOGIN_UNAME:
            print 'invalid username.'
        elif err == LOGIN_PASSWD:
            print 'bad password.'
        elif err == LOGIN_LOCK:
            print 'account locked.'
        else:
            print 'unkown reason.'
    def on_connect(self):
        if self.worker:
            print "Daemonic worker:",self.worker.isDaemon() 
    def on_status_change(self, name, status, details):
        print "%s - %s %s" % (name, status, details)
    def on_rem_contact_req(self, src, who, where):
        print "Request to remove contact '%s' from '%s'." % (who,where)
    def on_add_contact_req(self, who, msg):
        print "%s requested a buddy add. He said: '%s'" % (who,msg)
        if msg == "please":
            print "Approving (he said 'please')."
            #t.deny_add_req(who, 'Please is not enough !')
            #t.deny_add_req_ex(who, 'Please is not enough !')
            self.approve_add_req(who)
            self.add_contact(who, 'test')
        else:
            print "Denying the bastard."
            self.deny_add_req(who, 'Say please fucker !')
    def on_add_contact_deny(self, who, reason):
        print "%s denied my buddy add request because: '%s'." % (who,reason)
    def on_add_contact_approval(self, who):
        print "%s approved my add request." % who


if __name__ == '__main__':
    y = YahooClient('jihoonjaylee', 'dunk24ce', daemonic=True)
    y.connect()
    import time
    while 1:
        if y.logged:
            y.send_msg(raw_input('who:'),raw_input('text:'))
        time.sleep(0.5)
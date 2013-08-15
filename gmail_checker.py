#Should hopefully retrieve the number of emails in my inbox from gmail, then show me the info from each one.
import imaplib, sys

def setup():
	# Check to see if the user has provided 2
	#command line arguments which are not blank
	if len(sys.argv) == 1:
		print "You do not appear to have correctly called this function"
		print "USAGE: Command, username, password"
		sys.exit("Incorrect Usage")
		
	if sys.argv[1] != "":
                #print "Assigning Usernme"
		username = sys.argv[1]
	if sys.argv[2] != "":
                #print "Assiging Password"
		password = sys.argv[2]
	else:
		print "You do not appear to have correctly called this function"
		print "USAGE: Command, username, password"
		sys.exit("Incorrect Usage")
				
	client = 'imap.gmail.com'
	client_port = 993
		
	gmailpy = imaplib.IMAP4_SSL(client, client_port)
	gmailpy.login(username, password)
	new_main(gmailpy)
	

def new_main(server):
	#Search for unread messages
	server.select('Inbox', 'True')
        msgs = server.search (None, "(UNSEEN)")[1][0]
        msg_count = len(msgs.split(' '))
        a = ""
        for i in msgs.split(' '):
                a = a + i + ","
        a = a[0:(len(a)-1)]
        messages = server.fetch (a, '(body[header.fields (from to subject)])')
        
	
        #Initialise
        if msg_count > 1:
                print 'You have %d New Messages' % (msg_count)
                print '==========================='
        elif msg_count == 1:
                print 'You have 1 New Message'
                print '==========================='
        elif msg_count == 0:
                print 'You have No New Messages'
                print '==========================='
        msg_store = []
	for i in messages[1]:
                if len(i) != 1:
                        for a in range(0, 3):
                                msg_store.append(i[1].split('\n')[a].rstrip())
                                #print i[1].split('\n')[a].rstrip()
                        mess = ["","",""]
                        for a in msg_store:
                                if a[0:3]  == "To:":
                                        #print "DEBUG: a = %s" % (a)
                                        mess[0] = a
                                if a[0:4]  == "From":
                                        #print "DEBUG: a = %s" % (a)
                                        mess[1] = a
                                if a[0:8] == "Subject:":
                                        mess[2] = a
                                        #print "DEBUG: a = %s" % (a)
                        for a in mess:
                                print a
                        print '------------------------------------------------------------------------'
                        msg_store = []
                        
	server.close()
	server.logout()
	

if __name__ == "__main__":
        setup()

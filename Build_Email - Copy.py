import smtplib
#print('Enter your email: ')
#received_email = input().split(' ')

gmail_user = 'rig email here'
gmail_password = 'a password'

sent_from = gmail_user
#to = received_email
to = 'your email here'
subject = 'Canary Warning!'
body = 'The miner has restarted'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:
    print('Something went wrong...')

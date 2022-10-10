import smtplib, ssl, csv

##OPEN SERVER W/ CREDENTIALS -------------------------

port = 465  
smtp_server = "smtp.gmail.com"
sender_email = input("Enter your email: ") 
sender_alias = input("Optional - input alias: ")
password = input("Enter password: ")
contacts_list = input("Input contacts list file: ")
messagefile = input("Input message file: ")
cc_email = input("Optional - Input cc: ")
with open(messagefile) as file:
    message = file.read()


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)

    #READ SENDEE EMAIL AND NAME -----------------
    with open(contacts_list) as file:
        reader = csv.reader(file)
        next(reader) #skip header line
        for row in reader:
            name = row[0] #extract name from csv, rest is emails
            row.pop(0)
            for email in row:
                if email != '': #for each email provided, replace {name} with name and send email
                    #CUSTOMIZE MESSAGE AND SEND-------------
                    #optional alias
                    if sender_alias != '':
                        finalmessage = "From:" + sender_alias + "\n"
                        print(finalmessage)
                    else:
                        finalmessage = "From:" + sender_email + "\n"
                    #to:
                    finalmessage = finalmessage + "TO: " + email + "\n"
                    #optional cc:
                    if cc_email != '':
                        finalmessage = finalmessage + "CC:" + cc_email + "\n"
                        email = email + "," + cc_email
                        print(email)
                    #message content
                    finalmessage = finalmessage + message.format(name = name)
                    server.sendmail(sender_email, email, finalmessage) 

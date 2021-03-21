#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wikipedia
import wikipediaapi
import schedule
import time
import smtplib, ssl


#Initialize wikipedia api
wiki_reader = wikipediaapi.Wikipedia('en')

#Clear any jobs in the scheduler
schedule.clear()

#MUST TURN ON LESS SECURE APPS FOR SCRIPT TO WORK
def make_me_smarter():
    
    #Random Wikipedia Article and Contnet:
    article_title = wikipedia.random(1)
    content = wiki_reader.page(article_title).text
    
    #Encode the messages so that they can be emailed (many email providers REQUIRE this)
    
    #Replace non-ascii character with a ?
    encoded_article_title = article_title.encode('ascii','replace').decode('utf-8')

    
    #Must be written like this for proper email formatting. Otherwise, it'll be a byte stream
    encoded_content = content.encode('ascii','replace').decode('utf-8')
    
    
    #Email portion
    email = open(r'your email here').read()
    password=open(r'your password here').read()
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = email  # Enter your address
    receiver_email = email  # Enter receiver address
    

    subject = "Time to read about: {}".format(encoded_article_title)
    
    email_body = encoded_content
    
    message = 'Subject: {}\n\n{}'.format(subject,email_body)
    
    
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(email, password)
        server.sendmail(sender_email, receiver_email, message)

schedule.every(10).seconds.do(make_me_smarter)

while True:
    schedule.run_pending()
    time.sleep(1)

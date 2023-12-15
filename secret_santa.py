#! /usr/bin/python3

import random
import smtplib, ssl


port = 465  # For SSL
smtp_server = "smtp.gmail.com"

participants = {"p1" : "p1@gmail.com",
                "p2" : "p2@gmail.com",
                "p3" : "p3@gmail.com",
                "p4": "p4@gmail.com"}

turn = [p for p in participants]
match = [p for p in participants]

secret_santa = {}

for i in range(len(participants)):
    random.shuffle(turn)
    turn_p = turn[-1]

    random.shuffle(match)
    match_p = match[-1]
    while turn_p == match_p:
        random.shuffle(match)
        match_p = match[-1]

    turn.pop()
    match.pop()
    secret_santa[turn_p] = match_p

# Set the app password in your Google account
# For instructions refer https://support.google.com/accounts/answer/185833?hl=en
app_password = ""

for p in secret_santa:
    sender_email = "p1@gmail.com"
    receiver_email = participants[p]
    message = f"""\
Subject: Secret Santa

You are secret santa for {secret_santa[p]}."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message)
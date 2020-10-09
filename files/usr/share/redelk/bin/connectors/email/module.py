#!/usr/bin/python3
#
# Part of RedELK
# Script to check if there are alarms to be sent
#
# Author: Outflank B.V. / Mark Bergman / @xychix
# Contributor: Lorenzo Bernardi / @fastlorenzo
#
import config
import socket
import json
import argparse
import csv
import hashlib
import requests
import smtplib
import os
import shutil
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formatdate
from email.header import Header
from email.utils import formataddr
from email.mime.text import MIMEText
from modules.helpers import *
from subprocess import Popen, PIPE
from time import sleep

info = {
    'version': 0.1,
    'name': 'email connector',
    'description': 'This connector sends RedELK alerts via email',
    'type': 'redelk_connector',
    'submodule': 'email'
}

class Module():
    def __init__(self):
        #print("class init")
        pass

    def SendMail(to, mail, subject, fromaddr=config.fromAddr, attachment="None", smtpSrv=config.smtpSrv, smtpPort=config.smtpPort, smtpName=config.smtpName, smtpPass=config.smtpPass):
        msg = MIMEMultipart()
        # Read html File
        html = mail
        msg['Subject'] = subject
        msg['From'] = formataddr((str(Header(fromaddr, 'utf-8')), fromaddr))
        msg['To'] = ", ".join(to)
        msg['Date'] = formatdate()
        # DONE PREPARATION, BUILD MAIL
        msg.attach(MIMEText(html, 'html'))
        if attachment != "None":
            msg = self.Attach(msg, attachment)
        # Sending the stuff
        s = smtplib.SMTP(smtpSrv, int(smtpPort))
        s.starttls()
        s.login(smtpName, smtpPass)
        resp = s.sendmail(fromaddr, to, msg.as_string())
        print("smtpd response: %s" % (resp))
        s.close()


    def Attach(msg, filename):
        with open(filename, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=filename
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % filename
            msg.attach(part)
        return msg

    def send_alarm(alarm):
        fontsize = 13
        mail = """
                <html><head><style type="text/css">
                #normal {
                    font-family: Tahoma, Geneva, sans-serif;
                    font-size: 16px;
                    line-height: 24px;
                }
                </style>
                </head><body>
            """
        subjectPostPend = ""
        # print(a.checkDict)
        try:
            for k, v in alarm.checkDict.items():
                for item, itemData in v['results'].items():
                    mail = mail + \
                        "<p style=\"font-size:%spx\">Alarm on item %s while \"%s\"</p>\n" % (fontsize, item, v['name'])
                    mail = mail + "<p style=\"color:#770000; font-size:%spx\">%s</p>\n" % (fontsize - 3, pprint(itemData))
                    mail = mail + "<table>"
                    for itemDataK, ItemDataV in itemData.items():
                        mail = mail + "<tr><td style=\"font-size:%spx\">%s</td<><td style=\"font-size:%spx\">%s</td></tr>" % (
                            fontsize - 3, itemDataK, fontsize - 3, ItemDataV)
                    mail = mail + "</table>"
                    subjectPostPend = " | %s" % v['name']
        except Exception as e:
            print('Error sending email: %s' % e)
            pass
        mail = mail + "</body></html>\n"
        smtpResp = self.SendMail(config.toAddrs, mail, "Alarm from %s %s" % (socket.gethostname(), subjectPostPend))

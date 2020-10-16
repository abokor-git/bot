import time
import os
import csv
import requests
from bs4 import BeautifulSoup
import smtplib

materiels = ["https://www.topachat.com/pages/detail2_cat_est_micro_puis_rubrique_est_wpr_puis_ref_est_in20001237.html",
            "https://www.topachat.com/pages/detail2_cat_est_micro_puis_rubrique_est_w_cm_am4_puis_ref_est_in11018054.html",
            "https://www.topachat.com/pages/detail2_cat_est_micro_puis_rubrique_est_wme_ddr4_puis_ref_est_in11013478.html",
            "https://www.topachat.com/pages/detail2_cat_est_micro_puis_rubrique_est_wgfx_pcie_puis_ref_est_in11020134.html",
            "https://www.topachat.com/pages/detail2_cat_est_micro_puis_rubrique_est_w_ssd_puis_ref_est_in10109954.html",
            "https://www.topachat.com/pages/detail2_cat_est_micro_puis_rubrique_est_w_boi_sa_puis_ref_est_in20000240.html",
            "https://www.topachat.com/pages/detail2_cat_est_micro_puis_rubrique_est_w_ali_puis_ref_est_in10102958.html",
            ]

nexttime = True

def email():
    
    # Set Global Variables
    gmail_user = 'bot.system.mail@gmail.com'
    gmail_password = 'Mail.gmail.bot'
    # Create Email 
    mail_from = 'BOT TOP-ACHAT'
    mail_to = 'abokor.ahmed.kadar@outlook.com'
    mail_subject = 'Hello'
    mail_message_body = 'Tout tes articles sont disponiblee !!!'

    mail_message = '''\
    From: %s
    To: %s
    Subject: %s
    %s
    ''' % (mail_from, mail_to, mail_subject, mail_message_body)
    # Sent Email
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(gmail_user, gmail_password)
    server.sendmail(mail_from, mail_to, mail_message)
    server.close()
    
def verification():
    
    c = 0
    
    for i in materiels:
        
        requete = requests.get(i)
        page = requete.content
        soup = BeautifulSoup(page)
        stock = soup.find("span", {"class": "availability-mobile__sticker"})

        if stock.string == "En stock":
            c = c + 1
    
    return c

while nexttime==True:
    
    count = verification()
        
    if count == 7:
        email()
        break
    else:
        print("Pas encore")
        
    time.sleep(5)
    

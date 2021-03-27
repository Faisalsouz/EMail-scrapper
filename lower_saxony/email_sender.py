import pandas as pd
E_mails=pd.read_csv(r"D:\OneDrive - uos.de\OneDrive - uni-osnabrueck.de\UTP\Restau\Promotional Stuff\E-mail_list\to_be_sent02.csv").Email
count=0
for i in E_mails:
    print(i)
# import os
    import smtplib
    #import imghdr
    from email.message import EmailMessage

    EMAIL_ADDRESS = 'fkhalil@ur-techpartner.de'#os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD ='Souz3700))' #os.environ.get('EMAIL_PASS')

    #contacts = ['fkhalil@uni-osnabrueck.de', 'test@example.com','parihumagain@gmail.com','happyhailian@gmail.com']
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Ihr eigenes Online-Bestellsystem mit 0% Provision 0€ monatliche Gebühren.'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = i

        #msg.set_content('This is a plain text email only be shown when html is disabled.')

        msg.add_alternative("""\
        <p><span style="font-size: 13pt; font-family: Bell MT">
        Sehr geehrte damen und herren,<br>Hat die Corona-Krise Ihr Geschäft schwer getroffen?<br>Haben
        Sie Angst, zu viel Geld in Form einer Provision an liefrando zu verschenken, um nur Online-Bestellungen
        zu erhalten?<u><br>Wir haben eine Idee !!!</u><br>Warum bauen Sie nicht Ihr eigenes System wie liefrando,
        das Ihr eigenes mit <strong>0%</strong> Provision und <strong>0 €</strong> jährlichen Gebühren für ein Leben
        lang ist?<br>Ich kann mir vorstellen, dass die Frage in deinem Kopf auftaucht :). "Der Bau eines solchen
        Systems wäre sehr kostspielig?"<br>Die Antwort ist eine große Nein. Wir können für nur 1300 € ein
        hochentwickeltes System bauen, das Ihnen gehört.<br><u>Lass mich die nächste Frage erraten :)
        </u><br><br>Wie könnte es möglich sein? Es muss eine Falle oder versteckte Kosten geben?<br>Die
        Antwort ist wieder groß Nein. Es gibt keine Falle. <strong>Sie zahlen nur <span style="font-family:
         Berlin Sans FB Demi"><u>1.300</u></span><u> €</u> und alles gehört Ihnen ein Leben lang mit allen Passwörtern,
          der Verwaltungskontrolle, der Android App + Website + 3 in einem Android-Drucker.<br></strong>Wenn dir das gefällt,
           klicke auf den YouTube-Link unten, um zu sehen, wie es aussieht.<br><a href="https://youtu.be/fHQwuUA5Aqc"
           target="_blank">https://youtu.be/fHQwuUA5Aqc</a><br>Wenn Sie die Demo testen möchten,
           <a href="https://test.ur-techpartner.de/" target="_blank"><strong>klicken Sie hier</strong></a><strong>.
           </strong><br>Zögern Sie nicht, uns zu kontaktieren unter:<br>Whatapp+handy:
           +4917-626-969-472<br>Whatapp+handy: +49 17 645-981-653<br>E-Mail:
            <a target="_blank">fkhalil@ur-techpartner.de</a><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
             <a target="_blank">paribartan.humagain@ur-techpartner.de</a><br>website (FAQs):
             <a href="https://ur-techpartner.de/de/restaurant_ordering/" target="_blank">
             https://ur-techpartner.de/de/restaurant_ordering/</a><br><br>Sehen
             Sie, wie einige Restaurants in Berlin klug mit ihren eigenen Systemen
             spielen.<br><a href="https://yakundyeti-restaurant.de/" target="_blank">https://yakundyeti-restaurant.de/</a><br>
             Sie haben innerhalb von 3 Wochen 2.000 zusätzlich verdient, auch ohne Werbung.<br>mit freundlichen grüßen,
             <br>UrTechPartner<br>Albert-Einstein str.1,49076,Osnabrueck.<br>Ich möchte keine E-Mail erhalten&nbsp;Klicken
             Sie bitte&gt;&gt;&nbsp; <a href="https://ur-techpartner.de/e-mail-unsubscription/" target="_blank">Unsubscribe</a><br><br>
             <br></span></p>
        """, subtype='html')


        with smtplib.SMTP_SSL('smtp.ionos.de', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            with open('already_send.txt','a') as file:
                file.write(i+' , ')
            count+=1
            print(f'The Email to recipient {i} has been send')
            print(f'total {count} email has been send')
    except Exception as e:
        print(e)
        print(f'error occur send{i} email')
        continue

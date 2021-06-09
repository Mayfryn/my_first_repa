import smtplib
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)

smtp_obj.starttls()
smtp_obj.login('softermiioz@gmail.com', '****')
smtp_obj.sendmail(from_addr="softermiioz@gmail.com", to_addrs="el.piankova@gmail.com", msg="Olga Zaslavska says: I did it!")
smtp_obj.close()
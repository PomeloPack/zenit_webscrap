import smtplib
my_email = "p0m3l0pack@gmail.com"
password = "my password"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login( user = my_email, password = password )

connection.sendmail(from_addr = my_email, to_addrs = "santexD@seznam.cz", msg = "Hello World")

connection.close()

"""
total = 0
total = total + get_price("...")
total = total + get_price("...")

try:
    smtpObj = smtplib.SMTP("localhost")
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent emai")
except SMTPException:
    print("Error: unable to send email")
"""




#https://stackoverflow.com/questions/17759860/python-2-smtpserverdisconnected-connection-unexpectedly-closed
#https://bobcares.com/blog/smtp-authentication-error-534/








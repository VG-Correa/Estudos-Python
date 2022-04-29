import imaplib
import os

host = "imap-mail.outlook.com"
port = 993

user = input("Login: ")
password = input("Senha: ")
 
server = imaplib.IMAP4_SSL(host,port)
server.login(user,password)
server.select("Facebook")
status, data = server.search(None,"(INSEEN)")

for num in data[0].split():
    status, data = server.fetch(num, "(RFC822)")
    email_msg = data[0][1]

    soup = BeautifulSoup(markup=email_msg,features="lxml")
    news = soup.find_all("td")[0].text


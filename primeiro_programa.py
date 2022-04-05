#import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

#parâmetros
senha = "******"
msg['From'] = "alcemirmacedo@gmail.com"
msg['To'] = "alcemirmacedo@gmail.com"
msg['Subject'] = "Email enviado pelo Python"

#Criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.ehlo()
server.starttls()

#login na conta para o envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerranento do servidor
server.quit()

print('Mensagem enviada com sucesso')
from urllib.parse import urljoin
from http.server import BaseHTTPRequestHandler, HTTPServer
import smtplib, ssl
#NO PASAR LA CONTRASENYA A NADIE JORDIT
password = "DollarDuck123"
context = ssl.create_default_context()

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        #SI PONEMOS /PRACTICA.HTML 
        if "practica.html" in self.path:
            file = open("practica.html", 'rb')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(file.read())
        #SI PONEMOS /HYPERBEAST.JPG
        elif "hyperbeast.jpg" in self.path:
            file = open("hyperbeast.jpg", 'rb')
            self.send_response(200)
            self.send_header("Content-type", "image/jpg")
            self.end_headers()
            self.wfile.write(file.read())
            #ENVIA UN CORREO
            mail = smtplib.SMTP_SSL("smtp.gmail.com", 465) 
            mail.ehlo() #mensaje de salutació amb el servei/servidor
            mail.login("enterprisedollarduck@gmail.com", password) #login to gmail smtp
            message = "Subject: Hello There!" + "\n\n\nHa intentat entrar: %s" % str(self.client_address) #Cos del missatge
            mail.sendmail("enterprisedollarduck@gmail.com", "enterprisedollarduck@gmail.com", message) #envia el missatge
            mail.quit() 
        else:
            self.send_error(404, "Not Found")


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), GetHandler)

    server.serve_forever()
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import lxml


def ballenoil_scraping(web):
    resultado = requests.get(web)
    sopa = BeautifulSoup(resultado.text, 'lxml')
    valor = sopa.select('.small-12 tbody tr td')[1]
    precio = valor.getText()
    return precio




acount_sid = "ACd68d5d9fefec43914b8dc6f30ef98258"
auth_token = "5575aa3c8b1eeefa701674cfdd2129d3"

client = Client(acount_sid, auth_token)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+34635429905'

client.messages.create(
    body=f'Buenos dias, el precio del gasoil en ballenoil Mostoles es de {ballenoil_scraping("https://www.clickgasoil.com/g/precios-combustible-gasolinera-ballenoil-calle-alfonso-xii-20-en-el-municipio-mostoles")}',
    from_=from_whatsapp_number,
    to=to_whatsapp_number

)

client.messages.create(
    body=f'Buenos dias, el precio del gasoil en ballenoil Alcorcon es de {ballenoil_scraping("https://www.clickgasoil.com/g/precios-combustible-gasolinera-ballenoil-calle-laguna-88-en-el-municipio-alcorcon")}',
    from_=from_whatsapp_number,
    to=to_whatsapp_number

)

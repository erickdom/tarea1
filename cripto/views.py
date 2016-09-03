import base64

from Crypto import Random
from Crypto.Cipher import AES
from django.shortcuts import render
from django.views.generic.base import TemplateView


class Criptonite(TemplateView):
    template_name = "cripto.html"

    def get(self, request, *args, **kwargs):
        try:
            return render(request, self.template_name, {})
        except Exception as e:
            print e

    def post(self, request, *args, **kwargs):
        try:
            data = request.POST
            print data
            mensaje = data.get("mensaje")
            tipo = data.get("tarea")
            print mensaje
            key = "1234567890123456"
            aes = AESCipher(key)
            print tipo
            if tipo == "enc":
                encrypt = aes.encrypt(mensaje)
            else:
                encrypt = mensaje
                mensaje =  aes.decrypt(mensaje)

            data = {
                "encrypt" : encrypt,
                "key" : key,
                "decrypt" : mensaje,
            }
            return  render(request, self.template_name, data)
        except Exception as e:
            print e
            return render(request, self.template_name, {"error":e})

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]


class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))
from Crypto.Hash import SHA256
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.base import TemplateView

from hash.models import Usuario


class Hashing(TemplateView):
    template_name = "hash.html"

    def get(self, request, *args, **kwargs):
        try:
            return render(request, self.template_name, {})
        except Exception as e:
            print e

    def post(self, request, *args, **kwargs):
        try:
            data = request.POST
            usuario = data.get("usuario")
            nombre = data.get("nombre")
            password = data.get("password")
            h = SHA256.new()
            h.update(b'{}'.format(password))
            user = Usuario.objects.create(usuario=usuario, nombre=nombre, password=h.hexdigest())
            user.save()
            ctx = {
                "message": "Se creo el usuario exitosamente"
            }
            return render(request, self.template_name, ctx)
        except Exception as e:
            print e
            return render(request, self.template_name, {"message": e})


class HashingLogin(TemplateView):
    template_name = "hashLogin.html"

    def get(self, request, *args, **kwargs):
        try:
            return render(request, self.template_name, {})
        except Exception as e:
            print e

    def post(self, request, *args, **kwargs):
        try:
            data = request.POST
            usuario = data.get("usuario")
            password = data.get("password")
            h = SHA256.new()
            h.update(b'{}'.format(password))
            users = Usuario.objects.filter(usuario=usuario, password=h.hexdigest())
            if len(users) > 0:
                print users
                request.session["login"] = True
                request.session["Pass"] = h.hexdigest()
                request.session["user"] = usuario
                return HttpResponseRedirect(reverse('hashWelcome'))
            else:
                context = {
                    "error": "usuario no valido"
                }
                return render(request, self.template_name, context)
        except Exception as e:
            print e
            return render(request, self.template_name, {"error": e})


class HashingInit(TemplateView):
    template_name = "hashinit.html"

    def get(self, request, *args, **kwargs):
        if request.session.get("login", False):
            data = {
                "pass": request.session["Pass"],
                "user": request.session["user"],
            }
            return render(request, self.template_name, data)
        else:
            return HttpResponseRedirect(reverse('hashingLogin'))


class HashLogout(TemplateView):
    def get(self, request, *args, **kwargs):
        del request.session["login"]
        del request.session["Pass"]
        del request.session["user"]
        return HttpResponseRedirect(reverse('hashingLogin'))

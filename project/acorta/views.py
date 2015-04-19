from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from models import Url


# url is a models.Url
def formatUrlHtml(url, srvHost, srvPort):
    return "<p><a href=" + url.long_url + ">" + url.long_url + "</a>" + \
        "  -->  <a href='/" + str(url.id) + "'>" + srvHost + ":" + srvPort + \
        "/" + str(url.id) + "</a></p>"


def barra(request):
    formul = '<br><form action="" method="POST" accept-charset="UTF-8">' + \
        'URL para acortar: <input type="text" name="url">' + \
        '<input type="submit" value="Acorta!"></form><hr>'
    srvHost = str(request.META["SERVER_NAME"])
    srvPort = str(request.META["SERVER_PORT"])

    if request.method == "GET":
        urlshtml = ""
        urls = Url.objects.all()
        for url in urls:
            urlshtml += formatUrlHtml(url, srvHost, srvPort)
        return HttpResponse(formul + urlshtml)
    elif request.method == "POST":
        longUrl = request.POST.get("url", "")
        if longUrl == "":
            salida = "Incorrect post or empty url"
        else:
            if not longUrl.startswith("http://") and \
                    not longUrl.startswith("https://"):
                longUrl = "http://" + longUrl
            try:
                newUrl = Url.objects.get(long_url=longUrl)
            except Url.DoesNotExist:
                newUrl = Url(long_url=longUrl)
                newUrl.save()
            salida = formatUrlHtml(newUrl, srvHost, srvPort)
        return HttpResponse(salida)
    else:
        return HttpResponseNotAllowed("Method not allowed in this server")


def redirect(request, numUrl):
    try:
        url = Url.objects.get(id=numUrl)
        return HttpResponseRedirect(url.long_url)
    except Url.DoesNotExist:
        return HttpResponseNotFound("404 Page not found")


def notFound(request):
    return HttpResponseNotFound("404 Page not found")

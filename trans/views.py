from django.shortcuts import render
import googletrans
# Create your views here.
def index(request):
    context = {
        "ndict" : googletrans.LANGUAGES
    }
    b = request.GET.get("bf", "")
    if b:
        f = request.GET.get("fr", "")
        t = request.GET.get("to", "")
        tr = googletrans.Translator()
        a = tr.translate(b, src=f, dest=t)
        context.update({
            "btext" : b,
            "fr" : f,
            "to" : t,
            "atext" : a.text
        })

    return render(request, "trans/index.html", context)
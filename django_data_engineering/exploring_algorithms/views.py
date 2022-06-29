from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def index(request):
    # name = request.GET.get("name") or "world"
    # return HttpResponse(f"Hello, {name}!")
    name = "music lover"
    return render(request, "base.html", {"name": name})


def search(request):
    # name = request.GET.get("name") or "world"
    # return HttpResponse(f"Hello, {name}!")
    search = request.GET['search']
    return render(request, "search.html", {"search": search})

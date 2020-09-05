from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.shortcuts import redirect
import markdown2

from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    markdown_content = util.get_entry(title)
    if not markdown_content:
        return render(request, "encyclopedia/error.html", {
            "entry_title": title
        })
    html_content = markdown2.markdown(markdown_content)
    return render(request, "encyclopedia/entry.html", {
        "entry_title": title,
        "entry_body": html_content
    })

def search(request):
    if request.method == "POST":
        search_request = request.POST['q']
        entry_match = util.get_entry(search_request)
        if entry_match:
            return redirect('entry', title=search_request)
        all_entries = util.list_entries()
        return HttpResponse(search_request)
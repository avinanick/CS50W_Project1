from django.shortcuts import render
from django.shortcuts import redirect
import markdown2
from django import forms

from . import util

class NewPageForm(forms.Form):
    page_title = forms.CharField(label="Page Title")
    page_body = forms.Textarea()
    page_submit = forms.

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

def new_page(request):
    return render(request, "encyclopedia/create_page.html", {
        "form": NewPageForm()
    })

def search(request):
    if request.method == "POST":
        search_request = request.POST['q']
        entry_match = util.get_entry(search_request)
        if entry_match:
            return redirect('entry', title=search_request)
        all_entries = util.list_entries()
        partial_matches = [i for i in all_entries if search_request in i]
        return render(request, "encyclopedia/search_results.html", {
            "entries": partial_matches
        })
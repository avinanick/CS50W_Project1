from django.shortcuts import render
import markdown2

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
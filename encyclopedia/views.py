from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import markdown2
from random import choice
from .form import EditArticle, NewArticle

from . import util


def convert_to_html(text):
    return markdown2.markdown(text)



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def article(request, name):
    get_entery = util.get_entry(name)
    if get_entery == None:
        return render(request, "encyclopedia/error.html", {
            "error": f"{ name } is not in the encyclopedia"
        })
    return render(request, "encyclopedia/article.html", {
        "content":convert_to_html(get_entery),
        "title":name
    })  



def search(request):
    searched = request.GET['q']
    entries = util.list_entries()
    search_results = []
    if searched.upper() in (name.upper() for name in entries):
        return redirect("article", name=searched)
    else:
        for i in entries:
            if searched.upper() in i.upper():
                search_results.append(i)
        
        return render(request, "encyclopedia/search.html", {
            "search_results":search_results
        })



def new_article(request):
    if request.method == "POST":
        form = NewArticle(request.POST)
        entries = util.list_entries()
        if form.is_valid():
            new_article = form.cleaned_data
            for j in entries:
                if new_article["title"].upper() == j.upper():
                    title = new_article["title"]
                    return render(request, "encyclopedia/error.html", {
                        "error": f"their is already an article called {title}"
                    })
            util.save_entry(new_article["title"], new_article["content"])
            return redirect("index")
        else:
            return render(request, "encyclopedia/create_article.html", {
                "form":form
            })
    return render(request, "encyclopedia/create_article.html", {
        "form":NewArticle()
        })


def edit(request, name):
    if request.method == "POST":
        edited_form = EditArticle(request.POST)
        if edited_form.is_valid():
            edited_form = edited_form.cleaned_data
            content = edited_form["content"]
            file = open(f'entries/{name}.md', 'w')
            file.write(content)
            return redirect("index")
    else:
        now_content = util.get_entry(name)
        form = EditArticle({
            'content': now_content,
        })
    return render(request, 'encyclopedia/edit_article.html', {
    'form': form,
    'name': name
    })




def random(request):
    rand_choise = choice(util.list_entries())
    return redirect("article", name=rand_choise)


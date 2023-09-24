from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django import forms
from . import util

import markdown2
import random

class new_form(forms.Form) :
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Page title'}), 
        label='')
    text = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder" : "Enter text here" , 
        # "rows":5, "cols":5,
        }),
        label="")

all_entries = util.list_entries(True) 
# Home page
def index(request) :
    return render(request, "encyclopedia/index.html")

# Listing entire pages
def all_pages(request):
    want_all_entries = True
    return render(request, "encyclopedia/all_pages.html", {
        "entries": util.list_entries(want_all_entries),
        "want_all_entries" : want_all_entries 
    })


# page url
def return_by_title(request, route):
    # page_exists is a bool
    page_exists = None
    # Return by exact title
    if util.get_entry(route) :
        page_exists = True
        return render(request, "encyclopedia/page.html", {
            "content" : markdown2.markdown(util.get_entry(route)), "title" : route, "page_exists" : page_exists, "entries" : all_entries 
        })

# Creating Page
def create_page(request) :
    form = new_form(request.POST)
    if request.method == "GET" :
        page_exists = True
        return render(request, "encyclopedia/newpage.html", {
            "form" : form , "entries" : all_entries 
        })
    elif request.method == "POST" :
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["text"]
            util.save_entry(title,content)
            if util.get_entry(title) :
                return HttpResponseRedirect(reverse('page',args=[title]))
            else :
                return HttpResponse("<h1>ERROR</h1>")
    else:
        form = new_form()

    return render(request, "encyclopedia/newpage.html", {
        "form": form, "entries" : all_entries 
        })

# Editing a page
def edit_page(request) :
    return HttpResponse("hi")

# Searching for a page
def search(request) :
    title = request.GET.get("q","")
    if request.method == "GET" :
        want_all_entries = False
        page_exists = False
        return render(request, "encyclopedia/all_pages.html", {
            "search_entries" : util.list_entries(want_all_entries, title) , 
            "title" : title, 
            "page_exists" : page_exists, 
            "entries" : all_entries,
            "want_all_entries" : want_all_entries
        })

# Random Page
def random_page(request) :
    all_pages = util.list_entries(True)
    number_of_pages = len(all_pages)
    random_num = random.randint(0, number_of_pages -1)
    return HttpResponseRedirect(reverse('page',args=[all_pages[random_num]])) 
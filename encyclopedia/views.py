from django.shortcuts import render
from django.http import HttpResponseRedirect
from random import choice
import markdown2 

from . import util


def index(request):
    """
    The "index" function is the initial page. If request method is GET,
    it returns a list of avaliable entries. POST method is used to the search function.
    """
    if request.method == "POST":
        search_value = request.POST["q"]
        # "search_value"" is what the user typed in the "search" field.

        entries = util.list_entries()
        # request a list of avaliable entries.

        match = []
        # match is an array that will store all titles 
        # corresponding to the one typed by the user
        
        for entry in entries:
            if search_value in entry:
                if search_value == entry:
                    return HttpResponseRedirect(f"/wiki/{entry}")
                    # if the search_value is equal to any entry from entries,
                    # redirect user to entry page.
                else:
                    # else, append is match list that entry, 
                    # because some part of that entry contains the sought value.
                    match.append(entry)
        
        return render(request, "encyclopedia/search.html", {
            # return a render with a list of "matched" entries.
            "entries": match,
            "search": search_value
        })

    else:
        return render(request, "encyclopedia/index.html", {
            # if the request method is not POST, it is GET.
            # So, only render a list of avaliable titles.
            "entries": util.list_entries()
        })

def entry(request, entry):
    """
    The "entry" function renders on the page the title and content of an entry. 
    """
    content = util.get_entry(entry)
    if content == None:
        # if the content is "None", that entry does not exist is avaliable entries.
        # So, only render a error page.
        error = ["Error: Page not found!","""This page does not exists on this wiki.
                You are welcome to create it by clicking on 'Create New Page' 
                link in the menu on the left."""]
        return render(request, "encyclopedia/error.html",{
            # error its an array that allows use "error.html" 
            # for all errors in all cases.
            "error": error[0],
            "error2": error[1]
        })
    else:
        # if the content is not "None", that entry exists. 
        # So, just render that.
        return render(request, "encyclopedia/entry.html",{
            "entry": entry,
            "content" : markdown2.markdown(content)
    })

def new(request):
    """
    The "new" function is used to create and save a new entry.
    """
    if request.method == "POST":
        #if the request method is POST, user want to create a new entry 
        # and he/she have submited forms.
        data = request.POST
        # data is the variable that stores all data received from the user
        if data["title"] in util.list_entries():
            error = ["Error: This title already exists!",
            """Make sure your title does not exists yet."""]
            return render(request, "encyclopedia/error.html",{
                # error its an array that allows use "error.html" 
                # for all errors in all cases.
                "error": error[0],
                "error2": error[1]
            })
        else:
            # if title does not exists, its really a new one. 
            # So, create a new file and save content on it.

            util.save_entry(data["title"], data["content"])
            return HttpResponseRedirect(f"/wiki/{data['title']}")

    
    return render(request, "encyclopedia/new.html")
    # if the method is GET, it renders a page with forms 
    # for the user to enter the title and content.
  
def edit(request, entry):
    """
    The "edit" funcion renders a page with forms to edit an entry page.
    """
    if request.method == "POST":
        #if the user submited a form, he/she wants to edit a page.
        data = request.POST
        # data is the variable that stores all data received from the user
        util.save_entry(entry, data["content"])
        # save new data 
        return HttpResponseRedirect(f"/wiki/{entry}")
        # redirects the user to the updated version of the page.

    content = util.get_entry(entry)
    return render(request, "encyclopedia/edit.html",{
        "title": entry,
        "content" : content
    })
    # if the method is GET, it renders a page with all the content for editing.



def random(request):
    """
    The "random" function selects a random entry and redirects the user to the entry's page.
    """
    random_title = choice(util.list_entries())
    return HttpResponseRedirect(f"/wiki/{random_title}")


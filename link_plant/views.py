from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy


from .models import Profile, Link

class LinkListView(ListView): #gives us the functionality to list out our links
    # query for all the links with Link.objects.all()
    # context = ('links' : links)
    # return render (request, 'link_list_html', context)
    # List View has all of these included

    model = Link
    # looks for template called model_list.html-> link_list,.html

class LinkCreateView(CreateView):
    # create forms.py file and form
    # check if this was Post or get request
    # return an empty form or save the form data
    # createView make this whole process simple

    model = Link
    fields = "__all__"
    success_url = reverse_lazy('link-list')
    # creates a template model_form -> link_form.html

class LinkUpdateView(UpdateView):
    # create a form
    # check if a get request for put request
    # either render the form or update and save in db
    # this can all be done with UpdateView
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')

class LinkDeleteView(DeleteView):
    # take in id/pk of an object
    # query to db for that object
    # check if it exists -> delete the object
    model = Link
    success_url = reverse_lazy('link-list')
    # form to submit to delete the item
    # expect a template name model_confirm_delete.html
    # link_confirm_delete.html

def profile_view( request, profile_slug):
    profile = get_object_or_404(Profile, slug= profile_slug)
    links = profile.links.all()
    context = {
        'profile' : profile,
        'links' : links
    }
    return render( request, 'link_plant/profile.html', context)
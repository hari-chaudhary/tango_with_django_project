from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

#Import Category model
from rango.models import Category

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'rango/index.html', context_dict)

def about(request):

	context_dict = {'boldmessage': "Rango's about page."}
	
	# return HttpResponse("Rango says here is the about page. <br/> <a href='/rango/'>Index</a>")
	return render(request, 'rango/about.html', context_dict)
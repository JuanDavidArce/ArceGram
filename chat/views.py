from django.shortcuts import render

# Create your views here.
def messages_page(request):
    return render(request,"chat/start_point_messages.html")

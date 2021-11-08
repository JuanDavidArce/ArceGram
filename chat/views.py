from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from chat.models import Thread
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.views import View


@login_required
def messages_page(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'Threads': threads
    }
    return render(request, 'chat/messages.html', context)


class New_thread(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
            conversation = Thread(first_person_id=request.POST['first_person_id'],second_person_id=request.POST['second_person_id'])  
            conversations1= Thread.objects.all().filter(first_person_id=request.POST['first_person_id']).filter(second_person_id=request.POST['second_person_id'])
            conversations2= Thread.objects.all().filter(first_person_id=request.POST['second_person_id']).filter(second_person_id=request.POST['first_person_id'])
            if len(conversations1)==0 and len(conversations2)==0: 
                conversation.save()

            return redirect("chat:chat")
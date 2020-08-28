from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import forms 
from . import models
from django.contrib import messages

@login_required
def index(request):
    all_tickets = models.TicketModel.objects.all()
    return render(request, 'index.html', {'all_tickets': all_tickets})


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

        
    form = forms.LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def add_ticket_view(request):
    if request.method == "POST":
        form = forms.AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_ticket = models.TicketModel.objects.create(
                title = data['title'],
                description = data['description'],
                user_filed = request.user
            )
            if new_ticket:
                return HttpResponseRedirect(reverse("homepage"))
    form = forms.AddTicketForm()
    return render(request, 'generic_form.html', {'form': form})


def edit_ticket_view(request, ticket_id):
    ticket = models.TicketModel.objects.get(id=ticket_id)
    if request.method == "POST":
        form = forms.AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data["title"]
            ticket.description = data["description"]
            ticket.save()
        return HttpResponseRedirect(reverse("ticket_details", args=[ticket.id]))


    data = {
        "title": ticket.title,
        "description": ticket.description

    }
    form = forms.AddTicketForm(initial=data)
    return render(request, 'generic_form.html', {'form': form} )

@login_required
def assign_ticket_view(request, ticket_id):
    ticket = models.TicketModel.objects.get(id=ticket_id)
    ticket.status = "In Progress"
    ticket.user_assigned = ticket.user_filed
    ticket.user_ticket_completed = None
    ticket.save()
    messages.success(request, "Assigned to: " + str(ticket.user_filed))
    return HttpResponseRedirect(reverse('ticket_details', args=[ticket.id]))  

@login_required
def invalid_ticket_view(request, ticket_id):
    ticket = models.TicketModel.objects.get(id=ticket_id)
    ticket.status = "Invalid"
    ticket.user_assigned = None
    ticket.user_ticket_completed = None
    ticket.save()
    
    return HttpResponseRedirect(reverse('ticket_details', args=[ticket.id]))

@login_required
def complete_ticket_view(request, ticket_id):
    ticket = models.TicketModel.objects.get(id=ticket_id)
    ticket.status = "Done"
    ticket.user_assigned = None
    ticket.user_ticket_completed = ticket.user_filed
    ticket.save()
    
    return HttpResponseRedirect(reverse('ticket_details', args=[ticket.id]))

@login_required
def new_ticket_view(request, ticket_id):
    ticket = models.TicketModel.objects.get(id=ticket_id)
    ticket.status = "New"
    ticket.user_assigned = None
    ticket.user_ticket_completed = None
    ticket.save()
    
    return HttpResponseRedirect(reverse('ticket_details', args=[ticket.id]))




def ticket_detail_view(request, ticket_id):
    ticket = models.TicketModel.objects.filter(id=ticket_id).first()
    return render(request, 'ticket_detail.html', {'ticket': ticket})

def user_detail_view(request, user_name):
    user = models.TicketModel.objects.filter(user_filed__username=user_name).first()
    all_ticket = models.TicketModel.objects.filter(user_filed__username=user_name)
    return render(request, 'user_detail.html', {'all_ticket': all_ticket, 'user': user })



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("loginpage"))

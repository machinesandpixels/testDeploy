from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        # Check if user has made inquery
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id,
                user_id=user_id
                )
            if has_contacted:
                messages.error(
                    request, 
                    'You have already made an inquiry for this listing.'
                    )
                return redirect('/listings/', listing_id=listing_id)
                

        contact = Contact(

            listing_id=listing_id,
            listing=listing,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id

        )

        contact.save()

        return redirect('/listings/', listing_id=listing_id)
       

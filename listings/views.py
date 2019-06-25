from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
 
from listings.choices import bedroom_choices, price_choices, state_choices


def index(request):
    # listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        "listings": paged_listings
    }
    
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    context = {
        # 'listings': listings,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "state_choices": state_choices
    }
    return render(request, 'listings/search.html', context)

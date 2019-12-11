from django.http import request
from django.shortcuts import render, redirect, render_to_response
from django.views import generic
from django.contrib.gis.geos import Point, GEOSGeometry
from django.contrib.gis.db.models.functions import Distance
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Shop, User
from django import forms


# Create your views here.


class Home(generic.ListView):
    model = Shop, User
    context_object_name = 'Nearby_shops'
    user = User.objects.get(username='user')
    testlon = user.userLocation.x
    testlat = user.userLocation.y
    userCurrentLocation = Point(testlon, testlat, srid=4326)
    queryset = Shop.objects.annotate(distance=Distance('shopLocation', userCurrentLocation)).order_by('distance')[0:10]
    template_name = 'WebMap/index.html'


@csrf_exempt
def position(request):
    if request.method == "POST":

        lf = LocationForm(request.POST)
        if lf.is_valid():
            Latitude = lf.cleaned_data['latitude']
            Longitude = lf.cleaned_data['longitude']
            location = GEOSGeometry('POINT(%s %s)' % (Longitude, Latitude))
            userLoc = User.objects.filter(username='user').values('userLocation')
            if len(userLoc) == 0:
                user = User.objects.create(username='user', userLocation=location)
                user.save()
            else:
                if location != userLoc:
                    updateuser = User.objects.filter(username='user').update(userLocation=location)

    else:
        lf = LocationForm()

    return render_to_response('position.html', {'lf': lf})


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = 'Please Error'
        return render(request, 'WebMap/index.html', {'error_msg': error_msg})

    shop_list = Shop.objects.filter(shopName__contains=q)
    return render(request, 'search.html', {'error_msg': error_msg, 'shop_list': shop_list})


class LocationForm(forms.Form):
    latitude = forms.CharField(label='Latitude', max_length=100, widget=forms.TextInput(attrs={'id': 'Latitude'}))
    longitude = forms.CharField(label='Longitude', max_length=100, widget=forms.TextInput(attrs={'id': 'Longitude'}))


class SearchForm(forms.Form):
    text = forms.CharField(label='text', max_length=100)

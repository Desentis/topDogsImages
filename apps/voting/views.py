from django.shortcuts import render
from .models import Voted

from requests import get, HTTPError
from json import loads


def index(request):

    if request.method == 'GET':
        voting = get_voting_images()
        context = {'dogs': voting}
        return render(request, 'voting/index.html', context)

    if request.method == 'POST':
        voted_link = loads(request.body).get('link')
        if voted_link:
            make_vote(voted_link)
        return render(request, 'voting/index.html')


def best(request):
    most_voted = Voted.objects.order_by("votes")[:3]
    context = {'most_voted_dogs': most_voted}
    return render(request, 'voting/best.html', context)


def get_voting_images():

    api_url = 'https://dog.ceo/api/breeds/image/random'
    number_of_images = 2
    number_of_attempts = 10

    image_urls = []
    while len(image_urls) < number_of_images and number_of_attempts > 0:
        number_of_attempts -= 1

        try:
            r = get(api_url)
            r.raise_for_status()
        except HTTPError as err:
            continue

        image_url = loads(r.text).get('message')

        if not image_url:
            continue

        try:
            r = get(image_url)
            r.raise_for_status()
        except HTTPError as err:
            continue

        image_urls.append(image_url)

    voting = []
    for url in image_urls:
        vote = Voted.objects.filter(link=url)
        voting.append({'link': url, 'votes': vote[0].votes if vote else 0})

    return voting


def make_vote(voted_link):
    vote = Voted.objects.filter(link=voted_link)
    if vote:
        Voted.objects.filter(id=vote[0].id).update(votes=vote[0].votes + 1)
    else:
        Voted.objects.create(link=voted_link, votes=1)

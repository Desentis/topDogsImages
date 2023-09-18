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


def get_voting_images():

    api_url = 'https://dog.ceo/api/breeds/image/random'
    number_of_images = 2

    image_urls = []
    for i in range(number_of_images):
        try:
            r = get(api_url)
            r.raise_for_status()

        except HTTPError as err:
            raise err
            # API error
            pass

        else:
            url = loads(r.text).get('message')
            if url:
                image_urls.append(url)

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

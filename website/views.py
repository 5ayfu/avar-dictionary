from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def dictionary(request):
    return render(request, 'website/dictionary.html')


def phrasebook(request):
    return render(request, 'website/phrasebook.html')


def grammar(request):
    return render(request, 'website/grammar.html')


def names(request):
    return render(request, 'website/names.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    return render(request, 'website/contact.html')

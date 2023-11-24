from .models import AskLetter


def new_letters(request):
    return {"new_letters": AskLetter.objects.filter(is_read=False)}

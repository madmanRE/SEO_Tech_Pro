from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AskLetterForm
from .models import AskLetter


def index(request):
    form = AskLetterForm
    context = {"form": form}
    return render(request, "main/pages/index.html", context)


def get_form(request):
    if request.method == "POST":
        form = AskLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            mail = form.cleaned_data.get("mail")
            message = form.cleaned_data.get("message")

            ask_letter = AskLetter.objects.create(
                name=name,
                mail=mail,
                message=message,
            )
            ask_letter.save()
            return redirect("/")
        else:
            print(form.errors)
            return render(request, "main/pages/index.html", {"form": form})
    else:
        form = AskLetterForm()
        return render(request, "main/pages/index.html", {"form": form})


def admin(request):
    new_letters = AskLetter.objects.filter(is_read=False)
    read_letters = AskLetter.objects.filter(is_read=True)
    context = {"new_letters": new_letters, "read_letters": read_letters}
    return render(request, "main/pages/admin.html", context)


def admin_detail_view(request, pk):
    letter = AskLetter.objects.filter(id=pk).first()
    letter.is_read = True
    letter.save()
    context = {"letter": letter}
    return render(request, "main/pages/admin_detail.html", context)

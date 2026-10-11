from django.shortcuts import redirect, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import DiaryEntry, User
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden, HttpResponseNotFound

def RegisterView(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/login')
    return render(request, 'diaries/register.html', {"form": form})


def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        userid = user.id
        return redirect('user/' + str(userid))

    else:
        return render(request, 'diaries/index.html')

@login_required
def UserView(request, userid):
    # ----- FLAW 1: Broken access control -----

    if request.user.is_authenticated:
        user = User.objects.get(pk=userid)
        all_diary_entries = DiaryEntry.objects.filter(user=user)[:]
        context = {'all_diary_entries': all_diary_entries, 'userid': userid}
        return render(request, 'diaries/index.html', context)
    
    # -----------------------------------------
    
    # ----- FIX 1: Broken access control ------

    #if request.user.is_authenticated and request.user.id == userid:
    #    user = User.objects.get(pk=userid)
    #    all_diary_entries = DiaryEntry.objects.filter(user=user)[:]
    #    context = {'all_diary_entries': all_diary_entries, 'userid': userid}

    #    return render(request, 'diaries/index.html', context)
    #else:
    #    return HttpResponseForbidden("Forbidden request")
    
    # ------------------------------------------


def add(request):
    if not request.user:
        return redirect('/')

    if request.method == "POST":
        user = request.user
        new_content = request.POST.get('content')
        if len(new_content) == 0:
            return redirect('/')

        time = timezone.now()

        # ----- FLAW 3: SQL-injection -----

        c = connection.cursor()
        c.executescript(
            """INSERT INTO diaries_diaryentry (user_id, pub_date, diary_text)
            VALUES ('%s', '%s', '%s')"""
            % (user.id, time, new_content)
        )
        print(time)
        c.close()

        # ---------------------------------

        # ----- FIX 3: SQL-injection ------

        # diary_entry = DiaryEntry.objects.create(user=user, diary_text=new_content, pub_date=time)
        # diary_entry.save()
    
        # ---------------------------------

    return redirect('/')


@login_required
# ----- FLAW 5: CSRF -----
@csrf_exempt # FIX 5: Remove the @csrf_exempt
# ------------------------
def delete(request):
    if not request.user:
        return redirect('/')
    
    if request.method == "POST":
        user = request.user
        diaries = DiaryEntry.objects.filter(user=user)[:]
        diaries.delete()

    return redirect('/')


def CsrfView(request):
    return render(request, 'diaries/csrf.html')

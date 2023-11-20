
#from django.shortcuts import render
#from .models import User, JLibrary, Journal, Emotions


#def view_1(request):
#    user_id = 1  # Assuming the user ID is 1
#    journals = Journal.objects.filter(jlibrary__user_id=user_id)
#    context = {'journals': journals}
#    return render(request, 'view_1.html', context)

#def view_2(request):
#    user_id = 1  # Assuming the user ID is 1
#    journals = JLibrary.objects.filter(user_id=user_id, journal__emotion__emotion='happy')
#    context = {'journals': journals}
#    return render(request, 'view_2.html', context)

#def view_3(request):
#    user_id = 1
#    emotion_id = 1
#    journals_to_delete = Journal.objects.filter(emotion__emotionid=emotion_id, jlibrary__user_id=user_id)
#    context = {'journals_to_delete': journals_to_delete}
#    return render(request, 'view_3.html', context)

#def view_4(request):

#    result = Emotions.objects.filter(eid__isnull=True).union(Exercises.objects.filter(eid__isnull=True))

#   context = {'result': result}
#    return render(request, 'view_4.html', context)

#def view_5(request):
#    combined_entries = Emotions.objects.values('emotion').union(Exercises.objects.values('exname'))
#    context = {'combined_entries': combined_entries}
#    return render(request, 'view_5.html', context)

#def view_6(request):
#    users_after_2005 = Users.objects.filter(dob__year__gt=2005)

#    context = {'users_after_2005': users_after_2005}
#    return render(request, 'view_6.html', context)

#def view_7(request):
#    males_june_birth = Users.objects.filter(pronouns='M', dob__month='June')

#    context = {'males_june_birth': males_june_birth}
#    return render(request, 'view_7.html', context)

#def view_8(request):
#    journals_with_words = Journal.objects.filter(content__icontains='content1') | Journal.objects.filter(content__icontains='content2')

#    context = {'journals_with_words': journals_with_words}
#    return render(request, 'view_8.html', context)

#def view_9(request):
#    alina_pronouns = Users.objects.get(fname='Alina').pronouns
#    users_same_pronouns = Users.objects.filter(pronouns=alina_pronouns).exclude(fname='Alina')

#    context = {'users_same_pronouns': users_same_pronouns}
#    return render(request, 'view_9.html', context)


#def view_10(request):
#    users_with_a = Users.objects.filter(lname__icontains='a').count()

#    context = {'users_with_a': users_with_a}
#    return render(request, 'view_10.html', context)
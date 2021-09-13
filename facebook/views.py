from django.shortcuts import render

# Create your views here.
count = 0
def play(request):
    return render(request, 'play.html')

def play2(request):
    name = '정원'
    global count
    count += 1   
    age = 20
    if age > 19:
        status = '성인'
    else:
        status = '청소년'
    return render(request, 'play2.html', { 'name': name, 'cnt': count, 'age': status})
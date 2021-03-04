from django.shortcuts import render


def get_main(request):
    return render(context={},
                  template_name='main/homepage.html',
                  request=request)

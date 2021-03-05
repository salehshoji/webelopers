from django.shortcuts import render


def profile(request):
    return render(request=request,
                  template_name='profiles/profile.html',
                  context={})

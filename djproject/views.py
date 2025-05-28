from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import LogoutView

# class CustomLogoutView(LogoutView):
#     def get_next_page(self):
#         next_page = self.request.GET.get('next')
#         if next_page:
#             return next_page
#         return super().get_next_page()


def main(request):
    return render(request,'main.html')

def first_pg(request):
    return render(request,'first_page.html')
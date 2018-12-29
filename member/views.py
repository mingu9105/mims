from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from member.models import Member
from django.utils import timezone

from django.urls import reverse_lazy

# from django.contrib.auth.forms import UserCreationForm

from django.views import generic

from django.conf import settings

from member.models import Member
from member.forms import CustomUserCreationForm, MemberForm

# Create your views here.


class SignUp(generic.CreateView):
        model = Member
        form_class = CustomUserCreationForm
        second_form_class = MemberForm
        success_url = reverse_lazy('login')
        template_name = 'member/signup2.html'

        def get_context_data(self, **kwargs):
                #Get the context
                context = super(SignUp, self).get_context_data(**kwargs)
                #Adding the second form
                context['member_form'] = self.second_form_class
                return context

        def form_valid(self, form):
                if self.request.method == 'POST':
                        user_form = CustomUserCreationForm(self.request.POST)
                        member_form = MemberForm(self.request.POST)
                        print("self.request.?",self.request.member)
                        print("self.request.POST",self.request.POST)
                        print("user_form.is_valid()",user_form.is_valid())
                        print("member_form.is_valid()",member_form.is_valid())
                        if user_form.is_valid() and member_form.is_valid():
                                user_form.save()
                                member_form.save()
                                print("user_form.is_valid()",user_form.is_valid())
                        print("form_valid------------")
                        print(settings)
                        # return HttpResponseRedirect(self.get_success_url())
                        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)


def join0(request):
    if request.method == 'GET':
        return render(request, 'member/signup1.html', {})


def join(request):
    if request.method == 'GET':
        return render(request, 'member/signup2.html', {})
    else:
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_name = request.POST['user_name']
        user_num1 = request.POST.get('user_num_1', False)
        user_num2 = request.POST.get('user_num_2', False)
        user_years = request.POST.get('user_years', False)
        user_month = request.POST.get('user_month', False)
        user_day = request.POST.get('user_day', False)
        user_phone_1 = request.POST.get('user_phone_1', False)
        user_phone_2 = request.POST.get('user_phone_2', False)
        user_email = request.POST.get('user_email', False)
        user_address = request.POST.get('user_address', False)
        user_doctor_no = request.POST.get('user_doctor_no', False)
        user_hospital_no1 = request.POST.get('user_hospital_no1', False)
        user_hospital_no2 = request.POST.get('user_hospital_no2', False)
        user_hospital_no3 = request.POST.get('user_hospital_no3', False)

        member = Member(user_id=user_id, user_pw=user_pw, user_name=user_name, user_num1=user_num1, user_num2=user_num2, user_years=user_years, user_month=user_month,
                        user_day=user_day, user_email=user_email, user_phone_1=user_phone_1, user_phone_2=user_phone_2, user_address=user_address, user_doctor_no=user_doctor_no, user_hospital_no1=user_hospital_no1, user_hospital_no2=user_hospital_no2,
                        user_hospital_no3=user_hospital_no3)

        member.c_date = timezone.now()
        member.save()

        return HttpResponse('가입 완료' + user_id + user_pw + user_name)
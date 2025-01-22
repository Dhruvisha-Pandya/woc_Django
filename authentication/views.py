from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from .forms import UserRegistrationForm,CustomAuthenticationForm

#login view
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # Log the user in after form submission
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
    
# register view
def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password=form.cleaned_data.get('password')
            user.set_password(password)
            user.save()

            new_user = authenticate(email=user.email, password=password)
            if new_user is not None:
                login(request, new_user)
            return redirect('home')  # Redirect to the home page 
        
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/signup.html', {'form': form}) 
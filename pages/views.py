from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home_view(request):
	return render(request, 'pages/home.html')

def about_view(request):
	return render(request, 'pages/about.html')

def contact_view(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			print("Valid data")

			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']

			message_body = f"This is an email from your portfolio\nName:{name}\nEmail:{email}\nMessage:{message}"

			send_mail(
				"Email from Portfolio",
				message_body,
				email,
				['daphane.elizabeth@gmail.com'] #<-who should get it
			)
		else:
			print("Invalid form data")
	else:
		form = ContactForm()
	return render(request, 'pages/contact.html', {"form": form})


from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method =="POST":
		# Do stuff
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# Send email
		send_mail(
			message_name,	# Subject
			message,	# Message
			message_email,	# From email
			['heartattackwarning999@gmail.com'],	# To email
			fail_silently=False,
			)




		return render(request, 'contact.html', {'message_name': message_name})

	else:
		# Return a page
		return render(request, 'contact.html', {})
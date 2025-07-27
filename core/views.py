from django.shortcuts import render
from django.http import JsonResponse
from .forms import WaitlistForm
from .utils import send_mail


def index(request):
    form = WaitlistForm()
    return render(request, 'index.html', {'form': form})

def submit_waitlist(request):
    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            entry = form.save()

            # 📨 Notify Admin
            send_mail(
                template='waitlist_admin.html',
                data={
                    'email': 'Homelandermailing@gmail.com',
                    'subject': '🎉 New Homelander Waitlist Signup',
                    'name': getattr(entry, 'name', 'User'),
                    'context': {
                        'email': entry.email,
                        'role': entry.get_role_display(),
                        'joined': entry.created_at.strftime('%Y-%m-%d %H:%M'),
                    }
                }
            )

            # 🙌 Send Confirmation to User
            send_mail(
                template='waitlist_user.html',
                data={
                    'email': entry.email,
                    'subject': '🎉 Welcome to the Homelander Waitlist',
                    'name': getattr(entry, 'name', 'User'),
                    'context': {
                        'role': entry.get_role_display(),
                    }
                }
            )

            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
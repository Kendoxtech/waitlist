from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage


def send_mail(template, data={}):
    url = "http://localhost:8000/static/email/"

    # Get name and email directly from data
    name = data.get('name', 'User')
    email = data.get('email')

    template_data = {
        'homelander': f"{url}homelander.png",
        'social_icon_twitter': f"{url}social-icon-x.png",
        'social_icon_fb': f"{url}social-icon-fb.png",
        'social_icon_ig': f"{url}social-icon-ig.png",
        'social_icon_tiktok': f"{url}social-icon-tiktok.png",
        'social_icon_linkedin': f"{url}social-icon-linkedin.png",
        'name': name,
    }

    try:
        data['context'].update(template_data)
    except KeyError:
        data['context'] = template_data

    if email and 'subject' in data:
        message = render_to_string(template, data['context'])
        msg = EmailMessage(
            subject=data['subject'],
            body=message,
            from_email=f"Homelander <{settings.EMAIL_HOST_USER}>",
            to=[email],
        )
        msg.content_subtype = 'html'
        msg.send()
    else:
        raise ValueError("Missing required keys: 'email' and 'subject'")

from django.core.mail import send_mail
from django.conf import settings

def mail_send(email, name=""):
    subject = 'Thank You for Contacting Us!'
    message = f"""
    Hi {name if name else "there"},

    Thank you for reaching out to us through our portfolio website. We appreciate you taking the time to contact us.

    This is a quick confirmation that we have received your message, and we will get back to you as soon as possible.
    If your inquiry is urgent, please feel free to reach out to us directly via our contact number or social media channels.


    Best regards,
    Sameer Ahmed
    Portfolio Team

    P.S. You can always stay updated with our latest projects by following us on our social media channels!

    """
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    fail_silently = False
    
    print("sending mail")
    send_mail(subject, message, from_email, recipient_list, fail_silently)

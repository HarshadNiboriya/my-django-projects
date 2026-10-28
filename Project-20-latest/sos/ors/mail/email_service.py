from django.core.mail import send_mail, EmailMessage
from .email_builder import EmailBuilder


class EmailService:

    @staticmethod
    def send(details, sending_mail, obj):
        if (sending_mail == 'signUp'):
            msg = EmailBuilder.sign_up(obj)
            email_message = EmailMessage(details.subject, msg, details.frm, details.to)
            email_message.content_subtype = 'plain'

            try:
                email_message.send()
            except Exception as e:
                raise Exception(e)


        elif (sending_mail == 'forgetPassword'):
            msg = EmailBuilder.forgot_password(obj)
            email_message = EmailMessage(details.subject, msg, details.frm, details.to)
            email_message.content_subtype = 'plain'

            try:
                email_message.send()
            except Exception as e:
                raise Exception(e)

        elif (sending_mail == 'changePassword'):
            msg = EmailBuilder.change_password(obj)
            email_message = EmailMessage(details.subject, msg, details.frm, details.to)
            email_message.content_subtype = 'plain'
            try:
                email_message.send()
            except Exception as e:
                raise Exception(e)

        else:
            return None

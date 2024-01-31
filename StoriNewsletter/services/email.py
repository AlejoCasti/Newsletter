import os
from datetime import datetime
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string, get_template
import os
import ssl
# import resend

# Just for dev
ssl._create_default_https_context = ssl._create_unverified_context
# resend.api_key = os.environ["RESEND_API_KEY"]

MIME_TYPE = {
    'pdf': 'application/pdf',
    'png': 'image/png',
}


class EmailService:
    @staticmethod
    def send_email(
        *,
        file,
        attachment_file_name,
        emails: str,
        email_template_name: str,
        email_params: dict,
        title: str = 'Newsletter',
    ):
        now = datetime.now()
        current_day = now.strftime('%B %d, %Y')
        file_type = attachment_file_name.split('.')[1]

        template = get_template(f'{email_template_name}.html')
        html_content = template.render(email_params)

        email = EmailMessage(
            subject=title,
            from_email='acastiblancop16@gmail.com',
            to=emails,
            attachments=[(f'{title} - {current_day}', file, MIME_TYPE.get(file_type))],
        )
        email.content_subtype = 'html'
        email.body = html_content

        email.send()


import os

from services.jwt import JwtService
import urllib.parse

UNSUBSCRIBE_ROUTE = 'unsubscribe'


class Utils:
    @staticmethod
    def build_link(email, newsletter_id=None):
        token = JwtService.encode(
            email=email,
            newsletter_id=newsletter_id,
        )

        url = urllib.parse.urljoin(os.environ['FRONT_BASE_URL'], UNSUBSCRIBE_ROUTE)
        return f'{url}/{token}'

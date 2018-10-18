import os

import jinja2
import webapp2
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates')
)


class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        # If user exists, show logout and get user email
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
            user_email = user.email()
        # If user does not exist, create login and create a default to ensure checks work.
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
            user_email = 'none@none.com'

        template_values = {
            'page_a': True,
            'user': user,
            'user_email': user_email,
            'url': url,
            'url_linktext': url_linktext
        }

        template = jinja_environment.get_template('index.html', template_values)
        self.response.out.write(template.render(template_values))

    # def post(self):
        # if self.request.get('action') == 'checkpaperwork':
            # vfrvis = self.request.get('vfrvis')




app = webapp2.WSGIApplication(
    [
        ('/', MainPage),
    ],
    debug=True)

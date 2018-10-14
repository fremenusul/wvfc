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

        template_values = {
            'page_a': True,
            'user': user,
        }

        template = jinja_environment.get_template('index.html', template_values)
        self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication(
    [
        ('/', MainPage),
    ],
    debug=True)

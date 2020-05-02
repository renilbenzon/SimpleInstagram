import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from models.users_model import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class InstagramList(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()
        template_values = {}
        if user:
            url = users.create_logout_url('/')
            url_string = 'logout'
        else:
            self.redirect(users.create_login_url('/'))
            return

        instagrams, nextCursor, more = User.query().fetch_page(PAGE_SIZE)
        template_values = {
            'url': url,
            'url_string': url_string,
            'user': user,
            'newevs': newevs
        }
        template = JINJA_ENVIRONMENT.get_template('instagrampost.html')
        self.response.write(template.render(template_values))

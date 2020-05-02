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

        instagrams, nextCursor, more = User.query().fetch_page(PAGE_SIZE)
        template_values = {
            'url': url,
            'url_string': url_string,
            'user': user,
            'users': users
        }
        template = JINJA_ENVIRONMENT.get_template('instagrampost.html')
        self.response.write(template.render(template_values))

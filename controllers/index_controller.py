from google.appengine.ext import ndb
from main import Controller
from google.appengine.api import images

class Index(Controller):

    """Home Page"""

    def get(self):
        instagrams = ndb.gql("SELECT * FROM Instagram ORDER BY created DESC")
        self.render('instagram.html', instagrams=instagrams)

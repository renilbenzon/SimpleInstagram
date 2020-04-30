from google.appengine.ext import ndb
from users_model import User
from google.appengine.api import images

def instagram_key(name='default'):

    """Assign a key to Instagram"""

    return ndb.Key('instagrams', name)


class Instagram(ndb.Model):

    """Instagram's Info"""

    author = ndb.StructuredProperty(User)
    content = ndb.TextProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    like = ndb.IntegerProperty(default=0)
    subject = ndb.StringProperty(required=True)
    

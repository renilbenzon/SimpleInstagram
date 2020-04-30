from google.appengine.ext import ndb
from users_model import User


class Likes(ndb.Model):

    """Like's Info"""

    instagram_id = ndb.IntegerProperty(required=True)
    author = ndb.StructuredProperty(User)

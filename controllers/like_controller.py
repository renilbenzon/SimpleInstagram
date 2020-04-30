import time

from models.instagram_model import Instagram
from main import Controller
from models.likes_model import Likes
from google.appengine.ext import ndb


class Like(Controller):

    """Like A Post"""

    def get(self, instagram_id):
        pass

    def post(self, instagram_id):
        key = int(instagram_id)
        post = Instagram.get_by_id(key)

        if post and self.user:
            post.like += 1
            like = Likes(instagram_id=key, author=self.user)
            like.put()
            post.put()
            time.sleep(0.2)
            self.redirect('/%s' % key)
        else:
            self.redirect('/login')


class Unlike(Controller):

    """Unlike A Post"""

    def get(self, instagram_id):
        pass

    def post(self, instagram_id):
        key = int(instagram_id)
        post = Instagram.get_by_id(key)

        if post and self.user:
            post.like -= 1
            like = Likes(instagram_id=key, author=self.user)
            like.put()
            post.put()
            time.sleep(0.2)
            self.redirect('/%s' % key)
        else:
            self.redirect('/login')

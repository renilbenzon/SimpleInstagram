import time

from main import Controller
from models.comments_model import Comments
from models.users_model import *
from google.appengine.api import images

class DeleteComment(Controller):

    """Delete Comment"""

    def get(self, comment_id):
        pass

    def post(self, comment_id):
        key = int(comment_id)
        c = Comments.get_by_id(key)
        instagram_id = int(c.instagram_id)

        if self.user.name == c.author.name:
            c.key.delete()
            time.sleep(0.1)

        self.redirect('/%s' % instagram_id)


class EditComment(Controller):

    """Edit Comment"""

    def get(self, comment_id):
        key = int(comment_id)
        c = Comments.get_by_id(key)

        if self.user:
            self.render('edit-comment.html',
                        content=c.content, instagram_id=c.instagram_id)
        else:
            self.redirect('/%s' % c.instagram_id)

    def post(self, comment_id):
        key = int(comment_id)
        c = Comments.get_by_id(key)
        content = self.request.get('content')

        if content:
            if self.user.name == c.author.name:
                c.content = content  # update the comment's content
                c.put()
                time.sleep(0.1)

        self.redirect('/%s' % c.instagram_id)


class NewComment(Controller):

    """New Comment"""

    def get(self, instagram_id):
        pass

    def post(self, instagram_id):
        instagram_id = int(instagram_id)
        content = self.request.get('content')

        # new comment have content,
        # the current user, and the instagram_id
        if self.user and content:
            c = Comments(content=content,
                         author=self.user,
                         instagram_id=instagram_id)
            c.put()
            time.sleep(0.1)

        self.redirect('/%s' % instagram_id)

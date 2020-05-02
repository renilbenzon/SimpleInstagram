import time

from main import Controller
from models.instagram_model import Instagram
from models.comments_model import Comments
from google.appengine.ext import ndb
from models.users_model import User
from account_controller import *
class NewPost(Controller):

    """ New Post Page """

    def get(self):
        if self.user:
            self.render('newpost.html')
        else:
            self.redirect('/login')

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if self.user and subject and content :
            b = Instagram(subject=subject,
                     content=content,

                     author=self.user,
                     uname=self.user)
            b.put()
            time.sleep(0.1)  # sleep is used due to lag time
            self.redirect('/%d' % b.key.id())  # redirect to permalink
        else:
            self.render('newpost.html', subject=subject, content=content)


class Permalink(Controller):

    """Permalink's Page for a Instagram Post"""

    def get(self, instagram_id):
        instagram_key = Instagram.get_by_id(int(instagram_id))
        comment_key = Comments.gql("WHERE instagram_id = %s "
                                   "ORDER BY created DESC" % int(instagram_id))

        # render the instagram object and all of it's comment
        self.render("instagrampost.html", instagrams=[instagram_key], comments=comment_key)


class DeletePost(Permalink):

    """Delete a Instagram Post"""

    def get(self, instagram_id):
        pass

    def post(self, instagram_id):
        key = int(instagram_id)  # get id and turns into integer
        post = Instagram.get_by_id(key)  # use id to fine the instagram post item

        if self.user.name == post.author.name:
            post.key.delete()  # delete the found item
            time.sleep(0.1)  # sleep is used because of replication lag time

        self.redirect('/')  # redirect to home


class EditPost(Permalink):

    """Edit a Instagram Post's Page"""

    def get(self, instagram_id):
        key = Instagram.get_by_id(int(instagram_id))

        if self.user:
            # rendering the instagram post using instagram_id
            self.render("editpost.html", instagrams=[key])
        else:
            self.redirect("/login")

    def post(self, instagram_id):
        key = int(instagram_id)
        post = Instagram.get_by_id(key)
        subject = self.request.get('subject')
        content = self.request.get('content')

        # current user.name has to match
        # with author's name
        if self.user.name == post.author.name:
            if subject and content:
                post.subject = subject  # updating the subject
                post.content = content  # updating the content

                post.put()
                time.sleep(0.1)
                self.redirect('/%s' % key)  # redirect to the instagram post
            else:
                msg = "Something went wrong. Please try again."
                self.render("editpost.html", instagrams=[key], error_message=msg)
        else:
            self.redirect('/login')

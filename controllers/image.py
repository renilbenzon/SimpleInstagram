import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from blobcollection import BlobCollection
from uploadhandler import UploadHandler
from downloadhandler import DownloadHandler


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        collection_key = ndb.Key('BlobCollection', 1)
        collection = collection_key.get()
        if collection == None:
            collection = BlobCollection(id=1)
            collection.put()

        template_values = {
            'collection' : collection,
            'upload_url' : blobstore.create_upload_url('/upload'),
        }
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))

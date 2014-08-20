# Our example webserver

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from main_page import main_page
from test_page import test_page

class MainPage(webapp.RequestHandler):
 
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(main_page())

class TestPage(webapp.RequestHandler):
 
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write(test_page())


# This is where the running code starts

application = webapp.WSGIApplication([
      ('/', MainPage),
      ('/test', TestPage)
    ], debug=True)

def main():
  run_wsgi_app(application)
 
if __name__ == "__main__":
  main()
# Chris Merrill
# CS496
# 1/9/2018
# Prints Current Time to a GAE Application

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("Hello!")

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

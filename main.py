# Chris Merrill
# CS496
# 1/9/2018
# Prints Current Time to a GAE Application

import webapp2
import time

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        localtime = time.asctime(time.localtime(time.time()))
        self.response.write("Local current time :", localtime)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

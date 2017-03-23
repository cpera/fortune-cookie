#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
	fortuneCookiesList = ["You're going to learn much more at LaunchCode", "You will hear a surprise news in next few days", "You better try one more time!"]
	index = random.randint(0,2)
	return fortuneCookiesList[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
		headerTag = "<h1> Fortune Cookie</h1>"
		fortune = "<strong>" + getRandomFortune() + "</strong>"
		fortuneString = "Your fortune: " + fortune
		fortuneParagraph = "<p>" + fortuneString + "</p>"
		lucky_number = "<strong>" + str(random.randint(1, 999)) + "</strong>"
		numberString = 'Your lucky number is: ' + lucky_number
		numberParagraph = "<p>" + numberString + "</p>"
		cookiesAgainBtn = "<a href='.'> <button> Another cookie plz! </button> </a>"
		content = headerTag + fortuneParagraph + numberParagraph + cookiesAgainBtn
		self.response.write(content)

class LoginHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write("Trying to login")

routes = 	[ ('/', MainHandler), ('/login', LoginHandler) ]	

app = webapp2.WSGIApplication(routes, debug=True)

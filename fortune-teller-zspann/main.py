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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
class TimeHandler(webapp2.RequestHandler):
    def get(self):
        i = 1
        self.response.write("You've visited this page " + str(i) + " times.")
        i += 1
class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        i = random.randint(0, 4)
        fortune_list = ["You will develop great skills.", "You will accomplish great but terrible things.", "You will encounter great people.", "You will destroy the entire world.", "You will be left entirely alone."]
        self.response.write(fortune_list[random.randint(0, len(fortune_list))])

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/timesaver', TimeHandler),
    ('/fortune', FortuneHandler)
], debug=True)

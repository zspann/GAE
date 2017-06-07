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
import jinja2
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
class FormHandler(webapp2.RequestHandler):
    def get(self):
        fortune_form = JINJA_ENVIRONMENT.get_template("templates/form.html")
        self.response.write(fortune_form.render())
class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        name = "Zack"
        location = "Seattle"
        f_list = [" will be left forever alone.", " will find everlasting love.", " will be lost to the end of time.", " will always be around people.", " will never leave the house."]
        fortune = f_list[random.randint(0, len(f_list)-1)]
        fortune_response = JINJA_ENVIRONMENT.get_template("templates/fortune.html")
        self.response.write(fortune_response.render({
        "form_name" : name,
        "form_location" : location,
        "random_fortune" : fortune,
        }))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/form', FormHandler),
    ('/fortune', FortuneHandler)
], debug=True)

'''_

Let's create a simple web application framework. We'll need view
classes for each page on the site:

>>> home_view = HomePageView()
>>> home_view.render()
'<html><body>Welcome!</body></html>'
>>> home_view.body
'Welcome!'

>>> about_view = AboutPageView()
>>> about_view.render()
'<html><body>This is a simple website about nutrition.</body></html>'

To route URLs to views, we'll create a global webapp object.

>>> app = WebApp()

It will keep track of the mappings with a protected variable:

>>> type(app._routes)
<class 'dict'>

Routings - that is, a mapping from a URL to a view object - are
created with add_route(). Then you can get and render the view with
get().

>>> app.add_route("/", home_view)
>>> app.add_route("/about/", about_view)
>>> app.get("/")
'<html><body>Welcome!</body></html>'
>>> app.get("/about/")
'<html><body>This is a simple website about nutrition.</body></html>'

Let's create some more views. This site has two kinds of endpoints:
HTML pages, for browser content, and JSON objects, for API access.

>>> class ContactView(HTMLView):
...     body = 'Get in touch at hello@example.com'
...
>>> app.add_route("/contact/", ContactView())
>>> app.get("/contact/")
'<html><body>Get in touch at hello@example.com</body></html>'

(Hint for the JSON endpoints: One of the functions in the json module
takes an option to sort object keys.)

>>> class CarrotInfoView(JSONView):
...     def data(self):
...         return {
...             'serving_size': 61,
...             'fat': 0.1,
...             'calories': 25,
...             'protein': 0.6,
...             }

>>> carrot_view = CarrotInfoView()
>>> carrot_view.render()
'{"calories": 25, "fat": 0.1, "protein": 0.6, "serving_size": 61}'
>>> app.add_route("/api/carrot/", carrot_view)

Create a view for baked chicken nutritional info:

>>> app.add_route("/api/chicken/", ChickenInfoView())
>>> app.get("/api/chicken/")
'{"calories": 231, "fat": 5, "protein": 43, "serving_size": 140}'

And let's add a helper to give us a sorted list of all URLs defined so far.

>>> app.urls()
['/', '/about/', '/api/carrot/', '/api/chicken/', '/contact/']

It's important to keep your class hierarchies well-organized. Since
every view has a render() method, it makes sense to put that in a
common base class.

>>> type(View.render)
<class 'function'>

>>> isinstance(home_view, View)
True
>>> issubclass(ChickenInfoView, View)
True

And we can have more specialized views, FOR EXAMPLE WHEN WE WANT TO
OUR WRITING TO MAKE AN IMPACT:

>>> class LegalView(ShoutingHTMLView):
...     body = 'you agree to our terms of service!'

>>> legal_view = LegalView()
>>> app.add_route("/legal/", legal_view)
>>> app.get("/legal/")
'<HTML><BODY>YOU AGREE TO OUR TERMS OF SERVICE!</BODY></HTML>'
>>> isinstance(legal_view, HTMLView)
True

Python lets you do something called "monkey patching".  It can lead to
hard-to-understand code, so don't overuse it. But it can be useful
when working with certain libraries whose source you cannot/do not
want to modify, for example.

The idea is you modify a method of an already-created object, or a
superclass deep in an inheritance hierarchy, by assigning to it
directly. It works because in Python, (a) everything is an object, and
(b) methods are just attributes that can be assigned to.

>>> original_htmlview_render = HTMLView.render
>>> def new_htmlview_render(self):
...     # Add <p> tag around content
...     return '<html><body><p>' + self.body + '<p></body></html>'
>>> HTMLView.render = new_htmlview_render

Now that HTMLView is modified, instances of its subclasses are
modified too - provided that subclass reuses that method defined in
the superclass:

>>> legal_view.render()
'<HTML><BODY><P>YOU AGREE TO OUR TERMS OF SERVICE!<P></BODY></HTML>'

'''

# Write your code here:
import abc
import json

class WebApp:
    def __init__(self):
        self._routes = {}
    def add_route(self, url, view):
        self._routes[url] = view
    def get(self, url):
        view = self._routes[url]
        return view.render()
    def urls(self):
        return sorted(self._routes.keys())

class View(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self):
        pass

class HTMLView(View):
    body: str
    def render(self):
        return '<html><body>' + self.body + '</body></html>'

class ShoutingHTMLView(HTMLView):
    def render(self):
        return super().render().upper()

class JSONView(View):
    @abc.abstractmethod
    def data(self):
        pass
    def render(self):
        return json.dumps(self.data(), sort_keys=True)
    
class HomePageView(HTMLView):
    body = 'Welcome!'

class AboutPageView(HTMLView):
    body = 'This is a simple website about nutrition.'

class ChickenInfoView(JSONView):
    def data(self):
        return {
            'serving_size': 140,
            'fat': 5,
            'calories': 231,
            'protein': 43,
            }


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.

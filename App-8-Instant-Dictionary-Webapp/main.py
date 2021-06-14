import justpy as jp
from webapp import page
import inspect
from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary

imports = list(globals().values())

for key in imports:
    if inspect.isclass(key):
        if issubclass(key, page.Page) and key is not page.Page:
            jp.Route(key.path, key.serve)

# jp.Route(Home.PATH, Home.serve)
# jp.Route(About.PATH, About.serve)
# jp.Route(Dictionary.PATH, Dictionary.serve)
jp.justpy(port=8001)
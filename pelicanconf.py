AUTHOR = 'Plasma'
SITENAME = 'Plasma Hut'
SITEURL = "https://Ale-Pedroni.github.io"
SITESUBTITLE = 'A minimalist brutalist website with Ugandan flag-inspired colors'
FEED_DOMAIN = SITEURL

PATH = "content"
OUTPUT_PATH = 'output'
THEME_STATIC_DIR = 'theme'
THEME = 'uganda_theme'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'En'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/Ale-Pedroni"),
    ("Another social link", "#"),
)

# Custom Menu Items
MENUITEMS = (
    ('About', '/pages/about.html'),
    ('Contact', '/pages/contact.html'),
)

# Pagination
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Display categories on menu and homepage
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_CATEGORIES_ON_HOMEPAGE = True

# Display pages on menu
DISPLAY_PAGES_ON_MENU = True

# Enable Jinja2 extensions
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.loopcontrols', 'jinja2.ext.do']}

# Custom settings for the theme
import datetime
CURRENTYEAR = datetime.date.today().year 
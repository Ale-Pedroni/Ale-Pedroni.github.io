AUTHOR = 'Plasma'
SITENAME = 'Il mio blog'
SITEURL = "https://Ale-Pedroni.github.io"
SITESUBTITLE = 'A blog about everything and nothing'
FEED_DOMAIN = SITEURL

PATH = "content"
OUTPUT_PATH = 'output'
STATIC_PATHS = ['static']
THEME_STATIC_DIR = 'static'
THEME = 'kev_quirk'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'En'

TYPOGRIFY = False

GITHUB_URL = "https://github.com/Ale-Pedroni"

# category URL
CATEGORY_URL = 'category/{slug}/index.html'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# article URL
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

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
    ("instagram", "https://www.instagram.com/pedro_zixuan/"),
)

# Custom Menu Items
#MENUITEMS = (
#    ('About', '/pages/about.html'),
#    ('Contact', '/pages/contact.html'),
#)

# Pagination
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),  # First page
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),  # Subsequent pages
)
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Display categories on menu and homepage
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_HOMEPAGE = True

# Display pages on menu
DISPLAY_PAGES_ON_MENU = True

# Enable Jinja2 extensions
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.loopcontrols', 'jinja2.ext.do']}

# Custom settings for the theme
import datetime
CURRENTYEAR = datetime.date.today().year

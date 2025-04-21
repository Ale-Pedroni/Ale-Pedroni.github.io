# Ugandan Brutalist Theme for Pelican

A minimalist brutalist theme for Pelican static site generator, inspired by the colors of the Ugandan flag.

## Color Palette

### Primary Colors (directly from the flag)
* Black: `#000000`
* Yellow/Gold: `#FCDC04`
* Red: `#D90000`

### Extended Palette
* Deep Maroon: `#8C0303` (darker shade of the flag's red)
* Light Gold: `#FFE866` (lighter version of the flag's yellow)
* Dark Charcoal: `#333333` (softer black for text)
* Off-White: `#F5F5F5` (for backgrounds and contrast)
* Forest Green: `#006633` (representing Uganda's lush landscapes)

## Installation

1. Clone this repository to your Pelican themes directory:
   ```bash
   git clone https://github.com/yourusername/ugandan-brutalist-theme.git
   ```

2. Add the theme to your `pelicanconf.py`:
   ```python
   THEME = 'path/to/ugandan-brutalist-theme'
   ```

## Features

- Brutalist/minimalist design philosophy
- Responsive layout
- Clean typography focused on readability
- Ugandan flag-inspired color scheme
- Support for categories and tags
- Pagination for article listings
- Mobile-friendly navigation

## Configuration

Add these settings to your `pelicanconf.py` to customize the theme:

```python
# Display categories on menu and homepage
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_CATEGORIES_ON_HOMEPAGE = True

# Display pages on menu
DISPLAY_PAGES_ON_MENU = True

# Current year for footer copyright
CURRENTYEAR = 2025  # Update this each year
```

## Typography

The theme uses:
- 'Courier New' monospace font for body text
- 'Arial Black'/Helvetica for headings

## License

MIT License

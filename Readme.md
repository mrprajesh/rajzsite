# Main Webpage
This is my CSE@IITM homepage content generated using pelican.

## Usage
Generate html webpage from the markdown(md) files.

```make html```

Runs the server. Open http://localhost:8000/ to see the rendering.

```make serve```

Once the development is done. We are ready for deploying.

```
$make publish
$pelican content -s publishconf.py
$make rsync_upload
```


# Pages
The pages contains the static pages.
- About me
- Education
- Research
- Tools
- Contact
- Learning Curve
- News

# Articles
This has two group dynamic pages sorted in chronological order.
- Learning curve
- News

# Some Workarounds done
The about page is made a the index page. Using. 
```
url: 
save_as: index.html
```
The page order is enforced using page-order for pages
```
PAGE_ORDER_BY = 'page-order' in config file
```
The plugin render math using in config file
```
PLUGIN_PATHS = ['/home/rajz/install/pelican-plugins']
PLUGINS = ["render_math"]
```

# Main Webpage
This is my CSE @ IIT Madras [homepage](http://www.cse.iitm.ac.in/~mrprajesh/) content generated using pelican. 

## TODO
- [ ] Can you add code highlighter
	- [ ] with line numbers
	- [ ] with terminal like code block
- [x] How to create pandoc style hyperlinks/ id links/header id/anchor links 	
- [ ] can I change Dark vs light on your theme?


## Usage
Generate html webpage from the markdown(md) files.

```make html```

Runs the server. Open http://localhost:8000/ to see the rendering.

```make serve```

or use
``` make devserver ```

Once the development is done. We are ready for deploying.

```
$ make publish
$ make rsync_upload # or make dropbox_upload or copy htmls to gh-pages
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
The about page is made as the index page. Using:
```
url: 
save_as: index.html
```
The page order is enforced using page-order for pages.
```
PAGE_ORDER_BY = 'page-order' in config file
```
The plugin render math used in config file to generate LaTeX support.
```
PLUGIN_PATHS = ['/home/rajz/install/pelican-plugins']
PLUGINS = ["render_math"]
```

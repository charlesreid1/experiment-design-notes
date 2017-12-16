# experimental-design

Notes on experimental design.


<br />
<br />


## HTML Pages and Notebooks

The main output of the repository consists of HTML pages 
and Jupyter notebooks containing lecture notes and
example problems on various experimental design topics. 

**Link:** [http://charlesreid1.github.io/experiment-design](http://charlesreid1.github.io/experiment-design)

To generate these, use Pelican (see next section).


<br />
<br />


## Pelican Source Code

The source code for creating the HTMl and Jupyter notebooks
is organized as follows:

* Pelican is the Python module used to turn raw content into web content
    * `pelicanconf.py` is the main Pelican "Makefile"
    * `content/` directory will contain any pelican content

* Raw content in `content/` is turned into static web content in `docs`
    * Use `pelican content` command

* Jupyter notebooks are converted to HTML and added to `docs`
    * Jupyter nbconvert commands should be called by `pelicanconf.py`

* Static content in `docs` is hosted on Github Pages 
    **Link:** [http://charlesreid1.github.io/experiment-design](http://charlesreid1.github.io/experiment-design)


### Configuration file:

The Pelican configuration file is `pelicanconf.py`.

### Raw Content: 

Pelican turns raw content (markdown, HTML-like Jinja templates)
into static HTML content.

The default location for Pelican content is `content/`. 
This is where it looks for markdown files to turn into static content.
You can add more locations by adding to the list `EXTRA_TEMPLATE_PATHS`
in `pelicanconf.py`.

Markdown files in `content/` will be rendered as blog posts. 
This is problematic if there is no support for blog stuff, 
as with the theme we are using,

Markdown files in `content/pages/` will be rendered as static 
HTML pages. Easy peasy. 

### Theme:

The basic template files are contained in the theme folder.
To add your own templates to customize the theme, add more paths
containing templates to the `EXTRA_TEMPLATES_PATHS` list 
in `pelicanconf.py`.

Also explicitly add HTML template pages like this:

```
TEMPLATE_PAGES['mypage.html'] = 'mypage.html'
TEMPLATE_PAGES['custompath.html'] = 'custom/path/custompath.html'
```

### Splash/Landing Page:

The splash/landing page is in `content/pages/splash.md` and is converted
into the destination file `index.html` (via directives in the markdown file).
To modify the splash/startup page, just modify this Markdown file.

More complicated configurations can be achieved by setting values for 
custom variables in the header of the Markdown file, and accessing those
variable values in the theme's templates.



# experimental-design

Notes on experimental design.

## HTML Pages and Notebooks

The main output of the repository consists of HTML pages 
and Jupyter notebooks containing lecture notes and
example problems on various experimental design topics. 

**Link:** [http://charlesreid1.github.io/experiment-design]

## Source Code

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
    * Link: [http://charlesreid1.github.io/experiment-design]

# Installation

If you want to get the exact setup I have run
```bash
configure_notebooks.sh
```
it will get create an virtualenv install and configure all extensions, widgets and skin you
can see in the presentation.
If you want to change it go ahead!

# Presentation
To open the presentation just run
```bash
jupyter nbconvert --to slides presentation.ipynb --post serve
```
and click on the link to localhost that it shows you.

# Useful stuff
Go to resources and check :
- `deepsensify.css` if you want to write your own skin
- `microscope.html` to see how you can use html within your notebooks
- `plot_dir.py` for you own custom magic

# Resources
- https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/
- http://catherinedevlin.blogspot.com/2013/07/ipython-helloworld-magic.html

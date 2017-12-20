from IPython.display import HTML

def plot_html_microscope(img_filepath):
    with open("resources/microscope.html") as f:
        style_html = f.read()
    image_html = """<div class="magnify">
<div class="large"></div>
<img class="small" src="{}" width="200"/>
</div>
    """.format(img_filepath)
    
    html = style_html + "\n\n" + image_html
    display(HTML(html))
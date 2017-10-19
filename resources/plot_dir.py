import os, glob
import matplotlib.pyplot as plt
from IPython.core.magic import Magics, magics_class, line_magic, cell_magic

@magics_class
class PlotDirMagic(Magics):
    @line_magic('snapshot')
    def plot_dir(self, line='', cell=''):  
        path, nr = line.split(' ')
        dir_path = os.path.join(os.getcwd(), path)
        filepaths = glob.glob('{}/*'.format(dir_path))
        
        fig, axes = plt.subplots(1, int(nr), figsize=(16,12));
        for ax,filepath in zip(axes, filepaths):
            img = plt.imread(filepath)
            ax.imshow(img);
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
       
def load_ipython_extension(ip):
    ip.register_magics(PlotDirMagic)
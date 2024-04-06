"""
Fichero dedicado a la definicion de funciones auxiliares que 
puedan ser utilizadas en los Jupyter Notebooks donde se lleva a cabo
el Analisis Exploratorio de datos del proyecto.

Las funciones definidas en este fichero tratan, entonces, de mantener limpios
los notebooks escritos, puesto que todo el codigo se define dentro de este
fichero.
"""

## IMPORTS -----
import matplotlib.pyplot as plt
import seaborn as sns
import os

def line_plot(X, y, x_label = None, y_label = None, title = None, img_route = None, image_name = None):
    
    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    
    ax.plot(X, y, linewidth = 2.0)
    
    if x_label and y_label:
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        
    
    if img_route:
        plt.savefig(os.path.join(img_route, image_name))  # Guardo la imagen en el directorio especificado
    if title:
        plt.title(title)
    plt.show()

def scatter_plot(X, y, x_label = None, y_label = None, title = None, sizes = None, colors = None, img_route = None, image_name = None):
    
    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    
    if sizes:
        ax.scatter(X, y, s=sizes, c=colors, vmin=0, vmax=100)
    else:
        ax.scatter(X, y, c=colors, vmin=0, vmax=100)
    if x_label and y_label:
        plt.xlabel(x_label)
        plt.ylabel(y_label)
    
    if img_route:
        plt.savefig(os.path.join(img_route, image_name))  # Guardo la imagen en el directorio especificado
    if title:
        plt.title(title)
    plt.show()

def pie_plot(X, y, colors = None, title = None, img_route = None, image_name = None):
    
    plt.style.use('_mpl-gallery-nogrid')
    fig, ax = plt.subplots()
    
    ax.pie(X, colors=colors, radius=3, center=(4, 4),
            wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

    if img_route:
        plt.savefig(os.path.join(img_route, image_name))  # Guardo la imagen en el directorio especificado
    if title:
        plt.title(title)
    plt.show()
    
def box_plot(X, y, x_label = None, y_label = None, title = None, img_route = None, image_name = None):
    
    plt.style.use('_mpl-gallery')
    
    fig, ax = plt.subplots()

    ax.bar(X, y, width=1, edgecolor="white", linewidth=0.7)
    if x_label and y_label:
        plt.xlabel(x_label)
        plt.ylabel(y_label)
    
    if img_route:
        plt.savefig(os.path.join(img_route, image_name))  # Guardo la imagen en el directorio especificado
        
    if title:
        plt.title(title)    
    plt.show()

def violin_plot(dataset, x_label = None, y_label = None, title = None, img_route = None, image_name = None):
    
    plt.style.use('_mpl-gallery')
    
    fig, ax = plt.subplots()
    
    vp = ax.violinplot(dataset, widths=2,
                       showmeans=False, showmedians=False, showextrema=False)
    # styling:
    for body in vp['bodies']:
        body.set_alpha(0.9)
        
    if x_label and y_label:
        plt.xlabel(x_label)
        plt.ylabel(y_label)

    if img_route:
        plt.savefig(os.path.join(img_route, image_name))  # Guardo la imagen en el directorio especificado
        
    if title:
        plt.title(title)
    plt.show()


def hist_distrib(X, x_label = None, y_label = None, title = None, img_route = None, image_name = None):
    
    plt.style.use('_mpl-gallery')
    
    fig, ax = plt.subplots()
    
    ax.hist(X, bins=8, linewidth=0.5, edgecolor="white")
    if x_label and y_label:
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        
        
    if img_route:
        plt.savefig(os.path.join(img_route, image_name))  # Guardo la imagen en el directorio especificado
        
    if title:
        plt.title(title)
    plt.show()
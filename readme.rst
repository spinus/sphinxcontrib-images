Sphinx "fancybox" extension.

Fancybox
========

Fancybox is adaptation of `<http://fancybox.net/>`_ in version **1.3.4**.

Installation
------------

Instalation through pip: ::

    pip install sphinxcontrib-fancybox

or through github: ::

    git clone https://github.com/spinus/sphinxcontrib-fancybox
    cd sphinxcontrib-fancybox
    python setup.py install

Next, you have to add extension to `conf.py` in your sphinx project. ::

    extensions = [
              ...,
              'sphinxcontrib.fancybox',  
              ...]


Directives
----------

fancybox:
    
    Fancybox directive place a thumbnail of picture you selected, and add some
    `fancies`. If you click on image you get fullscreen box with that picture.

    Example: ::

        .. fancybox:: picture.png

    By default all images on one page are in the same group (you can navigate
    pressing `next` and `prev` buttons around this group).
    If you want to add picture to another group you have to set `group` 
    parameter, like: ::

        .. fancybox:: picture.png
            :group: group2


TODO
----

* fallback for non html output
* width and height parameters (currently the thumbnail is set to 100x100px)
* get default thumbnail size from config


Questions and suggestions
-------------------------

If you have some suggstions, patches, problems - please write an email or 
github message.


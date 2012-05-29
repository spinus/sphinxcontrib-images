# -*- coding: utf-8 -*-
__version__ = '0.3.1'
__author__ = 'Tomek Czyż <tomekczyz@gmail.com>'
__license__ = "BSD"


import os
import re
from docutils.parsers.rst import roles, directives
from docutils import nodes, utils
from sphinx.environment import NoUri
from sphinx.locale import _
from sphinx.util.compat import Directive, make_admonition
from sphinx.util.osutil import copyfile
import posixpath
import json

# Have no better idea how to include it at the end of the document.
# Used to use 'build-resolved' signal, but if I want to add a Text node
# (dont know which more I can use), the text is encoded in html not just
# pasted.
#
# Please send a patch if you know how to do it.
js = r'''
<script type="text/javascript">
    $(document).ready(function() {
        $("a.fancybox").fancybox(%s);
    });
</script>
'''

CSS_FILES = (
    'fancybox/jquery.fancybox-1.3.4.css',
)
JS_FILES = (
    'fancybox/jquery.fancybox-1.3.4.pack.js',
)
IMG_FILES = (
    'fancybox/blank.gif',
    'fancybox/fancybox.png',
    'fancybox/fancybox-x.png',
    'fancybox/fancybox-y.png',
    'fancybox/fancy_close.png',
    'fancybox/fancy_loading.png',
    'fancybox/fancy_nav_left.png',
    'fancybox/fancy_nav_right.png',
    'fancybox/fancy_shadow_e.png',
    'fancybox/fancy_shadow_ne.png',
    'fancybox/fancy_shadow_n.png',
    'fancybox/fancy_shadow_nw.png',
    'fancybox/fancy_shadow_se.png',
    'fancybox/fancy_shadow_s.png',
    'fancybox/fancy_shadow_sw.png',
    'fancybox/fancy_shadow_w.png',
    'fancybox/fancy_title_left.png',
    'fancybox/fancy_title_main.png',
    'fancybox/fancy_title_over.png',
    'fancybox/fancy_title_right.png',
)


class fancybox_node(nodes.image, nodes.General, nodes.Element):
    pass


class FancyboxDirective(Directive):
    has_content = True
    required_arguments = 1
    option_spec = {
        'group': unicode,
        'class': unicode,  # directives.class_option,
        'alt': unicode,

        'width': directives.length_or_percentage_or_unitless,
        'height': directives.length_or_unitless,
    }

    def run(self):
        env = self.state.document.settings.env

        group = self.options.get('group', 'default')

        width = self.options.get('width',
                                 env.app.config.fancybox_thumbnail_width)
        height = self.options.get('height',
                                  env.app.config.fancybox_thumbnail_height)
        cls = self.options.get('class',
                                  env.app.config.fancybox_thumbnail_class).\
                                    split(' ')
        alt = self.options.get('alt', '')

        # parse nested content
        #TODO: something is broken here, not parsed as expected
        description = nodes.paragraph()
        content = nodes.paragraph()
        content += [nodes.Text("%s" % x) for x in self.content]
        self.state.nested_parse(content,
                                0,
                                description)

        fb = fancybox_node()
        fb['group'] = group

        if env.app.config.fancybox_download_remote_images:
            #TODO: download to _images maybe as sha1 name?
            raise NotImplementedError('fancybox_download_remote_images '
                            'is not working yey, please contribute :)')
        else:
            # put link
            fb['uri'] = directives.uri(self.arguments[0])

        fb['content'] = description
        fb['size'] = (width, height)
        fb['classes'] += cls
        fb['alt'] = alt
        return [fb]


def visit_fancybox_node(self, node):
    # make links local (for local images only)
    if node['uri'] in self.builder.images:
        node['uri'] = posixpath.join(self.builder.imgpath,
                                   self.builder.images[node['uri']])

    self.body.append(
        self.starttag(
            node,
            'a',
            REL='%s' % node['group'],
            HREF=node['uri'],
            CLASS=' '.join(['fancybox'] + node['classes']),
            #TODO: nested parse not works at that moemnt
            TITLE=node['content'].astext(),
            ALT=node['alt'] or node['content'].astext(),
        ),
    )
    self.body.append(
        '<img src="%s" width="%s" height="%s" />' % (
                                                     node['uri'],
                                                     node['size'][0],
                                                     node['size'][1],
                                                    )
    )
    #TODO: handle it once, but where :)
    self.body.append(
        js % (json.dumps(self.builder.app.config.fancybox_config))
    )


def depart_fancybox_node(self, node):
    self.body.append('</a>')


def add_stylesheet(app):
    for FILE in CSS_FILES:
        app.add_stylesheet(FILE)


def add_javascript(app):
    for FILE in JS_FILES:
        app.add_javascript(FILE)


def copy_stylesheet(app, exception):
    if app.builder.name != 'html' or exception:
        return
    import os
    #TODO: change _static to variable from config (something like that exists?)
    path = os.path.abspath(os.path.join(app.builder.outdir,
                                        '_static',
                                        'fancybox')
                          )
    if not os.path.exists(path):
        os.makedirs(path)

    app.info('Copying fancybox stylesheets... ', nonl=True)
    for FILE in CSS_FILES:
        copyfile(
            os.path.join(os.path.dirname(__file__), FILE),
            os.path.join(app.builder.outdir, '_static', FILE)
        )
    app.info('done')
    app.info('Copying fancybox javascript... ', nonl=True)
    for FILE in JS_FILES:
        copyfile(
            os.path.join(os.path.dirname(__file__), FILE),
            os.path.join(app.builder.outdir, '_static', FILE)
        )
    app.info('done')
    app.info('Copying fancybox images... ', nonl=True)
    for FILE in IMG_FILES:
        copyfile(
            os.path.join(os.path.dirname(__file__), FILE),
            os.path.join(app.builder.outdir, '_static', FILE)
        )
    app.info('done')


'''
def add_javascript_code(app, doctree, fromdocname):
    #doctree[-1].append(js)
    pass
'''


def pass_node(self, node):
    pass


def setup(app):
    app.add_config_value('fancybox_thumbnail_width', '150px', 'env')
    app.add_config_value('fancybox_thumbnail_height', '150px', 'env')
    app.add_config_value('fancybox_thumbnail_class', '', 'env')
    app.add_config_value('fancybox_download_remote_images', False, 'env')
    app.add_config_value('fancybox_generate_thumbnails', False, 'env')
    app.add_config_value('fancybox_config', {}, 'env')
    app.add_node(fancybox_node,
                 html=(visit_fancybox_node, depart_fancybox_node),
                 latex=(pass_node, pass_node),
                 man=(pass_node, pass_node),
                 texinfo=(pass_node, pass_node),
                 text=(pass_node, pass_node),
    )

    app.add_directive('fancybox', FancyboxDirective)
    #app.connect('doctree-resolved', add_javascript_code)

    app.connect('builder-inited', add_stylesheet)
    app.connect('builder-inited', add_javascript)
    app.connect('build-finished', copy_stylesheet)

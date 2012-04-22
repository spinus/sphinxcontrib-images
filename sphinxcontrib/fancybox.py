# -*- coding: utf-8 -*-
import os
import re
from docutils.parsers.rst import roles, directives
from docutils import nodes, utils
from sphinx.environment import NoUri
from sphinx.locale import _
from sphinx.util.compat import Directive, make_admonition
from sphinx.util.osutil import copyfile

# Have no better idea how to include it at the end of the document.
# Used to use 'build-resolved' signal, but if I want to add a Text node
# (dont know which more I can use), the text is encoded in html not just
# pasted.
#
# Please send a patch if you know how to do it.
js = r'''
<script type="text/javascript">
    $(document).ready(function() {
        $("a.fancybox").fancybox({
            'titlePosition' :   'outside',
            'transitionIn'  :   'elastic',
            'transitionOut' :   'elastic',
            'speedIn'       :   600,
            'speedOut'      :   200,
            'overlayShow'   :   true
        });
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


class fancybox_node(nodes.General, nodes.Element):
    pass


class FancyboxDirective(Directive):
    has_content = True
    required_arguments = 1
    option_spec = {
        'group': unicode,
        'class': unicode, #directives.class_option,

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
                                  env.app.config.fancybox_thumbnail_class)


        # parse nested content
        description = nodes.paragraph()
        content = nodes.paragraph()
        content += [ nodes.Text("%s"%x) for x in self.content]
        self.state.nested_parse(self.content, 
                                0,
                                description)

        lb = fancybox_node()
        lb.group = group
        lb.link = directives.uri(self.arguments[0])
        lb.content = description
        lb.size = (width, height)
        lb.classes = cls

        return [lb]


def visit_fancybox_node(self, node):
    self.body.append(self.starttag(node,
                                   'a',
                                   REL='%s' % node.group,
                                   HREF=node.link,
                                   CLASS='fancybox '+node.classes,
                                   # TODO: how render title as html but 
                                   # do tooltip like text only
                                   TITLE=node.content,
                                   ALT=node.content.astext(),
                                  ),
                    )
    self.body.append('<img src="%s" width="%s" height="%s" />' % (
                                                                  node.link, 
                                                                  node.size[0],
                                                                  node.size[1]
                                                                 )
                    )
    self.body.append(js)


def depart_fancybox_node(self, node):
    self.body.append('</a>')


def add_stylesheet(app):
    for FILE in CSS_FILES:
        app.add_stylesheet(FILE)
    for FILE in JS_FILES:
        app.add_javascript(FILE)


def copy_stylesheet(app, exception):
    if app.builder.name != 'html' or exception:
        return
    app.info('Copying fancybox stylesheets and js... ', nonl=True)
    import os
    path = os.path.abspath(os.path.join(app.builder.outdir,
                                        '_static',
                                        'fancybox')
                          )
    if not os.path.exists(path):
        os.makedirs(path)

    for FILE in CSS_FILES:
        copyfile(
            os.path.join(os.path.dirname(__file__), FILE),
            os.path.join(app.builder.outdir, '_static', FILE)
        )
    for FILE in JS_FILES:
        copyfile(
            os.path.join(os.path.dirname(__file__), FILE),
            os.path.join(app.builder.outdir, '_static', FILE)
        )
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


def setup(app):
    app.add_config_value('fancybox_thumbnail_width','150px','env')
    app.add_config_value('fancybox_thumbnail_height','150px','env')
    app.add_config_value('fancybox_thumbnail_class','','env')
    app.add_node(fancybox_node,
                 html=(visit_fancybox_node, depart_fancybox_node),
                 #latex=(visit_fancybox_node, depart_fancybox_node),
                 #text=(visit_fancybox_node, depart_fancybox_node),
                 #man=(visit_fancybox_node, depart_fancybox_node),
                 #texinfo=(visit_fancybox_node, depart_fancybox_node)
    )

    app.add_directive('fancybox', FancyboxDirective)
    #app.connect('doctree-resolved', add_javascript_code)

    app.connect('builder-inited', add_stylesheet)
    app.connect('build-finished', copy_stylesheet)

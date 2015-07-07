
import os
from sphinxcontrib import images

class LightBox2(images.Backend):
    STATIC_FILES = (
        'lightbox2/css/lightbox.css',
        'lightbox2/js/jquery-1.11.0.min.js',
        'lightbox2/js/lightbox.min.js',
        'lightbox2/js/lightbox.min.map',
        'lightbox2/img/close.png',
        'lightbox2/img/next.png',
        'lightbox2/img/prev.png',
        'lightbox2/img/loading.gif',
    )

    def visit_image_node_html(self, writer, node):
        # make links local (for local images only)
        builder = self._app.builder
        if node['uri'] in builder.images:
            node['uri'] = os.path.join(builder.imgpath,
                                       builder.images[node['uri']])

        writer.body.append(
            u'''<a data-lightbox="{group}"
                   href="{href}"
                   class="{cls}"
                   title="{title}"
                   data-title="{title}"
                   >'''.format(
                group='group-%s' % node['group'] if node['group'] else node['uri'],
                href=node['uri'],
                cls=' '.join(node['classes']),
                title=node['title'] + node['content'],
                ))
        writer.body.append(
            '''<img src="{src}"
                    class="{cls}"
                    width="{width}"
                    height="{height}"
                    alt="{alt}"/>
                    '''.format(src=node['uri'],
                               cls='align-%s' % node['align'] if node['align'] else '',
                               width=node['size'][0],
                               height=node['size'][1],
                               alt=node['alt'],
                               title=node['title']))


    def depart_image_node_html(self, writer, node):
        writer.body.append('</a>')

    def visit_image_node(self, writer, node):
        writer.visit_image(node)

    def depart_image_node(self, writer, node):
        writer.depart_image(node)

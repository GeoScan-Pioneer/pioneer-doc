from docutils import nodes, utils
from docutils.nodes import Body, Element
from docutils.parsers.rst import directives

from docutils.parsers.rst import Directive

from docutils.core import publish_parts
from rst2html5 import HTML5Writer

class platenode(Body, Element):
    pass

class PlateDirective(Directive):
    final_argument_whitespace = True

    option_spec = {
        'icon': directives.unchanged,
        'head': directives.unchanged,
        'caption': directives.unchanged
    }

    has_content = True
    add_index = True

    node_class = nodes.note

    def run(self):
        body = ''
        rst = ''

        for pos, line in enumerate(self.content):
            rst += line + '\n'

        body += publish_parts(writer=HTML5Writer(), source=rst)['body']

        node = platenode()
        node['content'] = body
        node['icon'] = self.options['icon']
        node['head'] = self.options['head']
        node['caption'] = self.options['caption']
        return [node]

    def html_platenode(self, node):
        template = """
        <div class="plate">
            <div class="image"> <img src="%(imgpath)s" alt="icon"> </div>
            <div class="header"> <p>%(headertext)s</p> </div>
            <div class="spacer"></div>
            <hr noshade>
            <div class="caption"> <p>%(captiontext)s</p> </div>
            <div class="content">
                %(content)s
            </div>
        </div>
        """

        self.body.append(template%{'imgpath': node['icon'],
                                   'headertext': node['head'],
                                   'captiontext': node['caption'],
                                   'content': node['content']})
        raise nodes.SkipNode

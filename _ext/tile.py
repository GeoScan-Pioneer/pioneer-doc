from docutils import nodes, utils
from docutils.nodes import Body, Element
from docutils.parsers.rst import directives

from docutils.parsers.rst import Directive

from docutils.statemachine import ViewList

class tilenode(Element):
    pass

def visit_tile(self, node):
    template = """
            <div class="tile">
                <div class="image"> <img src="%(imgpath)s" alt="icon"> </div>
                <div class="header"> <p>%(headertext)s</p> </div>
                <div class="spacer"></div>
                <hr noshade>
                <div class="caption"> <p>%(captiontext)s</p> </div>
                <div class="content">"""

    self.body.append(template % {'imgpath': node['icon'],
                                 'headertext': node['head'],
                                 'captiontext': node['caption']})

def depart_tile(self, node):
    self.body.append("""</div></div>""")

class TileDirective(Directive):
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
        rst = ViewList()

        for pos, line in enumerate(self.content):
            rst.append(line, 'fakefile.rst', pos)

        node = tilenode('\n'.join(self.content))

        # nested_parse_with_titles(self.state, rst, node)
        self.state.nested_parse(self.content, self.content_offset, node)

        node['icon'] = self.options['icon'] if 'icon' in self.options else " "
        node['head'] = self.options['head'] if 'head' in self.options else " "
        node['caption'] = self.options['caption'] if 'caption' in self.options else " "
        return [node]


# <div class="local-toc">{{ toc }}</div>
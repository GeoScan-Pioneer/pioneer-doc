from docutils import nodes, utils
from docutils.nodes import Body, Element
from docutils.parsers.rst import directives

from docutils.parsers.rst import Directive

from docutils.statemachine import ViewList

class tilenode(Element):
    pass

def visit_tile(self, node):
    template = '            <div class="tile'

    if node['icon'] is None:
        template += ' no-image'
    if node['head'] is None or node['caption'] is None:
        template += ' no-any-text'

    template += f'"style="grid-template-rows: {node["hpx"]}px; height: {node["hpx"]}px">'
    # template += '">'


    if node['icon'] is not None:
        ins = node['icon']
        template += '\n'
        template += f'                <div class="image"> <img src="{ins}" alt="icon"> </div>'
    else:
        template += '\n'
        template += '                <div class="spacer">▶</div>'

    if node['head'] is not None:
        ins = node['head']
        template += '\n'
        template += f'                <div class="header"> <p>{ins}</p> </div>'

    if node['head'] is not None and node['caption'] is not None:
        template += '\n'
        template += '                <div class="spacer"></div>'
        template += '\n'
        template += '                <hr noshade>'

    if node['caption'] is not None:
        ins = node['caption']
        template += '\n'
        template += f'                <div class="caption"> <p>{ins}</p> </div>'

    template += '\n'
    template += '                <div class="content">'

    self.body.append(template)

def depart_tile(self, node):
    self.body.append("""</div></div>""")

class TileDirective(Directive):
    final_argument_whitespace = True

    option_spec = {
        'icon': directives.unchanged,
        'head': directives.unchanged,
        'caption': directives.unchanged,
        'hpx': directives.unchanged
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

        node['icon'] = self.options['icon'] if 'icon' in self.options else None
        node['head'] = self.options['head'] if 'head' in self.options else None
        node['caption'] = self.options['caption'] if 'caption' in self.options else None
        node['hpx'] = self.options['hpx'] if 'hpx' in self.options else 80
        return [node]


# <div class="local-toc">{{ toc }}</div>
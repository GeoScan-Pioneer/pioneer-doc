from docutils import nodes, utils
from docutils.nodes import Body, Element
from docutils.parsers.rst import directives
from docutils.statemachine import ViewList

from sphinx.util.nodes import nested_parse_with_titles
from docutils.parsers.rst import Directive

from docutils.core import publish_parts
from rst2html5 import HTML5Writer

from sphinx import addnodes

class platenode(Body, Element):
    pass

class PlateDirective(Directive):
    required_arguments = 0
    optional_arguments = 0
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

        toctree_flag = False
        ind1, ind2 = 0, 0

        content = [i for i in self.content]

        toctree_params = []
        toctree_sources = []

        for pos, line in enumerate(self.content):
            if line.encode('utf-8') == b'':
                line = '\n'

            if not toctree_flag:
                toctree_index = line.find('.. toctree::')
                if toctree_index >= 0:
                    toctree_flag = True
                    body += publish_parts(writer=HTML5Writer(), source=rst)['body'] + '\n'
                    rst = ''

                    ind1 = content.index('', pos+1)
                    toctree_params = content[pos+1:ind1]
                    toctree_params = dict([(i.split(':')[1], i.split(':')[2]) for i in toctree_params])

                    try:
                        ind2 = content.index('', ind1+1)
                        toctree_sources = content[ind1+1:ind2]
                    except Exception:
                        toctree_sources = content[ind1+1:]

                    continue
                rst += line + '\n'
            else:
                if pos >= ind2:
                    toctree_flag = False

        body += publish_parts(writer=HTML5Writer(), source=rst)['body']

        print('params: ', toctree_params)
        print('sources: ', toctree_sources)

        toc = addnodes.toctree()
        print("keeeeeeeeeeek: ", toc)

        wrappernode = nodes.compound(classes=['toctree-wrapper1'])
        wrappernode.append(toc)

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

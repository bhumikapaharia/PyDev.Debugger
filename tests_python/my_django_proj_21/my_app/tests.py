from django.test import SimpleTestCase


class MyTest(SimpleTestCase):

    def test_something(self):
        from django import template
        t = template.Template('''
{% if entries %}
    <ul>
    {% for entry in entries %}
        {% for entry in entries2 %}
            <li>
                {{ entry.key }}
                :
                {{ entry.val }}
            </li>
        {% endfor %}
    {% endfor %}
    </ul>
{% else %}
    <p>No entries are available.</p>
{% endif %}
''')

        nodelist = t.compile_nodelist()
        for node in self._iternodes(nodelist):
            print(node, self._get_lineno(node))

    def _get_lineno(self, node):
        if hasattr(node, 'token') and hasattr(node.token, 'lineno'):
            return node.token.lineno
        return None

    def _iternodes(self, nodelist):
        for node in nodelist:
            yield node

            for attr in node.child_nodelists:
                nodelist = getattr(node, attr, None)
                if nodelist:
                    # i.e.: yield from self._iternodes(nodelist)
                    for node in self._iternodes(nodelist):
                        yield node


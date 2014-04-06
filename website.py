import os

import jinja2
from flask import Flask


JINJA_ENVIRONMENT = jinja2.Environment(
    loader      = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions  = ['jinja2.ext.autoescape'],
    auto_reload = True,
)


def render_template(page):
    template = JINJA_ENVIRONMENT.get_template('templates/{0}.html'.format(page))
    content = template.render(page=page)

    template = JINJA_ENVIRONMENT.get_template('templates/layout.html')
    return template.render(page=page, content=content)


app = Flask(__name__)
app.add_url_rule('/'                    , 'index'               , lambda: render_template('index'))
app.add_url_rule('/story'               , 'story'               , lambda: render_template('story'))
app.add_url_rule('/collection'          , 'collection'          , lambda: render_template('collection'))
app.add_url_rule('/silk'                , 'silk'                , lambda: render_template('silk'))
app.add_url_rule('/sustainable'         , 'sustainable'         , lambda: render_template('sustainable'))
app.add_url_rule('/legales'             , 'legales'             , lambda: render_template('legales'))
app.add_url_rule('/about-us'            , 'about-us'            , lambda: render_template('about-us'))
app.add_url_rule('/terms-and-conditions', 'terms-and-conditions', lambda: render_template('terms-and-conditions'))
app.add_url_rule('/wholesale'           , 'wholesale'           , lambda: render_template('wholesale'))
app.add_url_rule('/contact'             , 'contact'             , lambda: render_template('contact'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

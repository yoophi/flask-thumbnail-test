import os

from flask import Flask, render_template
from flask import send_from_directory
from flask.ext.thumbnails import Thumbnail
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


CURRENT_DIR = os.path.dirname(__file__)

app = Flask(__name__)
app.config['MEDIA_FOLDER'] = os.path.join(CURRENT_DIR, 'media')
app.config['MEDIA_URL'] = '/media/'
app.url_map.converters['regex'] = RegexConverter

thumb = Thumbnail(app)


@app.route('/')
def index():
    gen_url = thumb.thumbnail('image.jpg', '100x100', crop='fit', quality=85)
    return render_template('app.html', gen_url=gen_url)


@app.route('/media/<regex("([\w\d_/-]+)?.(?:jpe?g|gif|png)"):filename>')
def media_file(filename):
    return send_from_directory(app.config['MEDIA_THUMBNAIL_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)

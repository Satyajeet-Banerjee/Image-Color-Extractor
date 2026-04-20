import os
from flask import Blueprint, render_template, request, current_app
from werkzeug.utils import secure_filename
from .services.color_extractor import extract_top_colors

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']

        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            colors = extract_top_colors(filepath)

            hex_colors = [
                '#%02x%02x%02x' % tuple(color) for color in colors
            ]

            return render_template(
                'result.html',
                image=filename,
                colors=hex_colors
            )

    return render_template('index.html')
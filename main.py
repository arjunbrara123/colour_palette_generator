import colorgram
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask import Flask, request, render_template
app = Flask(__name__)


# Extract 6 colors from the image.
def get_cols(img_path):
    #cols = []
    cols = colorgram.extract(img_path, 6)
    return cols


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/'+secure_filename(f.filename))
        cols = get_cols('static/'+f.filename)
        output_cols = ""
        for col in cols:
            output_cols += col.rgb.__str__() + "<br>"
        return output_cols


@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)

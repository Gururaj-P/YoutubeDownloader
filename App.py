from flask import Flask, render_template, request
from pytube import YouTube
from pytube.exceptions import RegexMatchError

app = Flask(__name__, template_folder="templates")


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/download', methods=['GET', 'POST'])
def download():
    # fetch the url entered in the html form
    url = request.form.get("url")
    try:
        YouTube(url).streams.first().download('Downloads')
    except RegexMatchError:
        return render_template('errorPage.html')
    else:
        return render_template('downloadPage.html')


if __name__ == '__main__':
    app.run(debug=True)

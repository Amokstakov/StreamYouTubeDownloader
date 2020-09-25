import re
import os
from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
import pytube

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/converter', methods=['GET', 'POST'])
@cross_origin()
def URL_converter():

    if request.method == "POST":
        url = request.json
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()

        title = video.title
        title = re.sub(r'[^\w]', ' ', title)
        title = title.replace(" ", "_")

        video.download("./Videos", title)

        return title

    else:
        return "This is a miss call"


@app.route('/api/getFile/<video_title>')
@cross_origin()
def return_file(video_title):
    try:
        return send_file(f"./Videos/{video_title}.mp4", attachment_filename=f"{video_title}.mp4", as_attachment=True)

    except Exception as e:
        return e


if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, port=8080)

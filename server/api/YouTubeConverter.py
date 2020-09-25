# import re
# from flask import Flask, request, send_file
# from flask_cors import CORS, cross_origin
# import pytube

# app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


# @app.route('/converter', methods=['GET', 'POST'])
# @cross_origin()
# def URL_converter():

# if request.method == "POST":
# url = request.json
# # try:
# youtube = pytube.YouTube(url)
# # except Exception as e:
# # error = "URL недействителен в формате YouTube. Проверьте еще раз"
# # return error
# video = youtube.streams.first()

# title = video.title
# title = re.sub(r'[^\w]', ' ', title)
# title = title.replace(" ", "_")
# video.download("../Videos", title)

# return title

# else:
# return "This is a miss call"


# @app.route('/getFile/<video_title>')
# @cross_origin()
# def return_file(video_title):
# try:
# return send_file(f"../Videos/{video_title}.mp4", attachment_filename=f"{video_title}.mp4", as_attachment=True)

# except Exception as e:
# return e

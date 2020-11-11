from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    transcript= ''
    if request.method== "POST":
        if "file" not in request.files:
            print ("there is no file")
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            print("Has No Data", file.filename)
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            #  Create audio file from the file that was uploaded
            # parse uploaded file into RECORD fn of recognizer module
            # file will be parsed into understandle format
            audioFile = sr.AudioFile(file)
            #  Open and read the file 
            with audioFile as source:
                data = recognizer.record(source)
            
            transcript = recognizer.recognize_google(data, key=None)
            print(transcript)

            print("check recognizer ", recognizer)

    return render_template('index.html', transcript= transcript)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.wav')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run(debug=True, threaded=True)




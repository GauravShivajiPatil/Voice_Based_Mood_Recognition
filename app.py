import numpy as np
import os
import librosa
import speech_recognition as sr
import librosa.display	
import warnings
warnings.filterwarnings("ignore")
import pickle



from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
  return render_template("index.html")


@app.route("/recording", methods=["GET", "POST"])
def record():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Hiii, Say something!")
        audio=r.record(source,duration=6)
    print("Recording Done")
    
    if os.path.exists('static/output.wav'):
        os.remove("static/output.wav")
        
    with open("static/output.wav", "wb") as f:
        f.write(audio.get_wav_data())
        f.close()
    print("Record saved!")
    
    return render_template('/index.html')



@app.route("/at", methods=["GET", "POST"])
def audiototext():
    r=sr.Recognizer()
    if os.path.exists('static/output.wav'):
        txt=sr.AudioFile("static/output.wav")
        with txt as source:
            audio=r.record(source)
        try:
            s=r.recognize_google(audio)
            print("You said : "+s)
        except Exception as e:
            s="cannot recognize your voice"
    else:
        s="Audio doesn't exists !!!"
        render_template('/index.html',transcript=s)
        
    return render_template('/index.html',transcript=s)


x=[]
y=[]

#This function extracts features from the recorded
#audio using the Librosa library. It returns a numpy
#array containing the extracted features.
def extract_feature(data,sampling_rate):
    result=np.array([])
    #Path=i
    #result=np.hstack((result, Path))
    
    stft = np.abs(librosa.stft(data))
    chromagram = np.mean(librosa.feature.chroma_stft(S=stft, sr=sampling_rate).T, axis=0)
    result=np.hstack((result, chromagram))
   
     
        
    mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
    result=np.hstack((result, mfcc))
    

    mel=np.mean(librosa.feature.melspectrogram(data, sr=sampling_rate).T,axis=0)
    result=np.hstack((result, mel))
    

    return result






@app.route("/predict", methods=["GET", "POST"])
def predict():
    label=""
    Pkl_Filename="new_mlp_74.pkl"
    with open(Pkl_Filename,'rb') as file:
        model=pickle.load(file)
        
    x=[]
    
    if os.path.exists('static/output.wav'):
        data, sampling_rate=librosa.load('static/output.wav')
    else:
        label="Please record audio to predict !!!"
        return render_template('/index.html',label=label)
        
    feature=extract_feature(data, sampling_rate)
    x.append(feature)
    
    label=model.predict(x)
    
    return render_template('/index.html',label=label)


    
@app.route("/request", methods=["GET", "POST"])
def index():
    transcript2 =""    
    print("I am innnn")
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        file.filename = "static/output1.wav"  #some custom file name that you want
        file.save(file.filename)
        
        if file.filename == "":
            return redirect(request.url)
        if file:
            r = sr.Recognizer()
            txt=sr.AudioFile("static/output1.wav")
            with txt as source:
                audio = r.record(source)
            try:
                transcript2 = r.recognize_google(audio)
                print("You Said  : "+transcript2)
            except Exception as e:
                transcript2= "cannot recognize your voice"
                
            
    return render_template('/index.html', transcript2=transcript2)



#This code defines another route in the Flask app. When a
#user navigates to /predictbyupload using a web browser,
#this function will be called. The function accepts both GET and POST requests.
@app.route("/predictbyupload", methods=["GET", "POST"])
def predictbyupload():
    l=""
    Pkl_Filename="new_mlp_74.pkl"
    with open(Pkl_Filename,"rb") as file:
        model=pickle.load(file)
        
    x=[]
    
    if os.path.exists('static/output1.wav'):
        data, sampling_rate=librosa.load('static/output1.wav')
    else:
        l="Please upload audio to predict !!!"
        return render_template('/index.html',l=l)
        
    feature=extract_feature(data, sampling_rate)
    x.append(feature)
    
    l=model.predict(x)
    
    return render_template('/index.html',l=l)



@app.route('/remove', methods=['GET','POST'])
def removefile():
    if os.path.exists("static/output.wav"):
        os.remove("static/output.wav")
        print("File deleted ")
    else:
        print("file doesn't exists")
        
    if os.path.exists("static/output1.wav"):
        os.remove("static/output1.wav")
        print("File deleted ")
    else:
        print("file doesn't exists")
        
    return render_template('/index.html')




if __name__ == '__main__':
	app.run(host="localhost",debug = True)
	# app.run()
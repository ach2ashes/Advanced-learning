import deepspeech
import numpy as np
import wave
import speech_recognition as sr
'''
def transcribe(audio_path):

    # Path to the DeepSpeech pre-trained model
    model_path = 'deepspeech-0.9.3-models.pbmm'

    # Load the DeepSpeech model
    model = deepspeech.Model(model_path)
    model.enableExternalScorer("deepspeech-0.9.3-models (3).scorer")

    # Load audio file
    audio = wave.open(audio_path, 'rb')
    sample_rate = audio.getframerate()

    # Read audio file as a numpy array
    audio_data = np.frombuffer(audio.readframes(audio.getnframes()), dtype=np.int16)

    # Transcribe audio
    transcript = model.stt(audio_data)

    # Print the transcription
    return transcript
'''
def transcribe():
    
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = recognizer.record(source, duration=5)
    
    text = recognizer.recognize_google(audio_data)
    return  text

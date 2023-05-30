import pyaudio
import wave

def record_audio(output_file, duration):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    sample_rate = 16000

    audio = pyaudio.PyAudio()
    print("Start")
    stream = audio.open(format=sample_format,
                        channels=channels,
                        rate=sample_rate,
                        frames_per_buffer=chunk,
                        input=True)

    frames = []
    for i in range(int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(sample_format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    

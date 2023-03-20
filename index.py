import speech_recognition as sr 
from pydub import AudioSegment
import os

#Uma lista de arquivos dentro de uma pasta específica 
m4as = []
path = os.path.dirname(r"[DIRECTORY]")
abspath = os.path.abspath(path)
dirs = os.listdir(abspath)

#Transformar os aquivos do formato escolhido (nesse caso, m4a) em wav
for file in dirs:
    if file.endswith('m4a'):
       m4as.append(file)

def m4a_to_wav(name):
    audio = AudioSegment.from_file(abspath + '/' + name, format="m4a")
    export_name = os.path.splitext(name)[0]
    new_audio = audio.export(export_name + '.wav', format = 'wav')
    return new_audio

for m4a in m4as:
    m4a_to_wav(m4a)

#Usar o Speech Recognition 
r = sr.Recognizer()
for m4a in m4as:
    print(m4a)
    new_audio = m4a_to_wav(m4a)
    audio = sr.AudioFile(new_audio)
    with audio as source:
        audio_text = r.record(source)
        text = r.recognize_google(audio_text, language='pt-BR')

#Imprimir a transcrição em um arquivo txt
arq = open('nome_arquivo.txt', 'w')
arq.write(text)
arq.close()

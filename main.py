import os
import speech_recognition as sr

r = sr.Recognizer()
clear = lambda: os.system('cls')
lyrics,nowlyrics,worse = [],[],[]

while len(lyrics) > 0:
    with sr.Microphone() as source:
        clear()
        nowlyrics.append(lyrics[0])
        print(f"Hatalı kelimeler : "+" ".join(worse)+"\n"+"Şarkı Sözü : "+" ".join(nowlyrics))
        audio = r.listen(source)
        try:
            if r.recognize_google(audio) == lyrics[0]:
                lyrics.pop(0)
            else:
                worse.append(lyrics[0])
                lyrics.pop(0)
        except:
            print("HATA : Sesiniz algılanamadı.")
            break
print("Şarkıyı bitirdiniz. Level atlandı!")     

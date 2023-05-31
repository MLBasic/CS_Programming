from gtts import gTTS
import os

text = "안녕하세요, 여러분 파이썬은 재미있습니다. "

tts = gTTS(text=text, lang='ko')
tts.save('tts.mp3')
os.system('tts.mp3')

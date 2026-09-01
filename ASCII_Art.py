#pip install gTTS

from gtts import gTTS

text = input("Enter the text you want to convert to speech: ")
tts = gTTS(text=text, lang='en')
output_file = input("Enter the name of the output audio file (without extension): ")
tts.save(f"{output_file}.mp3")
print(f"Audio file '{output_file}.mp3' has been created successfully.")
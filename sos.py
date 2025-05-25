from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
import time


model_path = r"D:\final project\NLP\3\AraT5_finetuned_model"
model = AutoModelForSeq2SeqLM.from_pretrained(model_path, local_files_only=True)
tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)

while True:
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print('Say something...')
        r.adjust_for_ambient_noise(src, duration=1)
        try:
            audio = r.listen(src, timeout=5, phrase_time_limit=10)

        except sr.WaitTimeoutError:
            print("No speech detected within timeout.")
            exit()
            break

    try:
        t = r.recognize_google(audio, language='ar-AR')
        print("Recognized text:", t)
        inputs = tokenizer(t, return_tensors="pt", padding=True, truncation=True)
        output_tokens = model.generate(**inputs)
        output_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)

        with open('text.txt', 'a', encoding='utf-8') as f:
           f.write(t + '\n')

        mp3_file = os.path.abspath('text.mp3')
        obj = gTTS(text=output_text, lang='ar', slow=False)
        obj.save(mp3_file)
        time.sleep(1)  # Ensure file is written
        playsound(mp3_file)
        os.remove(mp3_file)  # Clean up

    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

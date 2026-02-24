from googletrans import Translator
from gtts import gTTS
import pygame
import os

def translate_and_speak(text, target_lang='es'):
    # 1. Initialize Translator
    translator = Translator()
    
    # 2. Translate Text
    translation = translator.translate(text, dest=target_lang)
    print(f"Original ({translation.src}): {text}")
    print(f"Translated ({target_lang}): {translation.text}")
    
    # 3. Convert Translated Text to Speech (Audio)
    tts = gTTS(text=translation.text, lang=target_lang, slow=False)
    
    # 4. Save and Play Audio
    audio_file = "captured_voice.mp3"
    tts.save(audio_file)
    
    # Initialize Pygame mixer to play audio
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    
    # Wait for audio to finish
    while pygame.mixer.music.get_busy():
        continue
    
    # Cleanup: Close mixer and remove file so it can be overwritten
    pygame.mixer.quit()
    os.remove(audio_file)

# --- EXECUTION ---
if __name__ == "__main__":
    user_input = input("Enter English text to translate: ")
    print("Choose Language: es (Spanish), fr (French), hi (Hindi), de (German)")
    lang_choice = input("Enter language code: ")
    
    translate_and_speak(user_input, lang_choice)

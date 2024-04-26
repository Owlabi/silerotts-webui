import gradio as gr
import os

# Создаем список доступных speaker
speakers = ['aidar', 'baya', 'kseniya', 'xenia', 'eugene', 'random']
models = ['v4_ru', 'v3_1_ru', 'ru_v3', 'aidar_v2', 'aidar_8khz', 'aidar_16khz', 'baya_v2', 'baya_8khz', 'baya_16khz', 'irina_v2', 'irina_8khz', 'irina_16khz', 'kseniya_v2', 'kseniya_8khz', 'kseniya_16khz', 'natasha_v2', 'natasha_8khz', 'natasha_16khz', 'ruslan_v2', 'ruslan_8khz', 'ruslan_16khz']

def tts(file, speaker, model):
  # assuming tts.py is in the same directory as this script
  os.system(f"python tts.py --file {file.name} --speaker {speaker} --model {model}")
  # assuming tts.py outputs a file called output.wav in the same directory
  return "output.wav"

iface = gr.Interface(
  fn=tts,
  inputs=[        
        gr.File(label="Ваш txt файл", type="filepath"),
        gr.Dropdown(label="Выберите диктора", choices=["aidar", "baya", "kseniya", "xenia", "eugene", "random"], value="baya"), # отправляет 
        gr.Dropdown(label="Model", choices=models, value="v3_1_ru"), # отправляет 
  ],
  outputs=[
        gr.Audio(type="filepath", autoplay=True),
  ],
  title="TTS by Neurogen",
  description="Загрузите ваш txt файл с текстом и получите на выходе аудиофайл с озвучкой</br>Работает на базе SileroTTS"
)

iface.launch()

import gradio as gr
import os

# Создаем список доступных speaker
speakers = ['aidar', 'baya', 'kseniya', 'xenia', 'eugene', 'random']

def tts(file, speaker):
  # assuming tts.py is in the same directory as this script
  os.system(f"python tts.py --file {file.name} --speaker {speaker}")
  # assuming tts.py outputs a file called output.wav in the same directory
  return "output.wav"

iface = gr.Interface(
  fn=tts,
  inputs=[        
        gr.File(label="Ваш txt файл", type="filepath"),
        gr.Dropdown(label="Выберите диктора", choices=["aidar", "baya", "kseniya", "xenia", "eugene", "random"], value="baya"), # отправляет
  ],
  outputs=[
        gr.Audio(type="filepath", autoplay=True),
  ],
  title="TTS by Neurogen",
  description="Загрузите ваш txt файл с текстом и получите на выходе аудиофайл с озвучкой</br>Работает на базе SileroTTS"
)

app = iface.launch

def external_app():
  iface.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
  app()

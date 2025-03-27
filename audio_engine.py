from pydub import AudioSegment
import sounddevice as sd

class AudioEngine:
    def __init__(self):
        self.sample_rate = 44100  # Fréquence d'échantillonnage standard

    def load_audio(self, file_path):
        """Charge un fichier audio (MP3/WAV) avec pydub"""
        return AudioSegment.from_file(file_path)

    def play(self, audio_segment, bus_id=0):
        """Joue un son sur un bus spécifique"""
        samples = audio_segment.get_array_of_samples()
        sd.play(samples, self.sample_rate, device=bus_id)

from audio_engine import AudioEngine

engine = AudioEngine()
audio = engine.load_audio("test.wav")  # Charge le fichier
engine.play(audio)  # Joue le son
input("Appuyez sur Entrée pour arrêter...")  # Garde le programme actif

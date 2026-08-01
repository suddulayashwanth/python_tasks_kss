class WiFiDevice:
    def connect_wifi(self):
        print("Smart speaker connected to WiFi.")


class VoiceAssistant:
    def accept_voice_command(self):
        print("Voice command received.")


class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def play_music(self):
        print("Playing music.")


speaker = SmartSpeaker()

speaker.connect_wifi()
speaker.accept_voice_command()
speaker.play_music()
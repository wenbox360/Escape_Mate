from cartesia import Cartesia
import pyaudio
import os

def create_audio(user_transcript):
    client = Cartesia(api_key=os.environ.get("c9e1bac7-37b1-4c93-ac5a-a401b2ed101d"))
    voice_name = "Barbershop Man"
    voice_id = "2461f054-b556-48f5-bc6d-362232d335ab"
    voice = client.voices.get(id=voice_id)
    transcript = user_transcript

    # You can check out our models at https://docs.cartesia.ai/getting-started/available-models
    model_id = "sonic-english"

    # You can find the supported `output_format`s at https://docs.cartesia.ai/reference/api-reference/rest/stream-speech-server-sent-events
    output_format = {
        "container": "raw",
        "encoding": "pcm_f32le",
        "sample_rate": 22050,
    }

    p = pyaudio.PyAudio()
    rate = 22050

    stream = None

    # Set up the websocket connection
    ws = client.tts.websocket()

    # Generate and stream audio using the websocket
    for output in ws.send(
        model_id=model_id,
        transcript=transcript,
        voice_embedding=voice["embedding"],
        stream=True,
        output_format=output_format,
    ):
        buffer = output["audio"]

        if not stream:
            stream = p.open(format=pyaudio.paFloat32, channels=1, rate=rate, output=True)

        # Write the audio data to the stream
        stream.write(buffer)

    stream.stop_stream()
    stream.close()
    p.terminate()

    ws.close()  # Close the websocket connection
from cartesia import Cartesia
import pyaudio
import os

def create_audio(user_transcript):
    client = Cartesia(os.getenv("CARTESIA_API_KEY"))
    voice_name = "Hang"
    voice_id = "c1fdb842-8fec-4834-8b3e-11ae538a1d7c"
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

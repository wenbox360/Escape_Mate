import asyncio
import json
import tts
from tts import create_audio
import sensor_game
from sensor_game import game
from sst import recognize_speech
from question import answer_questions
from langchain_setup import setup_langchain

question_queue = asyncio.Queue()

llm = setup_langchain()

async def run(story):
    stages = story['stages']
    create_audio(story['intro'])
    for stage in stages:
        create_audio(stage['description'])
        completed = False
        speech_task = asyncio.create_task(recognize_speech(question_queue))
        while not completed:  
            if not question_queue.empty():
                question = await question_queue.get()
                answer = answer_questions(llm, question, story['brief'])
                create_audio(answer)
            completed = await game()
            await asyncio.sleep(0.1)
        #speech_task.cancel()
        #await speech_task
        create_audio(stage['success_message'])

    create_audio(story['good_ending'])

    print("Game completed")
    return



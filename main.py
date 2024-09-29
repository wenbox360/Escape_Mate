import json
import tts
from tts import create_audio
import sensor_game
from sensor_game import game

with open('text.json', 'r') as file:
    data = json.load(file)

    stages = data['stages']

    stage_index = 0

    tts(data['brief'])
    tts(data['introduction'])

    for stage in stages:
        tts(stage['stage_intro'])
        tts(stage['stage_instructions'])
        completed = False
        while(completed is False):
            completed = game()
        if stage_index < len(stages) - 1:
            tts(data['next_stage'])

        stage_index += 1
    
    tts(data['good_ending'])

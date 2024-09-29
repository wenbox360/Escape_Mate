import json
import tts
from tts import create_audio
import sensor_game
from sensor_game import game

with open('text.json', 'r') as file:
    data = json.load(file)

    stages = data['stages']

    stage_index = 0

    create_audio(data['brief'])
    create_audio(data['introduction'])

    for stage in stages:
        create_audio(stage['stage_intro'])
        create_audio(stage['stage_instructions'])
        completed = False
        while(completed is False):
            completed = game()
        if stage_index < len(stages) - 1:
            create_audio(data['next_stage'])

        stage_index += 1
    
    create_audio(data['good_ending'])

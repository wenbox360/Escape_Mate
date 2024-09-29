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
    create_audio(data['intro'])
    
    for stage in stages:
        create_audio(stage['description'])
        completed = False
        while(completed is False):
            completed = game()
        create_audio(stage['success_message'])
        
    
    create_audio(data['good_ending'])


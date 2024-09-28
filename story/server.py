from flask import Flask, request, jsonify
from baml_client import b
from baml_client.types import StoryParams

app = Flask(__name__)

@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.json
    theme = data['theme']
    difficulty = data['difficulty']
    stage_physical_descriptions = data['stage_physical_descriptions']
    num_players = data['num_players']
    time_limit_min = data['time_limit_min']
    story_params = StoryParams(
        theme=theme,
        difficulty=difficulty,
        stage_physical_descriptions=stage_physical_descriptions,
        num_players=num_players,
        time_limit_min=time_limit_min
    )
    try:
        story = b.GenerateStory(story_params)
        return jsonify(story)
    except Exception as e:
        print('Error generating story:', e)
        return jsonify({'error': 'Failed to generate story'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

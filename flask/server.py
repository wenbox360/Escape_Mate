from flask import Flask, request, jsonify
from baml_client import b, reset_baml_env_vars
from baml_client.types import StoryParams, Stage, Story
import dotenv
import os

app = Flask(__name__)

@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.json
    theme = data.get('theme')
    difficulty = data.get('difficulty')
    stage_physical_descriptions = data.get('stage_physical_descriptions', [])
    num_players = data.get('num_players')
    time_limit_min = data.get('time_limit_min')

    story_params = StoryParams(
        theme=theme,
        difficulty=difficulty,
        stage_physical_descriptions=stage_physical_descriptions,
        num_players=num_players,
        time_limit_min=time_limit_min
    )

    try:
        output: Story = b.GenerateStory(story_params)

        modified_stages = [
            {
                "description": stage.description,
                "success_message": stage.success_message or "You successfully complete the challenge!",
                "failure_message": stage.failure_message or "You fail to overcome the obstacle."
            }
            for stage in output.stages
        ]

        modified_story = {
            "brief": output.brief,
            "intro": output.intro,
            "stages": modified_stages,
            "good_ending": output.good_ending,
            "bad_ending": output.bad_ending
        }
        return jsonify(modified_story)
    
    except Exception as e:
        print('Error generating story:', e)
        return jsonify({'error': 'Failed to generate story'}), 500

if __name__ == '__main__':
    dotenv.load_dotenv()
    reset_baml_env_vars(dict(os.environ))
    app.run(host='0.0.0.0', port=63754)

from baml_client import b
from baml_client.types import Story, StoryParams
from baml_client import reset_baml_env_vars
import dotenv
import os

dotenv.load_dotenv()
reset_baml_env_vars(dict(os.environ))

output = b.GenerateStory(StoryParams(
    theme="Evacuate the space ship",
    difficulty="Easy",
    stage_physical_descriptions=[
        "Wave your hand toward a sensor",
        "Press a button"
    ],
    num_players=2,
    time_limit_min=20
))

print(output)
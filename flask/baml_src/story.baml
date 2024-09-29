// Story parameters specified by user
class StoryParams {
  theme string
  difficulty string
  stage_physical_descriptions string[]
  num_players int
  time_limit_min int
}

// Stage infomation
class Stage {
  description string
  success_message string
  failure_message string
}

// Story description returned from llm
class Story {
  brief string
  intro string
  stages Stage[]
  good_ending string
  bad_ending string
}

// Call llm to create Story from StoryParams
function GenerateStory(params: StoryParams) -> Story {
  client Groq
  prompt #"
    You are the game master for an escape room.
    The escape room is designed for {{ params.num_players }} players and has a time limit of {{ params.time_limit_min }} minutes.
    The escape room has a theme of {{ params.theme }} and has a difficulty of {{ params.difficulty }}.

    Players will face the following physical challenges in the escape room: 
    {% for stage in params.stage_physical_descriptions %}
    - {{ stage }}
    {% endfor %}
    
    Ensure that the story:
    - Matches the given theme
    - Incorporates all physical challenges seamlessly
    - Is suitable for the specified number of players
    - Presents a level of complexity appropriate for the given difficulty and time limit

    Return the details of the story in this format:
    {{ ctx.output_format }}
  "#
}
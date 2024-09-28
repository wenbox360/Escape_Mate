from narration import get_unique_narration
from tts import trigger_tts_for_characters
from tts import trigger_tts_for_introductory_narration
from langchain_setup import setup_langchain

# Game loop
def run_game():
    llm = setup_langchain()

    current_state = "introduction"
    while current_state != "finished":

        if(current_state == "introduction"):
            trigger_tts_for_introductory_narration()
            print("Initial Adjustment") # Placeholder
        else:
            resistance_narration = get_unique_narration("resistance_leader", current_state, llm)
            shadow_narration = get_unique_narration("shadow", current_state, llm)
            trigger_tts_for_characters(resistance_narration, shadow_narration)

            if current_state == "initial_adjustment":
                current_state = "bias_too_high"
            # ... other state transitions
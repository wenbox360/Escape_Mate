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
            current_state = "stage1"
        elif(current_state == "finished"):
            print("Game finished") # Placeholder
        else:
            resistance_narration = get_unique_narration("resistance_leader", current_state, llm)
            shadow_narration = get_unique_narration("shadow", current_state, llm)
            trigger_tts_for_characters(resistance_narration, shadow_narration)

            if (current_state == "stage1"): #&& level passed
                print("Puzzle")
            # ... other state transitions
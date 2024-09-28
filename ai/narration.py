import random
from langchain.chat_models import ChatModel

# Resistance Leader narrations
RESISTANCE_NARRATION_VARIATIONS = {
    #PASTE THE NARRATION VARIATIONS HERE
    "introduction": [
        "You're in! We've accessed the core systems. Adjust those controls carefully, this system is fragile.",
        "You're on the right track! Start making adjustments, but be cautious—we can't afford mistakes.",
        "Good job getting in! Now you need to balance the system without causing too much disruption."
    ],
    # ... other narration variations for Resistance Leader
}

# Shadow narrations
SHADOW_NARRATION_VARIATIONS = {
    #PASTE THE NARRATION VARIATIONS HERE
    "introduction": [
        "Access granted. You are now adjusting the bias controls. Be precise.",
        "You've begun altering the AI's core parameters. Adjust carefully.",
        "The system is reacting to your input. Continue modifying the bias controls."
    ],
    # ... other narration variations for Shadow
}

used_narrations = {
    "resistance_leader": [],
    "shadow": []
}

def get_unique_narration(character, type_of_narration, llm: ChatModel):
    narration_pool = (RESISTANCE_NARRATION_VARIATIONS if character == "resistance_leader" 
                      else SHADOW_NARRATION_VARIATIONS)[type_of_narration]
    unused_narrations = [n for n in narration_pool if n not in used_narrations[character]]
    
    if not unused_narrations:
        used_narrations[character] = []
        unused_narrations = narration_pool
    
    narration = random.choice(unused_narrations)
    used_narrations[character].append(narration)
    
    # Use the provided LLM (Google AI) to generate the narration
    if character == "resistance_leader":
        result = llm.invoke([
            ("system", "You are the Resistance Leader. Provide the following narration:"),
            ("human", narration)
        ])
    else:
        result = llm.invoke([
            ("system", "You are the Shadow. Provide the following narration:"),
            ("human", narration)
        ])
    
    return result
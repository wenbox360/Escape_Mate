import random
from langchain.chat_models import ChatModel

def parseJson(json):
    # Parse the JSON and return the fields as a dictionary

def get_unique_narration(json, serialData, stage, llm: ChatModel):
    
    data = parseJson(json)
    context = data['brief']

    basic_motivators = ["You can do it!", "You're almost there!", "Keep going!", "You're doing great!", "You're making progress!"]
    
    # Use the provided LLM (Google AI) to generate the narration
    
    result = llm.invoke([
        ("system", "Consider the following scenario: " + context),
           
        ])
    
    
    return result
    
    
    
from baml_client import b
from baml_client.types import *

# add to baml
def AnswerQuestion(brief: str, question: str, answer: str):
    return b.GenerateStory(StoryParams(
        brief=brief,
        question=question,
        answer=answer
    ))
    return output

def handle_failure(message):
    print(f"Failure: {message}")

# game loop
# only keep track of stage
def game_loop():
    stage = 0
    faq = ["What is the objective?", "How much time do we have?", "What are the rules?"]
    brief = "You are in an escape room game."
    while True:
        print(f"Current stage {stage}")
        

if __name__ == "__main__":
    game_loop()
from langchain.chat_models import ChatModel

STATES_COMMON_QA = {
    "stage1":{
            "1": "",
            "2": "",
            "3": ""
        }
    }

def answer_questions(llm: ChatModel, question, state):
    if state == "stage1":
        category = llm.invoke([
        ("system", "Please categorize the following question only into the following categories: "
                "1. Wire connection, 2. How to use buttons, 3. Objective. Please return only a number corresponding to the category. e.g 1"),
        ("human", question)
        ])
        
        # Use the provided LLM (Google AI) to generate the response
        
        response = llm.invoke([("system", f"Please see if there are any helpful answers through here and answer the human's question accordingly : {STATES_COMMON_QA[state][category]} "),
        ("human", question)
        ])
        
        return response
    
    

    
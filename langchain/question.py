STATES_COMMON_QA = {
    "stage1":{
            "1": "The end of the long wire with an red head should be secured into your device's port section not covered with blue tape. ",
            "2": "The buttons are used to control the LED count. The one closer to you decreases the count and the one further increases the count of LEDS.",
            "3": "Your objective is to crack the code. You can do this by adjusting the LEDS to the correct values.",
            "4": "This is not a question. Please respond back in an meangingful way."

        }
    }


def answer_questions(llm: ChatModel, question, brief):
    category = llm.invoke([
    ("system", "Please categorize the following question only into the following categories: "
            "1. Wire connection, 2. How to use buttons, 3. Objective. 4. Not a question Please return only a number corresponding to the category. e.g 1"),
    ("human", question)
    ])
    
    # Use the provided LLM (Google AI) to generate the response
    
    response = llm.invoke([("system", f"Please see if there are any helpful answers through here and answer the human's question accordingly : {STATES_COMMON_QA[state][category]} "),
    ("human", question)
    ])
    
    return response

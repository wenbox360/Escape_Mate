STATES_COMMON_QA = {
    "stage1":{
            "0": "The end of the long wire with an red head should be secured into your device's port section not covered with blue tape. ",
            "1": "The buttons are used to control the LED count. The one closer to you decreases the count and the one further increases the count of LEDS.",
            "2": "Your objective is to crack the code. You can do this by adjusting the LEDS to the correct values.",
            "3": "This is not a question. Please respond back in an meangingful way."

        }
    }


def answer_questions(llm, question, brief):
    category = llm.invoke([
    ("system", "Please categorize the following question only into the following categories with no newline: "
            "0. Wire connection, 1. How to use buttons, 2. Objective. 3. Not a question Please return only a number corresponding to the category. e.g 1"),
    ("human", question)
    ])
    print(category.content)
    print("trying to strip")
    index = category.content.strip()
    # Use the provided LLM (Google AI) to generate the response
    category_value = STATES_COMMON_QA["stage1"][index]
    
    response = llm.invoke([("system", f"Please see if there are any helpful answers through here and answer the human's question accordingly : {category_value} "),
    ("human", question)
    ])
    print(response.content)
    
    return response.content

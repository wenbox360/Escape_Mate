function AnswerQuestion(brief: string, question: string, faq: string[]) -> string {
  client Groq
  prompt #"
    You are an escape room game master telling a story where:
    {{ brief }}

    A player asks this question:
    {{ question }}

    If the question is technical confer to this faq:
    {% for qa in faq %}
    - {{ qa }}
    {% endfor %}

    Otherwise, answer the question to the best of your abliity.
  "#
}
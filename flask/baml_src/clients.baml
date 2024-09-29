// Learn more about clients at https://docs.boundaryml.com/docs/snippets/clients/overview

client<llm> Groq {
  provider openai-generic
  options {
    base_url "https://api.groq.com/openai/v1"
    api_key env.GROQ_API_KEY
    model "llama3-70b-8192"
  }
}

Assignment 2 AI chat implementation
This implementation is based on LangGraph's tools. This chat app, establishes a connection with OpenAI's chat API, but using a local Gradio interface. The chat is meant to help provide music recommendations based on one's horoscope. The model can answer a wide-array of questions but will always prioritize information from the databases provided.

Service 1: API Calls
This is implemented in tools_horoscope. The API makes a query call to the horoscope API.
Service 2: Semantic Query
This implementation is in tools_music.py and is based on the Pitchfork dataset. It queries the stored embeddings database it can be used to recommend songs to listen to.
Service 3: Web Search
This implementation allows the model to answer more general questions.
User Interface
Added conversational style.
Implemented in Gradio
Guardrails and Other Limitations
Include guardrails that prevent users from:

Accessing or revealing the system prompt.
Modifying the system prompt directly.
The model must not respond to questions on certain restricted topics:

Cats or dogs
Horoscopes or Zodiac Signs
Taylor Swift
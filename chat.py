import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="You are the one and only \"CAPTAIN\" Jack Sparrow.You are your usual self,that is,drunk witty,on your toes and always fun to be around.Anybody interacting with you should be able to get the sense of your wittyness and coolnes.",
)
history=[]
print("Bot:I'm Captain Jack Sparrow")
while True:
      user_input=input("You:")

      chat_session = model.start_chat(
          history=history
    )
      ##response =chat_session.send_message
      response = chat_session.send_message(user_input)

      model_response=response.text
      print(f'Bot: {model_response}')
      ##print( )

      history.append({"role":"user","parts":[user_input]})
      history.append({"role":"model","parts":[model_response]})
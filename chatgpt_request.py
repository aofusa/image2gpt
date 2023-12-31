import openai

class ChatGPTRequest:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_request(self, text):
        try:
            client = openai.OpenAI(api_key=self.api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",  # You can use a different engine if needed
                messages=[
                    {"role": "user", "content": text},
                ],
                max_tokens=4096
            )
            print(response)
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error making request to ChatGPT: {e}")
            return e

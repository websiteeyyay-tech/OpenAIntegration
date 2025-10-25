from openai import OpenAI

class Automation:
    def __init__(self):
        self.client = OpenAI()

    def reply_to_client(self, message):
        prompt = f"""
        You are a helpful real estate assistant.
        Reply politely and informatively to this client message:
        "{message}"
        Keep the tone professional and clear.
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a real estate assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

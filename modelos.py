import openai #Importamos la librería


openai.api_key = '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'



class OpenAIModel:
    def __init__(self):
        self.conversations = []

    def generate_response(self, question):
        question_with_prompt = 'Yo: ' + question

        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = question_with_prompt,
            temperature = 0.5,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0.6
        )

        answer = 'AI: ' + response.choices[0].text.strip()

        self.conversations.append(question_with_prompt)
        self.conversations.append(answer)

        return answer

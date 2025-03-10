import flet as ft
import random


def main(page: ft.Page):
    def getResponse():
        responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes-Definetly," "You may rely on it", "As i see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Dont count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful", "Qsy", "Claro que si compai", "Yes you re the goat", "No Malisimo", "Si"]
        return random.choice(responses)

    def Ask(e):
        question = questionInput.value
        if question.strip():  
            response = getResponse()
            responseLabel.value = f"Answer: {response}"
        else:
            responseLabel.value = "ask a question."
        page.update()
    questionInput = ft.TextField(label="Ask a yes or no question")
    responseLabel = ft.Text("Answer: ", size=20)
    askButton = ft.ElevatedButton("Ask the 8-Ball", on_click=Ask)
    page.add(questionInput, askButton, responseLabel)

ft.app(main)

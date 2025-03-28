import flet as ft
import random

def main(page: ft.Page):
    page.window.height = 300
    page.window.height = 300
    page.add("Ask button", )
    page.vertical_alignment  = ft.MainAxisAlignment.END
    page.title = "Magic 8-Ball"
    responses = ["Yes", "No", "Maybe", "Ask again later", "Definitely", "Absolutely not"]
    random.randint (0,300) = responses = ["Sorry i can't help you with that", "Heck naw"]

    def ask_8_ball(e):
        response_text.value = random.choice(responses) if question_input.value.strip() else "Please enter a question."
        page.update()
    
    question_input = ft.TextField(label="Your question", width=300) 
    ask_button = ft.ElevatedButton("Ask the 8-Ball", on_click=ask_8_ball)
    response_text = ft.Text(size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE)
    page.add(ft.Column([question_input, ask_button, response_text], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER))

ft.app(target=main)

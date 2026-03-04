from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import json
from groq import Groq

client = Groq(api_key=settings.GROQ_API_KEY)


def mentor_page(request):
    return render(request, "mentor/mentor.html")


def mentor_chat(request):

    if request.method == "POST":

        data = json.loads(request.body)
        user_message = data.get("message")

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0.3,
            max_tokens=200,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI mentor for competitive programming. "
                        "Give SHORT answers (4-6 lines max). "
                        "Use bullet points when possible. "
                        "Focus on algorithms, data structures, Codeforces, LeetCode and problem solving tips. "
                        "Do NOT give long textbook explanations."
                    )
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        reply = completion.choices[0].message.content

        return JsonResponse({"reply": reply})
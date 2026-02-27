import json
from django.conf import settings
from google import genai
from google.genai import types

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generar_rutina():
    prompt = """
Generate a daily gym routine in VALID JSON format.

IMPORTANT:
- All exercise names must be written in Spanish.
- Use common commercial gym exercise names in Spanish.

The JSON structure must be EXACTLY:

{
    "upper_body": [
        {"name": "Exercise name", "sets": number, "reps": number}
    ],
    "lower_body": [
        {"name": "Exercise name", "sets": number, "reps": number}
    ]
}

STRICT RULES:

1) Output ONLY valid JSON.
2) Do NOT include explanations.
3) Do NOT include markdown.
4) Do NOT include text before or after the JSON.
5) Exactly 6 upper body exercises.
6) Exactly 5 lower body exercises.
7) Exercises must be ordered from most compound/heaviest to most accessory/lightest.
8) Compound multi-joint movements MUST appear first in each section.
9) Isolation exercises MUST appear at the end of each section.
10) Vary exercises across generations.
11) Avoid repeating the same exercise combinations frequently.
12) Use different variations of exercises when possible (e.g., barbell, dumbbell, machine).

UPPER BODY REQUIREMENTS:
- Exactly 6 exercises.
- All exercises must target torso muscles.
- Randomly choose ONE of these distributions:

Option A:
- 2 chest
- 1 back
- 1 shoulders
- 1 biceps
- 1 triceps

Option B:
- 2 back
- 1 chest
- 1 shoulders
- 1 biceps
- 1 triceps

- Include a mix of compound and accessory exercises.
- Compound exercises must have lower reps (4–8).
- Accessory exercises must have higher reps (10–15).
- Sets must be between 3 and 4.

LOWER BODY REQUIREMENTS:
- Exactly 5 exercises.
- All exercises must target lower body.
- Include:
    - 2 quad-dominant exercises (1 compound, 1 accessory)
    - 2 hamstring-dominant exercises (1 compound, 1 accessory)
    - 1 calf exercise
- Compound exercises must have lower reps (4–8).
- Accessory exercises must have higher reps (10–15).
- Sets must be between 3 and 4.

Return ONLY valid JSON.
"""

    try:
        print("Rutina de GENAI")
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=1.0,
                response_mime_type="application/json",
            ),
        )

        content = response.text.strip()
        return json.loads(content)

    except Exception as e:
        print(f"Error generating routine with Gemini: {e}")
        return rutina_fallback()


def rutina_fallback():
    print("Rutina fallback")
    return {
        "upper_body": [
            {"name": "Flexiones", "sets": 3, "reps": 12},
            {"name": "Dominadas", "sets": 3, "reps": 8},
            {"name": "Press de hombro", "sets": 3, "reps": 10},
            {"name": "Curl de bíceps", "sets": 3, "reps": 12},
            {"name": "Fondos de tríceps", "sets": 3, "reps": 12},
            {"name": "Press inclinado con mancuernas", "sets": 3, "reps": 10},
        ],
        "lower_body": [
            {"name": "Sentadillas", "sets": 4, "reps": 6},
            {"name": "Prensa de piernas", "sets": 3, "reps": 12},
            {"name": "Peso muerto rumano", "sets": 4, "reps": 6},
            {"name": "Curl femoral", "sets": 3, "reps": 12},
            {"name": "Elevaciones de talones", "sets": 4, "reps": 15},
        ],
    }
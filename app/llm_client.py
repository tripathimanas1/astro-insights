from dataclasses import dataclass
from datetime import date
from .personalisation import UserProfile, compute_personalization_score
from .rules import get_zodiac_rules
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
@dataclass
class LLMConfig:
    provider: str = "gemini"
    model_name: str = "gemini-2.0-flash-001"
    api_key_env: str = "GEMINI_API_KEY"  


class GeminiLLMClient:
    """
    Gemini LLM client for insights.
    """

    def __init__(self, config: LLMConfig | None = None):
        self.config = config or LLMConfig()

        api_key = os.getenv(self.config.api_key_env)
        if not api_key:
            raise ValueError(f"{self.config.api_key_env} is not set in environment.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(self.config.model_name)

    def build_prompt(self, profile: UserProfile) -> str:
        rules = get_zodiac_rules(profile.zodiac)

        return f"""
You are an empathetic astrologer. Produce a concise daily insight (2–3 sentences)
that reflects:

• Zodiac: {profile.zodiac}
• Core traits: {rules['core']}
• Today's theme: {rules['today']}
• Person: {profile.name}
• Birth place: {profile.birth_place}
• Date for insight: {profile.date_for}

Guidelines:
- Do NOT be fatalistic.
- Avoid health/medical predictions.
- Tone must be supportive, positive, grounded.
""".strip()

    def generate(self, profile: UserProfile) -> tuple[str, float]:
        prompt = self.build_prompt(profile)

        # personalization score (our custom logic)
        score = compute_personalization_score(profile)

        # actual Gemini call
        try:
            resp = self.model.generate_content(prompt)
            text = resp.text.strip()
        except Exception as e:
            # fallback: avoid hard crashes
            text = (
                f"{profile.name}, as a {profile.zodiac}, expect a balanced day where your natural traits "
                "help you navigate situations with clarity and confidence."
            )

        return text, score

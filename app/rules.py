from typing import Dict

# simple rules for each zodiac ( hard coded currently )
ZODIAC_TRAITS: Dict[str, Dict[str, str]] = {
    "Aries": {
        "core": "bold, action-oriented, spontaneous",
        "today": "You may feel an urge to start something new; channel it wisely."
    },
    "Taurus": {
        "core": "grounded, patient, comfort-loving",
        "today": "Stability will be your strength today; avoid unnecessary risks."
    },
    "Gemini": {
        "core": "curious, communicative, adaptable",
        "today": "Conversations and ideas could open interesting doors."
    },
    "Cancer": {
        "core": "emotional, nurturing, intuitive",
        "today": "Your sensitivity can help you connect more deeply with others."
    },
    "Leo": {
        "core": "confident, expressive, warm",
        "today": "Your natural charisma can attract attention and opportunities."
    },
    "Virgo": {
        "core": "detail-oriented, practical, analytical",
        "today": "Organizing and refining can bring surprising satisfaction."
    },
    "Libra": {
        "core": "harmonious, diplomatic, relationship-focused",
        "today": "Balancing different expectations will be your key theme."
    },
    "Scorpio": {
        "core": "intense, private, transformative",
        "today": "You might uncover hidden motives—use the insight constructively."
    },
    "Sagittarius": {
        "core": "optimistic, exploratory, freedom-loving",
        "today": "A learning or travel-related opportunity may catch your eye."
    },
    "Capricorn": {
        "core": "disciplined, goal-driven, responsible",
        "today": "Consistent effort can move you closer to a long-term goal."
    },
    "Aquarius": {
        "core": "independent, unconventional, future-focused",
        "today": "An unconventional approach could solve a nagging problem."
    },
    "Pisces": {
        "core": "empathetic, imaginative, dreamy",
        "today": "Your imagination can guide you toward healing or creativity."
    },
}


def get_zodiac_rules(zodiac: str) -> Dict[str, str]:
    return ZODIAC_TRAITS.get(zodiac, {
        "core": "unique, evolving, hard to define",
        "today": "This is a day to stay flexible and open-minded."
    })

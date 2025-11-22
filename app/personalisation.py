from datetime import time, date
from dataclasses import dataclass


@dataclass
class UserProfile:
    name: str
    birth_time: time | None
    birth_place: str | None
    zodiac: str
    date_for: date


def compute_personalization_score(profile: UserProfile) -> float:
    # just a sample personalisation score logic
    base = 0.5

    
    base += (len(profile.name) % 5) * 0.05  

    
    if profile.birth_time:
        if profile.birth_time.hour < 12:
            base += 0.1
        else:
            base += 0.05

    
    if profile.zodiac in ["Leo", "Aries", "Capricorn"]:
        base += 0.05

    
    base += (profile.date_for.weekday() % 3) * 0.03

    
    return max(0.0, min(1.0, base))

from datetime import date

# zodiac based on western sun signs
ZODIAC_RANGES = [
    ("Capricorn", (12, 22), (1, 19)),
    ("Aquarius", (1, 20), (2, 18)),
    ("Pisces", (2, 19), (3, 20)),
    ("Aries", (3, 21), (4, 19)),
    ("Taurus", (4, 20), (5, 20)),
    ("Gemini", (5, 21), (6, 20)),
    ("Cancer", (6, 21), (7, 22)),
    ("Leo", (7, 23), (8, 22)),
    ("Virgo", (8, 23), (9, 22)),
    ("Libra", (9, 23), (10, 22)),
    ("Scorpio", (10, 23), (11, 21)),
    ("Sagittarius", (11, 22), (12, 21)),
]


def _is_in_range(month: int, day: int, start: tuple[int, int], end: tuple[int, int]) -> bool:
    s_m, s_d = start
    e_m, e_d = end

    if s_m <= e_m:  
        return (month > s_m or (month == s_m and day >= s_d)) and \
               (month < e_m or (month == e_m and day <= e_d))
    else:
        
        return (month > s_m or (month == s_m and day >= s_d)) or \
               (month < e_m or (month == e_m and day <= e_d))


def infer_zodiac(birth_date: date) -> str:
    month = birth_date.month
    day = birth_date.day
    for sign, start, end in ZODIAC_RANGES:
        if _is_in_range(month, day, start, end):
            return sign
    
    return "Unknown"

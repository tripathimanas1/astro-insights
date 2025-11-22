from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from datetime import date
from .model import InsightRequest, InsightResponse, ErrorResponse
from .zodiac import infer_zodiac
from .llm_client import GeminiLLMClient
from .personalisation import UserProfile
from .translator import translate
from .cache import get_from_cache, store_in_cache


app = FastAPI(
    title="Astrological Insight Generator",
    description="Service that generates daily astrological insights from birth details.",
    version="0.1.0",
)


llm_client = GeminiLLMClient()



@app.post(
    "/insight",
    response_model=InsightResponse,
    responses={400: {"model": ErrorResponse}},
)
def generate_insight(request: InsightRequest):
    try:
        zodiac = infer_zodiac(request.birth_date)
        if zodiac == "Unknown":
            raise ValueError("Could not infer zodiac from given birth date.")

        date_for = request.date_for or date.today()

        
        cached = get_from_cache(request.name, zodiac, date_for, request.language)
        if cached:
            
            profile = UserProfile(
                name=request.name,
                birth_time=request.birth_time,
                birth_place=request.birth_place,
                zodiac=zodiac,
                date_for=date_for,
            )
            
            from .personalisation import compute_personalization_score
            score = compute_personalization_score(profile)

            return InsightResponse(
                zodiac=zodiac,
                insight=cached,
                language=request.language,
                date_for=date_for,
                personalization_score=score,
            )

        
        profile = UserProfile(
            name=request.name,
            birth_time=request.birth_time,
            birth_place=request.birth_place,
            zodiac=zodiac,
            date_for=date_for,
        )

        insight_en, score = llm_client.generate(profile)

        
        final_insight = translate(insight_en, request.language)

        
        store_in_cache(request.name, zodiac, date_for, request.language, final_insight)

        return InsightResponse(
            zodiac=zodiac,
            insight=final_insight,
            language=request.language,
            date_for=date_for,
            personalization_score=score,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    except Exception as e:
        
        raise HTTPException(status_code=500, detail="Internal server error") from e



if __name__ == "__main__":
    import argparse
    import uvicorn

    parser = argparse.ArgumentParser(description="Run Astrological Insight API server.")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    uvicorn.run("app.main:app", host=args.host, port=args.port, reload=True)

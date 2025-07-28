from fastapi import FastAPI, Request
from agents.extractor_agent import extract_requirements
from agents.recommender_agent import recommend_service
from agents.writer_agent import generate_proposal

app = FastAPI()

@app.post("/query")
async def handle_query(request: Request):
    body = await request.json()
    user_input = body['message']
    data = extract_requirements(user_input)
    service = recommend_service(data)
    proposal = generate_proposal(data, service)
    return {"response": proposal, "data": data, "service": service}

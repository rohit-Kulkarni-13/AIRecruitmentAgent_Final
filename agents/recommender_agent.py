def recommend_service(data):
    if data["industry"].lower() == "fintech" and "backend engineer" in [r.lower() for r in data["roles"]]:
        return "Tech Startup Hiring Pack"
    return "General Hiring Pack"

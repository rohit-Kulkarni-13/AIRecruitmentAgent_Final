from agents.extractor_agent import extract_requirements
from agents.recommender_agent import recommend_service
from agents.writer_agent import generate_proposal
from memory.memory_handler import store_session_data

user_input = input("Client: ")

extracted_data = extract_requirements(user_input)
recommendation = recommend_service(extracted_data)
proposal = generate_proposal(extracted_data, recommendation)

store_session_data(user_input, extracted_data, recommendation, proposal)

print("Agent:", proposal)

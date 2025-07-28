# AI Recruitment Agent

## Overview
This project is an AI-powered Sales Agent for recruitment agencies. It understands client hiring needs, recommends services, and generates proposals.

## Features
- Natural language understanding (NLU) using GPT-4
- Role and requirement extraction
- Service recommendation
- Proposal generation
- API endpoint using FastAPI
- Memory with SQLite logging

## Setup
1. Set your OpenAI API key in `.env` as `OPENAI_API_KEY=your-key`
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
python main.py
```
4. For API:
```bash
uvicorn api.app:app --reload
```

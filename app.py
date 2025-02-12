# app.py
from fastapi import FastAPI
from langcorn import create_service

app:FastAPI = create_service("agent:agent")
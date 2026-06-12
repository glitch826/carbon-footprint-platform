import os
from google import genai
from google.genai import types

class CarbonIntelligenceAgent:
    """
    Orchestrates the LLM architecture to provide real-time, context-aware
    carbon minimization strategies based on processed metrics.
    """
    def __init__(self):
        # Initializes the official SDK client; automatically picks up GEMINI_API_KEY from environment
        self.client = genai.Client()
        self.model_name = "gemini-2.5-flash"

    def generate_strategy(self, processed_context: dict) -> str:
        """
        Generates tactical optimization targets using a structured, zero-shot system prompt.
        """
        system_instruction = (
            "You are an elite Carbon Intelligence System. Your objective is to analyze "
            "the user's localized emission profile and output a precise, high-leverage optimization strategy. "
            "Be direct, action-oriented, and base all recommendations strictly on the provided quantitative data."
        )

        user_content = f"Analyze this user profile data and provide optimization targets: {processed_context}"

        config = types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.2, # Low temperature ensures strict logical adherence, minimizing hallucination
            max_output_tokens=800
        )

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=user_content,
                config=config
            )
            return response.text
        except Exception as e:
            return f"Execution error during agent logical inference: {str(e)}"
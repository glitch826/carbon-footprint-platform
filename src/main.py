import os
from dotenv import load_dotenv
from src.context_manager import CarbonContextManager
from src.agent import CarbonIntelligenceAgent 
load_dotenv()

def run_platform_pipeline(raw_user_input: dict) -> dict:
    """
    Executes the end-to-end data processing and intelligent inference pipeline.
    """
    # 1. Process context and calculate impact metrics
    context_handler = CarbonContextManager(raw_user_input)
    calculated_metrics = context_handler.process_user_metrics()
    
    # 2. Feed structured data into the reasoning engine
    ai_agent = CarbonIntelligenceAgent()
    tactical_strategy = ai_agent.generate_strategy(calculated_metrics)
    
    return {
        "metrics": calculated_metrics,
        "optimization_strategy": tactical_strategy
    }

if __name__ == "__main__":
    # Mock context payload simulating real-world platform ingestion
    sample_user = {
        "location": "Varanasi, India",
        "transport_mode": "petrol_car",
        "daily_distance_km": 25,
        "diet": "vegetarian"
    }
    
    print("Initializing Carbon Intelligence Engine pipeline...\n")
    output = run_platform_pipeline(sample_user)
    
    print(f"--- LOCALIZED METRICS ({output['metrics']['user_location']}) ---")
    print(f"Calculated Daily Impact: {output['metrics']['total_co2_kg']} kg CO2")
    print(f"Breakdown: {output['metrics']['breakdown']}\n")
    print("--- GENERATED OPTIMIZATION STRATEGY ---")
    print(output['optimization_strategy'])
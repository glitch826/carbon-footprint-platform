from typing import Dict, Any

class CarbonContextManager:
    """Manages and categorizes user context for customized carbon intelligence calculation."""
    
    def __init__(self):
        self.supported_sectors = ["household", "corporate", "manufacturing"]

    def process_user_context(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validates and enriches user context data to enable logical decision-making.
        """
        sector = raw_data.get("sector", "household").lower()
        if sector not in self.supported_sectors:
            sector = "household"
            
        # Structure the context dictionary with strict defaults for the agent
        enriched_context = {
            "sector": sector,
            "region": raw_data.get("region", "Global"),
            "energy_usage_kwh": float(raw_data.get("energy_usage_kwh", 0.0)),
            "transport_miles": float(raw_data.get("transport_miles", 0.0)),
            "waste_kg": float(raw_data.get("waste_kg", 0.0)),
            "scale_factor": 1.5 if sector == "manufacturing" else (1.2 if sector == "corporate" else 1.0)
        }
        return enriched_context
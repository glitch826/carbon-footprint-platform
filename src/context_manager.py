class CarbonContextManager:
    """
    Manages and parses dynamic user context profiles to compute localized 
    carbon footprints with O(1) calculation efficiency.
    """
    def __init__(self, user_profile: dict):
        self.user_profile = user_profile
        
        # Standardized emission constants (kg CO2 per unit metric)
        self.emission_factors = {
            "transport": {
                "electric_vehicle": 0.05,
                "public_transit": 0.08,
                "petrol_car": 0.22,
                "diesel_car": 0.25,
                "walk_or_cycle": 0.00
            },
            "diet": {
                "vegan": 1.5,
                "vegetarian": 2.0,
                "non_vegetarian": 4.5
            }
        }

    def process_user_metrics(self) -> dict:
        """
        Extracts user features and maps them to emission baselines dynamically.
        """
        location = self.user_profile.get("location", "Global")
        transport = self.user_profile.get("transport_mode", "walk_or_cycle")
        distance = float(self.user_profile.get("daily_distance_km", 0))
        diet = self.user_profile.get("diet", "vegetarian")

        # High-speed safe lookup map
        transport_impact = self.emission_factors["transport"].get(transport, 0.0) * distance
        diet_impact = self.emission_factors["diet"].get(diet, 2.0)
        
        total_score = transport_impact + diet_impact

        return {
            "user_location": location,
            "total_co2_kg": round(total_score, 2),
            "breakdown": {
                "transportation_co2": round(transport_impact, 2),
                "diet_co2": round(diet_impact, 2)
            }
        }
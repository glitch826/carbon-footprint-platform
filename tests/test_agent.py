import pytest
from src.context_manager import CarbonContextManager

def test_context_manager_math_precision():
    """
    Verifies that the O(1) engine maps and calculates metrics correctly.
    """
    mock_input = {
        "location": "Delhi, India",
        "transport_mode": "electric_vehicle",
        "daily_distance_km": 10,
        "diet": "vegan"
    }
    
    manager = CarbonContextManager(mock_input)
    results = manager.process_user_metrics()
    
    # Expected: (0.05 factor * 10km) + 1.5 diet factor = 2.00 kg
    assert results["total_co2_kg"] == 2.00
    assert results["breakdown"]["transportation_co2"] == 0.50
    assert results["breakdown"]["diet_co2"] == 1.50
    assert results["user_location"] == "Delhi, India"
import unittest
from src.context_manager import CarbonContextManager

class TestCarbonIntelligencePipeline(unittest.TestCase):
    
    def setUp(self):
        self.manager = CarbonContextManager()

    def test_household_context_parsing(self):
        raw_data = {"sector": "household", "region": "Delhi", "energy_usage_kwh": "350"}
        processed = self.manager.process_user_context(raw_data)
        
        self.assertEqual(processed["sector"], "household")
        self.assertEqual(processed["region"], "Delhi")
        self.assertEqual(processed["scale_factor"], 1.0)

    def test_manufacturing_scale_logic(self):
        raw_data = {"sector": "manufacturing", "energy_usage_kwh": "12000"}
        processed = self.manager.process_user_context(raw_data)
        
        self.assertEqual(processed["sector"], "manufacturing")
        self.assertEqual(processed["scale_factor"], 1.5)

if __name__ == '__main__':
    unittest.main()
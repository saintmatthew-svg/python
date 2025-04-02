import unittest
import AirConditioner

class TestAirConditioner(unittest.TestCase):
    
    def test_ac_is_on(self):
        expected = AirConditioner.TurnOn()
        result = True
        self.assertEqual(expected, result)

    def test_ac_is_off(self):
        expected = AirConditioner.TurnOff()
        result = False
        self.assertEqual(expected, result)    

    def test_ac_can_increase(self):
        AirConditioner.TurnOn()
        Temperature = 16
        AirConditioner.Increase(Temperature)
        result = 17
        expected = AirConditioner.Increase(Temperature)
        self.assertEqual(expected, result)  

    def test_temperature_can_decrease(self):
        AirConditioner.TurnOn()
        Temperature = 22
        AirConditioner.Decrease(Temperature)
        result = 21
        expected = AirConditioner.Decrease(Temperature)
        self.assertEqual(expected, result) 

    def test_ac_cannot_decrease_below_sixteen(self):
        AirConditioner.TurnOn()
        Temperature = 16
        AirConditioner.Decrease(Temperature)
        result = 16
        expected = AirConditioner.Decrease(Temperature)
        self.assertEqual(expected, result)     

    def test_temperature_can_not_go_above_thirty(self):
        AirConditioner.TurnOn()
        Temperature = 30
        AirConditioner.Increase(Temperature)
        result = 30
        expected = AirConditioner.Increase(Temperature)
        self.assertEqual(expected, result) 


if __name__ == "__main__":
    unittest.main()
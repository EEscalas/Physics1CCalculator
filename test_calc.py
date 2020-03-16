import calc
import unittest

class TestCalculator(unittest.TestCase):

    # CHAPTER 27

    def test_motion_in_magnetic_field(self):
        self.assertTrue(calc.motionInMagneticField(1,2,3,4,"?") == "b = 1.5")

    def test_hall_effect(self):
        self.assertTrue(calc.hallEffect("?",-1,4,1,2) == "n = 2.0")

    def test_magnetic_torque(self):
        self.assertTrue(False)

    def test_magnetic_potential_energy(self):
        self.assertTrue(False)

    # CHAPTER 28

    # CHAPTER 30

    # CHAPTER 31

    # CHAPTER 32

    # CHAPTER 33

    # CHAPTER 34
    
    # CHAPTER 35

    # CHAPTER 36
    def test_single_slit_diffraction(self):
        self.assertTrue(False)
    
    def test_single_slit_diffraction_intensity(self):
        self.assertEqual(calc.singleSlitDiffractionIntensity("?","3.5","14","3.375","4 degrees"),"I = 2.6360781362135635")

    # CHAPTER 37

    def test_time_dilation(self):
        self.assertTrue(False)
    
    def test_time_dilation(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
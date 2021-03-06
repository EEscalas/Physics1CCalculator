import calc
import unittest

class TestCalculator(unittest.TestCase):

    # CHAPTER 27

    def test_motion_in_magnetic_field(self):
        self.assertTrue(calc.motionInMagneticField(1,2,3,4,"?") == "b = 1.5")

    def test_hall_effect(self):
        self.assertTrue(calc.hallEffect("?",-1,4,1,2) == "n = 2.0")
    """
    def test_magnetic_torque(self):
        self.assertTrue(False)

    def test_magnetic_potential_energy(self):
        self.assertTrue(False)
    """
    # CHAPTER 28

    # CHAPTER 30

    # CHAPTER 31

    # CHAPTER 32

    # CHAPTER 33

    def test_law_of_refraction(self):
        self.assertTrue(calc.lawOfRefraction(1,1.43955,"35 degrees","?") == "theta (b) = 0.40981699395033455 rad")

    # CHAPTER 34
    
    def test_focal_length(self):
        self.assertTrue(calc.focalLength(0.3,"?") == "F = 0.15")

    def test_distances_plane_refracting(self):
        self.assertTrue(calc.distancesPlaneRefracting(1.309,1,0.039,"?") == "s' = -0.029793735676088617")

    # CHAPTER 35

    # CHAPTER 36
    """
    def test_single_slit_diffraction(self):
        self.assertTrue(False)
    """
    def test_single_slit_diffraction_intensity(self):
        self.assertEqual(calc.singleSlitDiffractionIntensity("?","3.5","14","3.375","4 degrees","t"),"I = 2.6360781362135635")

    # CHAPTER 37

    def test_gamma_calculations(self):
        gamma = calc.getGamma(0.5)
        self.assertTrue(calc.udivcFromGamma(gamma) == 0.5000000000000002)

    def test_time_dilation(self):
        self.assertTrue(calc.timeDilation("?",5,0.5) == "t = 5.773502691896258")

    # OTHER

    def test_wave(self):
        self.assertTrue(calc.wave("?",2,3) == "v = 6.0")
        self.assertTrue(calc.wave(10,5,"?") == "wavelength = 2.0")
    """
    def test_cross_product(self):
        self.assertTrue(calc.crossProduct("+x","+y","?") == "+x x +y = +z")
    """

if __name__ == '__main__':
    unittest.main()
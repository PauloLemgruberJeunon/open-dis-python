import unittest
from math import sqrt

from distributed_interactive_simulation.RangeCoordinates import WGS84

class WGS84TestCase(unittest.TestCase):
    def setUp(self):
        self.wgs84 = WGS84()

    def test_wgs84_parameters(self):
        semi_major_axis_length = 6378137.0
        semi_minor_axis_length = 6356752.3142
        ellipsoid_flatness = (semi_major_axis_length - semi_minor_axis_length) / semi_major_axis_length
        eccentricity = sqrt(ellipsoid_flatness * (2 - ellipsoid_flatness))
        speed_of_light = 299792458.
        relativistic_const = -4.442807633e-10
        earths_gravitational_const = 3.986005e14
        earths_rotation_rate_radps = 7.2921151467e-5

        self.assertEqual(self.wgs84.a, semi_major_axis_length)
        self.assertEqual(self.wgs84.b, semi_minor_axis_length)
        self.assertEqual(self.wgs84.f, ellipsoid_flatness)
        self.assertEqual(self.wgs84.e, eccentricity)
        self.assertEqual(self.wgs84.c, speed_of_light)
        self.assertEqual(self.wgs84.F, relativistic_const)
        self.assertEqual(self.wgs84.mu, earths_gravitational_const)
        self.assertEqual(self.wgs84.omega_ie, earths_rotation_rate_radps)

    def test_wgs84_g0(self):
        L = 1
        result = self.wgs84.g0(L)
        expected_result = 9.816999687123264

        self.assertAlmostEqual(result, expected_result, places=6)

        
import unittest
from numpy.testing import assert_almost_equal

from distributed_interactive_simulation.RangeCoordinates import WGS84, GPS
import distributed_interactive_simulation.RangeCoordinates as rc


class GPSTestCase(unittest.TestCase):
    def setUp(self):
        self.gps = GPS()

        self.base_origin = '1000 1000 1000'

        self.base_lla = (
            34.0 + 0/60.0 + 0.00174/3600.0,
            -117.0 - 20.0/60.0 - 0.84965/3600.0,
            251.702
        )

        self.base_ecef = (
            -2430601.827677528,
            -4702442.70311117,
            3546587.3581588385
        )

        self.base_utm = (
            [469195.5283320455, 3762206.1743781692, 251.702],
            ['11S', 0.9996116971859619]
        )

        self.base_ned = (
            3422336.353523082,
            -1606434.088795911,
            5129642.66064011
        )

        self.base_pae = (
            6372303.38450314,
            -25.14521518145129,
            -53.6093223012941
        )

        self.base_gcc = (
            -2623583.7362721274,
            -3607987.9133834727,
            9807115.126894707
        )

    def tearDown(self):
        pass

    def assert_utm(self, utm):
        assert_almost_equal(utm[0], self.base_utm[0], 6)
        self.assertEqual(utm[1][0], self.base_utm[1][0])
        self.assertAlmostEqual(utm[1][1], self.base_utm[1][1], 6)

    def test_gps_params(self):
        f_gps = 1023
        f_l1 = f_gps * 1.54e6
        f_l2 = f_gps * 1.2e6

        self.assertEqual(f_gps, self.gps.fGPS)
        self.assertEqual(f_l1, self.gps.fL1)
        self.assertEqual(f_l2, self.gps.fL2)

    def test_lla2ecef(self):
        ecef = self.gps.lla2ecef(self.base_lla)
        assert_almost_equal(ecef, self.base_ecef, 6)

    def test_lla2utm(self):
        utm = self.gps.lla2utm(self.base_lla)
        self.assert_utm(utm)

    def test_ecef2lla(self):
        lla = self.gps.ecef2lla(self.base_ecef)
        assert_almost_equal(lla, self.base_lla, 6)       

    def test_ecef2utm(self):
        utm = self.gps.ecef2utm(self.base_ecef)
        self.assert_utm(utm)

    def test_ecef2ned(self):
        base_ori = [float(x) for x in self.base_origin.split(' ')]
        ned = self.gps.ecef2ned(self.base_ecef, base_ori)
        assert_almost_equal(ned, list(self.base_ned), 6)

    def test_ecef2pae(self):
        base_ori = [float(x) for x in self.base_origin.split(' ')]
        pae = self.gps.ecef2pae(self.base_ecef, base_ori)
        assert_almost_equal(pae, self.base_pae, 6)

    def test_ned2ecef(self):
        base_ori = [float(x) for x in self.base_origin.split(' ')]
        ecef = self.gps.ned2ecef(self.base_ned, base_ori)
        assert_almost_equal(ecef, self.base_ecef, 6)
    
    def test_ned2pae(self):
        pae = self.gps.ned2pae(self.base_ned)
        assert_almost_equal(pae, list(self.base_pae), 6)
    
    def test_lla2gcc(self):
        gcc = self.gps.lla2gcc(self.base_lla, self.base_origin)
        assert_almost_equal(gcc, self.base_gcc, 6)

    def test_euclidian_distance(self):
        p = rc.euclideanDistance(self.base_ned)
        self.assertAlmostEqual(p, 6372303.38450314, 6)
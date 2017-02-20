import geometry
from geometry import Spoke
from unittest import TestCase
import math


class TestIntersect(TestCase):

    def test_not_intersect(self):

        spoke = Spoke(0.463647609, 10, 10, 1)
        spoke.x = 8
        spoke.y = 9

        seg1 = (1, 4)
        seg2 = (3, 2)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))


    def test_not_intersect_blue_green(self):

        spoke = Spoke(2.5132741228718345, 66, 111, 1)
        spoke.x = 67.76335575687743
        spoke.y = 108.57294901687517

        seg1 = (233.0, 109.0)
        seg2 = (234.7633557568774, 108.42705098312483)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))



    def test_does_not_intersect_diag1(self):

        spoke = Spoke(math.pi, 5, 2.01, 1)
        spoke.x = 5
        spoke.y = 5.011

        seg1 = (3, 7.01)
        seg2 = (8, 7.09)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))


        spoke = Spoke(0, 5, 5.02, 1)
        spoke.x = 5.012
        spoke.y = 2.0

        seg1 = (3.02, 7.23)
        seg2 = (8.12, 7.12)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))




    def test_does_not_intersect_diag2(self):

        spoke = Spoke(0, 12, 2, 1)
        spoke.x = 12
        spoke.y = 5

        seg1 = (13, 7)
        seg2 = (15, 7)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))


    def test_does_not_intersect_diag3(self):

        spoke = Spoke((math.pi / 4), 4, 14, 1)
        spoke.x = 6
        spoke.y = 12

        seg1 = (5, 11)
        seg2 = (7, 9)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))


    def test_does_not_intersect_diag4(self):

        spoke = Spoke(math.pi /4, 14, 10.001, 1)
        spoke.x = 16
        spoke.y = 9

        seg1 = (15, 11.0001)
        seg2 = (17, 13)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))


    # def test_also_does_intersect(self):
    #
    #     spoke = Spoke(0.463647609, 10, 10)
    #     spoke.x = 8
    #     spoke.y = 9
    #
    #     seg1 = (9, 9)
    #     seg2 = (8, 9.5)
    #
    #     self.assertTrue(geometry.intersect(spoke, seg1, seg2))



    def test_parallel_intersect_start_same_place(self):

        spoke = Spoke(0.463647609, 10, 10, 1)
        spoke.x = 8
        spoke.y = 9

        seg1 = (8, 9)
        seg2 = (10, 10)

        self.assertTrue(geometry.intersect(spoke, seg1, seg2))


    def test_parallel_intersect_spoke_envelopes(self):

        spoke = Spoke(0.463647609, 10, 10, 1)
        spoke.x = 6
        spoke.y = 8

        seg1 = (8, 9)
        seg2 = (10, 10)

        self.assertTrue(geometry.intersect(spoke, seg1, seg2))



    def test_square_intersect(self):

        spoke = Spoke(math.pi / 2, 2.1, 2.1111, 1)
        spoke.x = 4.0010101
        spoke.y = 2.12

        seg1 = (3.011, 2.1553534)
        seg2 = (3.01434, 4.213132)

        self.assertTrue(geometry.intersect(spoke, seg1, seg2))




    def test_diagonal_intersect(self):

        #spokeangle =
        spoke = Spoke(math.pi / 4, 2.1, 2.1, 1)
        spoke.x = 4.2
        spoke.y = 4.2

        seg1 = (4.001, 2.001)
        seg2 = (2.002323, 4.23123)

        self.assertTrue(geometry.intersect(spoke, seg1, seg2))



    def test_square_diagonal_intersect(self):

        spoke = Spoke(math.pi / 4, 2, 2, 1)
        spoke.x = 4
        spoke.y = 4

        seg1 = (2, 3)
        seg2 = (4, 3)

        self.assertTrue(geometry.intersect(spoke, seg1, seg2))



    def test_atan(self):

        # AAAAAAAAAAAAA

        d45 = math.pi / 4
        d90 = math.pi / 2
        d180 = math.pi
        d270 = d180 + d90

        res = geometry.atan(1, 0)
        self.assertAlmostEqual(res, math.pi/2)   #90deg

        res = geometry.atan(1, 1)
        self.assertAlmostEqual(res, math.pi/4)   #45deg

        res = geometry.atan(1, -1)
        self.assertAlmostEqual(res, d90+d45)  #90+45  F

        res = geometry.atan(-1, 0)
        self.assertAlmostEqual(res, d270)  #270

        res = geometry.atan(-1, 1)
        self.assertAlmostEqual(res, d270+d45)  #270+45   F

        res = geometry.atan(-1, -1)
        self.assertAlmostEqual(res, d180+d45)  #180+45  F

        res = geometry.atan(0, 0)
        self.assertAlmostEqual(res, 0)    #F


    def test_atan_not_45(self):

        # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

        d45 = math.pi / 4
        d90 = math.pi / 2
        d180 = math.pi
        d270 = d180 + d90

        big_angle = math.atan(2) #1.107148717794
        small_angle = math.atan(0.5) #0.463647609

        res = geometry.atan(2, 0)
        self.assertAlmostEqual(res, math.pi/2)   #90deg

        res = geometry.atan(2, 1)
        self.assertAlmostEqual(res, big_angle)   #45deg

        res = geometry.atan(2, -1)
        self.assertAlmostEqual(res, (math.pi/2) + small_angle)  #90+smol  F

        res = geometry.atan(-2, 0)
        self.assertAlmostEqual(res, d270)  #270

        res = geometry.atan(-2, -1)
        self.assertAlmostEqual(res, d180 + big_angle)

        res = geometry.atan(-2, 1)
        self.assertAlmostEqual(res, d270 + small_angle)

        res = geometry.atan(0, 0)
        self.assertAlmostEqual(res, 0)





if __name__ == '__main__':
    unittest.main()

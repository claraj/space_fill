import geometry
from geometry import Spoke
from unittest import TestCase
import math


class TestIntersect(TestCase):

    def test_not_intersect(self):

        spoke = Spoke(0.463647609, 10, 10)
        spoke.x = 8
        spoke.y = 9

        seg1 = (1, 4)
        seg2 = (3, 2)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))


    def test_not_intersect_blue_green(self):

        spoke = Spoke(2.5132741228718345, 66, 111)
        spoke.x = 67.76335575687743
        spoke.y = 108.57294901687517

        seg1 = (233.0, 109.0)
        seg2 = (234.7633557568774, 108.42705098312483)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))



    def test_does_not_intersect_diag1(self):

        spoke = Spoke(math.pi, 5, 2)
        spoke.x = 5
        spoke.y = 5

        seg1 = (3, 7)
        seg2 = (8, 7)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))


        spoke = Spoke(0, 5, 5)
        spoke.x = 5
        spoke.y = 2

        seg1 = (3, 7)
        seg2 = (8, 7)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))




    def test_does_not_intersect_diag2(self):

        spoke = Spoke(0, 12, 2)
        spoke.x = 12
        spoke.y = 5

        seg1 = (13, 7)
        seg2 = (15, 7)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))


    def test_does_not_intersect_diag3(self):

        spoke = Spoke((math.pi / 4), 4, 14)
        spoke.x = 6
        spoke.y = 12

        seg1 = (5, 11)
        seg2 = (7, 9)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))


    def test_does_not_intersect_diag4(self):

        spoke = Spoke(math.pi /4, 14, 10)
        spoke.x = 16
        spoke.y = 9

        seg1 = (15, 11)
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

        spoke = Spoke(0.463647609, 10, 10)
        spoke.x = 8
        spoke.y = 9

        seg1 = (8, 9)
        seg2 = (10, 10)

        self.assertTrue(geometry.intersect(spoke, seg1, seg2))


    def test_parallel_intersect_spoke_envelopes(self):

        spoke = Spoke(0.463647609, 10, 10)
        spoke.x = 6
        spoke.y = 8

        seg1 = (8, 9)
        seg2 = (10, 10)

        self.assertTrue(geometry.intersect(spoke, seg1, seg2))



if __name__ == '__main__':
    unittest.main()

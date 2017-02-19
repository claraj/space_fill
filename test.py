import geometry
from geometry import Spoke
from unittest import TestCase


class TestIntersect(TestCase):

    def test_not_intersect(self):

        spoke = Spoke(0.463647609, 10, 10)
        spoke.x = 8
        spoke.y = 9

        seg1 = (1, 4)
        seg2 = (3, 2)

        self.assertFalse(geometry.intersect(spoke, seg1, seg2))



    def test_does_intersect(self):

        spoke = Spoke(0.463647609, 10, 10)
        spoke.x = 8
        spoke.y = 9

        seg1 = (9, 9)
        seg2 = (8, 9.5)

        self.assertTrue(geometry.intersect(spoke, seg1, seg2))


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

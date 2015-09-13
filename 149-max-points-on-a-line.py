# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
import unittest
import timeit

# Definition for a point.
class Point(object):
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution(object):
    """
    It takes 76ms for this solution.
    """
    def maxPoints(self, points):
        from collections import defaultdict

        l = len(points)
        m = 0
        d = defaultdict(lambda: 1)
        while points:
            p1 = points.pop()
            d.clear()
            d[float('inf')] = 1
            dup_count = 0
            
            if m > (len(points)) + 1:
                break
            
            for p2 in points:
                if p1.x == p2.x and p1.y == p2.y: 
                    dup_count += 1
                    continue
                if p1.x == p2.x: 
                    slope = float('inf')
                else:
                    slope = float(p2.y - p1.y)/(p2.x - p1.x)
                d[slope] += 1

            m = max(m, max(d.values()) + dup_count)
        return m


class SlowSolution(object):
    """
    My 1st trial on this problem, it took 128 ms to complete all the test cases.
    """
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        from math import sqrt
        from collections import defaultdict
        slopes = dict()
        max_points = max_counts = 0

        if not points: # no point
            return 0

        dup_point_count = dict()
        unique_points = []
        for i, p in enumerate(points):
            if (p.x, p.y) not in dup_point_count:
                dup_point_count[(p.x, p.y)] = 0
                unique_points.append(p)
            else:
                dup_point_count[(p.x, p.y)] += 1
        
        if len(unique_points) == 1:
            return len(points)

        while unique_points:
            p1 = unique_points.pop()
            for p2 in unique_points:

                if (p2.x == p1.x):
                    if (p2.y != p1.y):
                        m = float('inf')
                else:
                    m = float(p2.y - p1.y)/(p2.x - p1.x)
                    
                if m not in slopes:
                    slopes[m] = defaultdict(list)
                
                d = slopes[m]
                match_line = False
                for k, v in d.items():
                    if k[0] == p1.x:
                        m2 = float('inf')
                    else:
                        m2 = float(k[1]-p1.y)/(k[0] - p1.x)
                    
                    if m == m2:
                        match_line = True
                        l = v
                        break

                if not match_line:
                    l = slopes[m][(p1.x, p1.y)] = list()

                if p1 not in l:
                    l.append(p1)
                if p2 not in l:
                    l.append(p2)
                        
        for v in slopes.values():
            ll = v.values()
            for l in ll:
                scores = len(l)
                for p in l:
                    if (p.x, p.y) in dup_point_count:
                        scores += dup_point_count[(p.x, p.y)]
                        
                if scores > max_points:
                    max_points = scores
                
        return max_points

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_case0(self):
        l = []
        self.assertEqual(0, self.solution.maxPoints(l))

    def test_case1(self):
        l = [ Point(0, 0),
              Point(1, 1),
              Point(2, 2)
            ]
        self.assertEqual(3, self.solution.maxPoints(l))

    def test_case2(self):
        l = [ Point(0, 0),
              Point(1, 1),
              Point(5, 0),
              Point(2, 2),
              Point(-1, -1),
              Point(3, 1)
            ]
        self.assertEqual(4, self.solution.maxPoints(l))

    def test_case3(self):
        l = [ Point(0, 0),
              Point(1, 2),
              Point(2, 1)
            ]
        self.assertEqual(2, self.solution.maxPoints(l))

    def test_case4(self):
        l = [ Point(2, 2),
              Point(2, 2),
              Point(2, 2)
            ]
        self.assertEqual(3, self.solution.maxPoints(l))

    def test_case5(self):
        l = [Point(2, 2)]
        self.assertEqual(1, self.solution.maxPoints(l))

    def test_case6(self):
        l = [ Point(0, 0),
              Point(1, 1),
              Point(0, 0)
            ]
        self.assertEqual(3, self.solution.maxPoints(l))

    def test_case7(self):
        l = [ Point(0, 0),
              Point(0, 0)
            ]
        self.assertEqual(2, self.solution.maxPoints(l))

    def test_case8(self):
        test_cases = [[0,9],[138,429],[115,359],[115,359],[-30,-102],[230,709],[-150,-686],[-135,-613],[-60,-248],[-161,-481],[207,639],[23,79],[-230,-691],[-115,-341],[92,289],[60,336],[-105,-467],[135,701],[-90,-394],[-184,-551],[150,774]]
        l = [ Point(x[0], x[1]) for x in test_cases]
        self.assertEqual(12, self.solution.maxPoints(l))

    def test_case9(self):
        test_cases = [[0,-12],[5,2],[2,5],[0,-5],[1,5],[2,-2],[5,-4],[3,4],[-2,4],[-1,4],[0,-5],[0,-8],[-2,-1],[0,-11],[0,-9]]
        l = [ Point(x[0], x[1]) for x in test_cases]
        self.assertEqual(6, self.solution.maxPoints(l))
        

    def test_case10(self):
        test_cases = [[-4,-4],[-8,-582],[-3,3],[-9,-651],[9,591]]
        l = [ Point(x[0], x[1]) for x in test_cases]
        self.assertEqual(3, self.solution.maxPoints(l))
    
    def test_case19(self):
        test_cases = [[3,1],[12,3],[3,1],[-6,-1]]
        l = [ Point(x[0], x[1]) for x in test_cases]
        self.assertEqual(4, self.solution.maxPoints(l))
    
    def test_case26(self):
        test_cases = [[4,0],[4,-1],[4,5]]
        l = [ Point(x[0], x[1]) for x in test_cases]
        self.assertEqual(3, self.solution.maxPoints(l))

    def test_case27(self):
        test_cases = [[0,-12],[5,2],[2,5],[0,-5],[1,5],[2,-2],[5,-4],[3,4],[-2,4],[-1,4],[0,-5],[0,-8],[-2,-1],[0,-11],[0,-9]]
        l = [ Point(x[0], x[1]) for x in test_cases]
        self.assertEqual(6, self.solution.maxPoints(l))
        
if __name__ == '__main__':
    unittest.main() 
    # suite = unittest.TestSuite()
    # suite.addTest(MyTestCase("test_case26"))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    
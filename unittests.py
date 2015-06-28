import unittest
import pysphere

class TestModule(unittest.TestCase):
  def test_haversine_00(self):
      self.assertAlmostEqual(pysphere.haversine(52.516288, 13.377689, 52.519198, 13.379453), 0.3448896)

  def test_haversine_01(self):
      self.assertAlmostEqual(pysphere.haversine(52.516288, 13.377689, 52.516288, 13.377689), 0)

  def test_bearing(self):
      self.assertAlmostEqual(pysphere.bearing(52.516288, 13.377689, 52.519198, 13.379453), 20.24698, places=5)

  def test_cross_track_distance(self):
      self.assertAlmostEqual(pysphere.cross_track_distance(52.516288, 13.377689, 52.590117, 13.39915, 52.437385, 13.553989), 5.552993, places=6)

if __name__ == '__main__':
    unittest.main()

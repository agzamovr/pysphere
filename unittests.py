import unittest
import pysphere

class TestModule(unittest.TestCase):
  def test_haversine_00(self):
      self.assertAlmostEqual(pysphere.haversine(p1 = (52.516288, 13.377689), p2 = (52.519198, 13.379453)), 0.3448896)

  def test_haversine_01(self):
      self.assertAlmostEqual(pysphere.haversine(p1 = (52.516288, 13.377689), p2 = (52.516288, 13.377689)), 0)

  def test_haversine_02(self):
      p1 = (52.516288, 13.377689)
      p2 = (52.519198, 13.379453)
      self.assertAlmostEqual(pysphere.haversine(p1, p2), pysphere.haversine(p2, p1))

  def test_bearing_00(self):
      self.assertAlmostEqual(pysphere.bearing((52.516288, 13.377689), (52.519198, 13.379453)), 20.24698, places=5)

  def test_bearing_01(self):
      self.assertAlmostEqual(pysphere.bearing(p2 = (52.519198, 13.379453), p1 = (52.516288, 13.377689)), 20.24698, places=5)

  def test_cross_track_distance(self):
      p = (52.516288, 13.377689)
      p_start = (52.590117, 13.39915)
      p_end = (52.437385, 13.553989)
      self.assertAlmostEqual(pysphere.cross_track_distance(p_start, p_end, p), 5.552993, places=6)

  def test_along_track_distance(self):
      p = (52.516288, 13.377689)
      p_start = (52.590117, 13.39915)
      p_end = (52.437385, 13.553989)
      self.assertAlmostEqual(pysphere.along_track_distance(p_start, p_end, p), 6.218037, places=6)

  def test_line_length_01(self):
      p1 = (52.529198, 13.274099)
      p2 = (52.531835, 13.29234)
      p3 = (52.522116, 13.298541)
      p4 = (52.520569,13.317349)
      self.assertAlmostEqual(pysphere.line_length((p1, p2, p3, p4)),
                             pysphere.haversine(p1, p2) + pysphere.haversine(p2, p3) + pysphere.haversine(p3, p4)
                             , places=6)

  def test_distance_to_segment_00(self):
      p         = (52.516288, 13.377689)
      p_start   = (52.590117, 13.39915)
      p_end     = (52.437385, 13.553989)
      self.assertAlmostEqual(pysphere.distance_to_segment(p_start, p_end, p),
                             pysphere.cross_track_distance(p_start, p_end, p),
                             places=6)

  def test_distance_to_segment_01(self):
      p         = (52.516288, 13.377689)
      p1        = (52.529198, 13.274099)
      p2        = (52.531835, 13.29234)
      self.assertAlmostEqual(pysphere.distance_to_segment(p1, p2, p),
                             pysphere.haversine(p2, p),
                             places=6)

  def test_distance_to_segment_02(self):
      p         = (52.516288, 13.377689)
      p1        = (52.522462, 13.392328)
      p2        = (52.520921, 13.399703)
      self.assertAlmostEqual(pysphere.distance_to_segment(p1, p2, p),
                             pysphere.haversine(p1, p),
                             places=6)

if __name__ == '__main__':
    unittest.main()

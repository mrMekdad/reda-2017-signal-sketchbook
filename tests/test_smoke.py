import unittest
from signal_sketchbook.core import build_snapshot


class SmokeTest(unittest.TestCase):
    def test_signature(self):
        snapshot = build_snapshot()
        self.assertEqual(snapshot["author"], "Red@")


if __name__ == "__main__":
    unittest.main()

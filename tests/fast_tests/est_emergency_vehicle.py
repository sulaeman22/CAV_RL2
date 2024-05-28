import unittest
from GRL_Envs import EVSpecificEnv

class TestEmergencyVehicle(unittest.TestCase):
    def setUp(self):
        self.env = EVSpecificEnv()

    def test_reset(self):
        obs = self.env.reset()
        self.assertEqual(obs.shape, (84, 84, 3))

    def test_step(self):
        self.env.reset()
        obs, reward, done, info = self.env.step(1)
        self.assertEqual(obs.shape, (84, 84, 3))
        self.assertIsInstance(reward, float)
        self.assertIsInstance(done, bool)
        self.assertIsInstance(info, dict)

if __name__ == '__main__':
    unittest.main()

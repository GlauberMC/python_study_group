  # -*- coding: utf-8 -*-
import unittest

class TestBackjack(unittest.TestCase):

    def setUp(self):
        print('Entrou no setup')

    def test_error(self):
        self.assertEqual(True, False)

    def test_problem(self):
        self.assertEqual(True, False)

    def tearDown(self):
        print('Entrou no tearDown')

if __name__ == '__main__':
     unittest.main()

import unittest
import numpy as np
from typing import List

from pyECSS.Entity import Entity
from pyECSS.Component import Component, BasicTransform, Camera, ComponentDecorator, RenderMesh, CompNullIterator, VectorQuaternion_BasicTransformDecorator

import pyECSS.utilities as util

class TestComponent(unittest.TestCase):
    
    def test_init(self):
        """
        Entity init() test
        """
        print("TestComponent:test_init() START")
        
        gameComponent = BasicTransform("Transform", "TRS", 201)
        gameComponent2 = VectorQuaternion_BasicTransformDecorator("Transform2", "TRS2", 202)
        
        #self.assertEqual(gameComponent.rotationEulerAngles, gameComponent2.rotate())
        
    def test_rotation_matrix_to_quaternion(self):
        
        gameComponent2 = VectorQuaternion_BasicTransformDecorator("Transform2", "TRS2", 202)
        
        rot_v = np.array([1,1,1])
        a = gameComponent2.rotate_vector(rot_v)
        b = np.array([1.0000,    1.0000,    1.0000])
        a = np.array([round(a[0], 4),round(a[1], 4),round(a[2], 4)])
        
        for i in range(3):
            self.assertEqual(a[i],b[i])

    def test_translation_matrix_to_vector(self):
        
        gameComponent2 = VectorQuaternion_BasicTransformDecorator("Transform2", "TRS2", 202)
        
        tr_v = [2, 3, 4]
        a = gameComponent2.translate(tr_v)
        a = np.array([round(a[0], 1),round(a[1], 1),round(a[2], 1)])
        b = np.array([2.0, 3.0, 4.0])
        
        for i in range(3):
            self.assertEqual(a[i],b[i])
    
    print("TestComponent:test_init() END")
        
# run the test
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=3, exit=False)

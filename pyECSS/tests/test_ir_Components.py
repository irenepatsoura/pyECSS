import unittest
import numpy as np
from typing import List

from pyECSS.Entity import Entity
from pyECSS.Component import Component, BasicTransform, Camera, ComponentDecorator, RenderMesh, CompNullIterator, BasicTransformDecorator

import pyECSS.utilities as util

class TestComponent(unittest.TestCase):
    
    def test_init(self):
        """
        Entity init() test
        """
        print("TestComponent:test_init() START")
        
        gameComponent = BasicTransform("Transform", "TRS", 201)
        gameComponent2 = BasicTransformDecorator("Transform2", "TRS2", 202)
        
        self.assertEqual(gameComponent.rotationEulerAngles, gameComponent2.rotate())
        
        print("TestComponent:test_init() END")
        
# run the test
unittest.main()

import unittest

from pyECSS.skinning.System_skinning import System_skinning
from pyECSS.skinning.skinned_mesh import Skinned_mesh
from pyECSS.skinning.gate_module import *
import os.path

class TestComponent(unittest.TestCase):
    
    
    def setUp(self):
        
        self.skinnedMeshComponent = Skinned_mesh(filename='/Users/mlbeb/Desktop/boo/internship/py_code/pyECSSTree/pyECSS/examples/astroBoy_walk.dae', file_type='dae')

       
    def test_file_exists(self):
        assert(os.path.exists('/Users/mlbeb/Desktop/boo/internship/py_code/pyECSSTree/pyECSS/examples/')==True)
        
    print("TestComponent:test_animation() START")    
     
    def test_animation(self):
        a = self.skinnedMeshComponent
        self.assertNotEqual(a, None)
    
    print("TestComponent:test_animation() END")

        
    def test_vertices(self):
        a = self.skinnedMeshComponent
        for i in range(len(a.v)):
            assert(len(a.v[i])==3)

         
        
# run the test
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=3, exit=False)

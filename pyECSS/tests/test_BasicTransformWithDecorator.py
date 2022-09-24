import imp
import unittest
import numpy as np
import math
import pyECSS.utilities as util

from clifford.g3 import *  # import GA for 3D space
from pyECSS.Entity import Entity
from pyECSS.quaternion import Quaternion
from pyECSS.dual_quaternion import DualQuaternion
from pyECSS.Component import  BasicTransform,  VectorQuaternion_BasicTransformDecorator


class TestComponent(unittest.TestCase):
    
    
    def setUp(self):
        
        self.gameComponent = BasicTransform("Transform", "TRS", 201)
        self.gameComponent2 = VectorQuaternion_BasicTransformDecorator("Transform2", "TRS2", 202)
        self.obj = VectorQuaternion_BasicTransformDecorator()
        
        q = Quaternion(0,1,0,1)
        self.new_quat = VectorQuaternion_BasicTransformDecorator("Transform", "TRS", 203, None, q=q )
        self.new_quat_vec = VectorQuaternion_BasicTransformDecorator("Transform", "TRS", 207, None, q=q , vec=np.array([1,2,3]))

        
        q_rot = Quaternion(0, 0, 0, 1)
        q_dual = Quaternion(0, 0, 0, 0)
        dq = DualQuaternion(q_rot, q_dual)
        self.new_dq = VectorQuaternion_BasicTransformDecorator("Transform", "TRS", 204, None, None,dq)
        
        vector = np.array([1,1,-1])
        vector2 = np.array([1,2,3])
        # self.new_vector = VectorQuaternion_BasicTransformDecorator("Transform", "TRS", 205, None, None, None, vector)
        self.new_vector = VectorQuaternion_BasicTransformDecorator("Transform", "TRS", 205, None, None, None, vector2)
        
        rotor = np.array([1,2,3,4])
        self.new_rotor = VectorQuaternion_BasicTransformDecorator("Transform", "TRS", 206, None, None, None, None, rotor)
        
    def test_d_vec_2_trs(self):
        a = np.array([[-1,  0,  2, 1],
                      [ 0,  1,  0, 2],
                      [-2,  0, -1, 3],
                      [ 0 , 0,  0, 1]])
       
        b = self.new_quat_vec.trs
        
        self.assertAlmostEqual(a.all(),b.all(),1)
        

    def test_q_2_trs(self):
        
        a = np.array([[-1,  0,  2, 0],
                      [ 0,  1,  0, 0],
                      [-2,  0, -1, 0],
                      [ 0 , 0,  0, 1]])
       
        b = self.new_quat.trs()
        print("b is",b)
        
        self.assertAlmostEqual(a.all(),b.all(),1)
            
    def test_dq_2_trs(self):
        a = np.array([[1, 0, 0, 0], 
                      [0, 1, 0, 0], 
                      [0, 0, 1, 0], 
                      [0, 0, 0, 1]])
        b = self.new_dq.trs()
        self.assertAlmostEqual(a.all(),b.all(),1)
        
    def test_vec_2_trs(self):
        a = np.array([[ 1,  0,  0,  1],
                      [ 0,  1,  0,  2],
                      [ 0,  0,  1,  3],
                      [ 0,  0,  0,  1]])
        b = self.new_vector.trs
        self.assertAlmostEqual(a.all(),b.all(),1)
        
    def test_rotor_2_trs(self):
        a = np.array([[-25, -20,  22,   0],
                      [-28, -39,  -4,   0],
                      [ 10, -20, -49,   0],
                      [  0,   0,   0,   1]])
        
        b = self.new_rotor.trs()
        self.assertAlmostEqual(a.all(),b.all(),1)

        
        
        
          
    # def test_rotation_matrix_to_quaternion(self):
    #     """
    #     Entity rotation_matrix_to_quaternion() test
    #     """
    #     print("TestComponent:test_rotation_matrix_to_quaternion() START")
        
        
        # rot_v = np.array([1,1,1])
        # a = self.gameComponent2.rotate_vector(rot_v)
        # b = np.array([1.0000,    1.0000,    1.0000])
        # a = np.array([round(a[0], 4),round(a[1], 4),round(a[2], 4)])
        
        # for i in range(3):
        #     self.assertEqual(a[i],b[i])

    # def test_translation_matrix_to_vector(self):
        
        
    #     tr_v = [2, 3, 4]
    #     a = self.gameComponent2.translate_vector(tr_v)
    #     a = np.array([round(a[0], 1),round(a[1], 1),round(a[2], 1)])
    #     b = np.array([2.0, 3.0, 4.0])
        
    #     for i in range(3):
    #         self.assertEqual(a[i],b[i])
            
    # def test_translation_dual_quaternion(self):
    
    #     b = [ 7.0,  6.0, 16.0,]   
    #     a = self.obj.translate_dual_quaternion(5,3,2,2,3,14)
    #     a = np.array([round(a[0], 1),round(a[1], 1),round(a[2], 1)])
        
    #     for i in range(3):
    #         self.assertEqual(a[i],b[i])
            
    # def test_rotation_multivector(self):

    #     b = -(0.000000000005^e1) + (5.0^e2) + (0.000000000005^e3)
    #     a = 5*e1 # our object: the point (5,0,0)
    
    #     a = self.obj.rotate_multivector(a,2*math.pi/3) # the rotated object, ie, the point (0,5,0)
    #     self.assertAlmostEqual(a,b,3)

    
    
    print("TestComponent:test_init() END")
        
# run the test
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=3, exit=False)

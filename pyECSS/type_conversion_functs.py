from pyECSS.quaternion import Quaternion
import numpy as np

class Conversions():
    # function returning a 4x4 transformation matrix (trs) from a vector
    @classmethod
    def ir_vec_2_trs(self, vec):
        T = np.identity(n=4)
        T[0:3,3] = -vec
        return T

    #function returning trs from rotor
    @classmethod
    def ir_rotor_2_quat(self, rot):
        # assert( rot.odd.clean() == 0) # round odd part --> it should be 0, i.e., no odd vectors in bv
            
        q = Quaternion(x=rot[0],y=rot[3], z=rot[2], w=rot[1])
        return q       



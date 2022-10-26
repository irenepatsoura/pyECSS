
from re import M
from gate_module import *
import time
from System_skinning import System_skinning




class Skinned_mesh :
    def __init__(self,filename=None, file_type=None):
        
        if (filename is None):
            self._filename = self.getClassName()
        else:
            self._filename = filename
        
        if (file_type is None):
            self._file_type = self.getClassName()
        else:
            self._file_type = file_type
        
        # print(filename, file_type)
        self.model = load(self._filename,self._file_type)
        self.mesh_id = 3
        self.mesh = self.model.meshes[self.mesh_id]
        self.v = self.mesh.vertices
        print(self.mesh.faces)
        # print(self.v)
        self.f = self.mesh.faces
        self.b = self.mesh.bones
        color_list = []
        for i in range(len(self.v)):
            p = np.array([1.0, 0.0, 0.0])
            # print(p)
            color_list.append(p)
        color_array = np.array(color_list)
        self.mesh.colors = color_array
        self.model.meshes[self.mesh_id] = self.mesh
        self.colors = color_array
        
        
        
        
        # print(np.array(np.array([5,100,200])))
        # self.mesh.colors = len(self.mesh.vertices)*4
        
        # print("List:", my_list )
        # print("CS:",str(len(self.mesh.colors)))
        
        
# if __name__ == "__main__":
   
#     a = Skinned_mesh(filename='/Users/mlbeb/Desktop/boo/internship/py_code/pyECSSTree/pyECSS/examples/astroBoy_walk.dae',file_type='dae')
#     b = System_skinning(a.b, a.v, a.f)
    
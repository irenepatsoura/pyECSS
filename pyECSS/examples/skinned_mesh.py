
from re import M
from pyECSS.examples.gate_module import *
import time
from pyECSS.examples.System_skinning import System_skinning




class Skinned_mesh :
    def __init__(self,filename=None, file_type=None, animation=False):
        
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
        if(self.model==None): 
          return None  
        self.mesh_id = 3
        self.mesh = self.model.meshes[self.mesh_id]   
        print(self.mesh.faces)
        # print(self.v)
        self.f = self.mesh.faces
        if(len(self.f)==0):
            return None
        self.b = self.mesh.bones
        if(len(self.b)==0):
            return None 
        color_list = []
        for i in range(len(self.mesh.vertices)):
            p = np.array([1.0, 0.0, 0.0])
            # print(p)
            color_list.append(p)
        color_array = np.array(color_list)
        self.mesh.colors = color_array
        self.model.meshes[self.mesh_id] = self.mesh
        self.colors = color_array
        
        if not (animation):
            self.v = self.mesh.vertices
        else:
            temp = System_skinning()
            newv = temp.generate_mesh(self.mesh.vertices, self.b, self.model, self.mesh_id)
            self.v = newv
            
        if(len(self.v)==0):
            return None   
        

    
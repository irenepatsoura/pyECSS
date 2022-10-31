import time

from re import M
from pyECSS.skinning.gate_module import *
from pyECSS.skinning.System_skinning import System_skinning




class Skinned_mesh :
    """
    A concrete Sinned_mesh class

    Accepts a dedicated animation file to initiate the visualization of the model, using its vertex attributes
    """
    
    def __init__(self,filename=None, file_type=None, animation=False):
        """ Initialize the generic Skinned_mesh component with the name of the animation file and its type (e.g. .dae), 
        these will be passed to pyassimp load function in order to load the desired model
        then we initialize its vertex attributes, the bones and colors so we can generate the model. 

        """
        
        if (filename is None):
            self._filename = self.getClassName()
        else:
            self._filename = filename
        
        if (file_type is None):
            self._file_type = self.getClassName()
        else:
            self._file_type = file_type
        
        self.model = load(self._filename,self._file_type)
        
        if(self.model==None): 
          return None  
      
        self.mesh_id = 3
        self.mesh = self.model.meshes[self.mesh_id]   
        self.f = self.mesh.faces
        
        if(len(self.f)==0):
            return None
        
        self.b = self.mesh.bones
        
        if(len(self.b)==0):
            return None 
        
        color_list = []
        for i in range(len(self.mesh.vertices)):
            p = np.array([1.0, 0.0, 0.0])
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
        

    
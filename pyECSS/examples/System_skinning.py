from operator import mod
from gate_module import *
import time

class System_skinning:
    def __init__(self):
        pass
    
    def read_tree(model,mesh_id,M):
        b = model.meshes[mesh_id].bones
        MM = np.zeros([len(b),4,4])
        G = np.linalg.inv(model.rootnode.transformation)
        bone_names = get_bone_names(b)
        read_tree_names(MM,M,model.rootnode,G,bone_names)
        return MM

    def read_tree_names(MM,M,node,parentmatrix,bone_names):
        p = np.dot(parentmatrix,node.transformation)           
        if node.name in bone_names:
            index = bone_names.index(node.name)
            MM[index] = p
        for child in node.children:
            read_tree_names(MM,M,child,p,bone_names,False) 
     
    def print_animation(self, newv, v, f, b,model,meshid):
        print("col:",model.meshes[meshid].colors.shape)
        mp.plot(newv, f,c = model.meshes[meshid].colors,shading={"scale": 2.5,"wireframe":True},return_plot=True)
        
    # def print_animation(self,v, f, b, model, mesh_id) :         
        
    #     # print(v) 
    #     M = initialize_M(b)
    #     M[1] = np.dot(np.diag([2,2,2,1]),M[1])
        
    #     vw = vertex_weight(len(v))
    #     vw.populate(b)
        
    #     MM = read_tree(model,mesh_id,M,False)
    #     BB = [b[i].offsetmatrix for i in range(len(b))]
    #     newv = np.zeros([(len(v)),3])
    #     start = time.time()
    #     for i in range(len(v)):
    #         for j in range(4):
    #             if vw.id[i][j] >=0:
                 
    #                 mat = np.dot(MM[vw.id[i][j]],BB[vw.id[i][j]]) 
    #                 # mat =    BB[vw.id[i][j]]        
    #                 newv[i] = newv[i] + vw.weight[i][j]*(vertex_apply_M(v[i],mat))
    #     end = time.time()
    #     print("TIME : ", end-start)
    #     print("TRANSFORMATION = ", False)
    #     p = mp.plot(newv, f,newv[:, 1],shading={"scale": 2.5,"wireframe":True},return_plot=True)        
    #     # p.save(“skinning.html”)
        
    def generate_mesh(self,v, f, b, model, mesh_id):
        print("pipi")
        M = initialize_M(b)
        M[1] = np.dot(np.diag([2,2,2,1]),M[1])
        
        vw = vertex_weight(len(v))
        vw.populate(b)
        
        MM = read_tree(model,mesh_id,M,False)
        BB = [b[i].offsetmatrix for i in range(len(b))]
        newv = np.zeros([(len(v)),3])
        start = time.time()
        for i in range(len(v)):
            for j in range(4):
                if vw.id[i][j] >=0:
                 
                    mat = np.dot(MM[vw.id[i][j]],BB[vw.id[i][j]]) 
                    # mat =    BB[vw.id[i][j]]        
                    newv[i] = newv[i] + vw.weight[i][j]*(vertex_apply_M(v[i],mat))
        end = time.time()
        print("TIME : ", end-start)
        print("TRANSFORMATION = ", False)
        
        return self.print_animation(newv, v, f, b,model,mesh_id)
        
        # generate mesh (all above coode exept plot, returns a mesh to use by the ecss code in order ot print the animation)
        # color like Example_renderCube but for all vertices (.length())

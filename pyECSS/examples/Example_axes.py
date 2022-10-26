from statistics import mode
from turtle import width
import unittest

import numpy as np

import pyECSS.utilities as util
from pyECSS.Entity import Entity
from pyECSS.Component import VectorQuaternion_BasicTransformDecorator, Camera, RenderMesh
from pyECSS.System import System, TransformSystem, CameraSystem, RenderSystem
from pyGLV.GL.Scene import Scene
from pyECSS.ECSSManager import ECSSManager
from pyGLV.GUI.Viewer import SDL2Window, ImGUIDecorator, RenderGLStateSystem
from pyECSS.examples.quaternion import Quaternion

from pyGLV.GL.Shader import InitGLShaderSystem, Shader, ShaderGLDecorator, RenderGLShaderSystem
from pyGLV.GL.VertexArray import VertexArray

from OpenGL.GL import GL_LINES

import OpenGL.GL as gl



s1 = Scene()
scene = Scene()    

rootEntity = scene.world.createEntity(Entity(name="RooT"))
entityCam1 = scene.world.createEntity(Entity(name="entityCam1"))
scene.world.addEntityChild(rootEntity, entityCam1)

quat = Quaternion(0,0,0,1)
trans1 = scene.world.addComponent(entityCam1, VectorQuaternion_BasicTransformDecorator(name="trans1", q=quat))

entityCam2 = scene.world.createEntity(Entity(name="entityCam2"))
scene.world.addEntityChild(entityCam1, entityCam2)
trans2 = scene.world.addComponent(entityCam2, VectorQuaternion_BasicTransformDecorator(name="trans2", q=quat))
orthoCam = scene.world.addComponent(entityCam2, Camera(util.ortho(-100.0, 100.0, -100.0, 100.0, 1.0, 100.0), "orthoCam","Camera","500"))

node4 = scene.world.createEntity(Entity(name="node4"))
scene.world.addEntityChild(rootEntity, node4)
trans4 = scene.world.addComponent(node4, VectorQuaternion_BasicTransformDecorator(name="trans4", q=quat))
mesh4 = scene.world.addComponent(node4, RenderMesh(name="mesh4"))


axes = scene.world.createEntity(Entity(name="axes"))
scene.world.addEntityChild(rootEntity, axes)
axes_trans = scene.world.addComponent(axes, VectorQuaternion_BasicTransformDecorator(name="axes_trans", q=quat))
axes_mesh = scene.world.addComponent(axes, RenderMesh(name="axes_mesh"))

# a simple triangle
vertexData = np.array([
    [0.0, 0.0, 0.0, 1.0],
    [0.5, 1.0, 0.0, 1.0],
    [1.0, 0.0, 0.0, 1.0]
],dtype=np.float32) 
colorVertexData = np.array([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 1.0]
], dtype=np.float32)

#Colored Axes
vertexAxes = np.array([
    [0.0, 0.0, 0.0, 1.0],
    [1.0, 0.0, 0.0, 1.0],
    [0.0, 0.0, 0.0, 1.0],
    [0.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 1.0]
],dtype=np.float32) 
colorAxes = np.array([
    [1.0, 0.0, 0.0, 1.0],
    [1.0, 0.0, 0.0, 1.0],
    [0.0, 1.0, 0.0, 1.0],
    [0.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 1.0],
    [0.0, 0.0, 1.0, 1.0]
], dtype=np.float32)

#Simple Cube
vertexCube = np.array([
    [-0.5, -0.5, 0.5, 1.0],
    [-0.5, 0.5, 0.5, 1.0],
    [0.5, 0.5, 0.5, 1.0],
    [0.5, -0.5, 0.5, 1.0], 
    [-0.5, -0.5, -0.5, 1.0], 
    [-0.5, 0.5, -0.5, 1.0], 
    [0.5, 0.5, -0.5, 1.0], 
    [0.5, -0.5, -0.5, 1.0]
],dtype=np.float32) 
colorCube = np.array([
    [0.0, 0.0, 0.0, 1.0],
    [1.0, 0.0, 0.0, 1.0],
    [1.0, 1.0, 0.0, 1.0],
    [0.0, 1.0, 0.0, 1.0],
    [0.0, 0.0, 1.0, 1.0],
    [1.0, 0.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0],
    [0.0, 1.0, 1.0, 1.0]
], dtype=np.float32)

#index arrays for above vertex Arrays
index = np.array((0,1,2), np.uint32) #simple triangle
indexAxes = np.array((0,1,2,3,4,5), np.uint32) #3 simple colored Axes as R,G,B lines
indexCube = np.array((1,0,3, 1,3,2, 
                    2,3,7, 2,7,6,
                    3,0,4, 3,4,7,
                    6,5,1, 6,1,2,
                    4,5,6, 4,6,7,
                    5,4,0, 5,0,1), np.uint32) #rhombus out of two triangles



# Systems
transUpdate = scene.world.createSystem(TransformSystem("transUpdate", "TransformSystem", "001"))
camUpdate = scene.world.createSystem(CameraSystem("camUpdate", "CameraUpdate", "200"))
renderUpdate = scene.world.createSystem(RenderGLShaderSystem())
initUpdate = scene.world.createSystem(InitGLShaderSystem())

####################################################################################################
####################################################################################################
####################################################################################################

model = util.translate(0.0,0.0,0.0)
eye = util.vec(0.5, 0.5, 0.5)
target = util.vec(0,0,0)
up = util.vec(0.0, 1.0, 0.0)
view = util.lookat(eye, target, up)


projMat = util.ortho(-5.0, 5.0, -5.0, 5.0, 0.1, 100.0)

mvpMat = projMat @ view @ model 



shaderDec_axes = scene.world.addComponent(axes, ShaderGLDecorator(Shader(vertex_source = Shader.COLOR_VERT_MVP, fragment_source=Shader.COLOR_FRAG)))
shaderDec_axes.setUniformVariable(key='modelViewProj', value=mvpMat, mat4=True)

axes_mesh.vertex_attributes.append(vertexAxes) 
axes_mesh.vertex_attributes.append(colorAxes)
axes_mesh.vertex_index.append(indexAxes)
axes_vArray = scene.world.addComponent(axes, VertexArray(primitive=GL_LINES)) # note the primitive change




## ADD AXES TO THIS MESH - END ##


running = True
# MAIN RENDERING LOOP
scene.init(imgui=True, windowWidth = 1024, windowHeight = 768, windowTitle = "pyglGA test_axes")

# pre-pass scenegraph to initialise all GL context dependent geometry, shader classes
# needs an active GL context
scene.world.traverse_visit(initUpdate, scene.world.root)

while running:
    running = scene.render(running)
    scene.world.traverse_visit(renderUpdate, scene.world.root)
    scene.render_post()
    
scene.shutdown()


####################################################################################################  
####################################################################################################
####################################################################################################   

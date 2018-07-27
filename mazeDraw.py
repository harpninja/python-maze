import random
import maya.cmds as cmds

i = 1	# row
j = 1	# column
c = 1 	# cube number
filePath = cmds.fileDialog()

def create_shader():
	'''
	Add a white Arnold shader to the scene.
	'''
	name_shader = 'aiStandardSurfaceWhite'
	red = 1.0
	green = 1.0
	blue = 1.0
	cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=name_shader+'SG')
	cmds.shadingNode('aiStandardSurface', asShader=True, name=name_shader)
	cmds.setAttr(name_shader+'.baseColor', red, green, blue, type='double3')
	cmds.setAttr(name_shader+'.base', 0.85)         # diffuse weight
	cmds.setAttr(name_shader+'.specular', 0.05)     # specular weight
	cmds.connectAttr(name_shader+'.outColor', name_shader+'SG.surfaceShader')

def add_cube(nameCube, x, z):
	'''
	Add a cube to the scene and assign a shader to it.
	'''
	cmds.polyCube(name=nameCube, width=1, height=4, depth=1)
	cmds.move(x, 2, z)
	cmds.sets(nameCube, edit=True, forceElement='aiStandardSurfaceWhite'+'SG')

create_shader()
with open(filePath, 'r') as rfile:
	for row in rfile:
		i = i + 1
		columns = row.split(',')
		for column in columns:
			j = j + 1
			if ('True' in column):
				name = 'cube'+str(c)
				c = c + 1
				add_cube(name, i, j)
		j = 1

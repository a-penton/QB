from rubik.cube import Cube

"""
Holds helper functions for performing more trivial operations on the cube
All of these functions are imported to ./cubesolver.py,
 where they are used to perform more complex operations.

Functions include:
 - determine if a piece is solved
 - determine if a piece is permuted (placed correctly)
 - get the edges/corners around a center piece
 - find the next unsolved piece for a certain step (cross, layer, etc.)
"""

def is_piece_solved(cube, piece):
	# determine if a piece is solved
	# works for corners or edges

	# get colors of piece & corresponding centers
	colors = filter(None, piece.colors)
	centers = list(map(cube.find_piece, colors))

	# check permutation (placement)
	tuples = zip(*[c.pos for c in centers])
	correct_pos = list(map(sum, tuples))
	if correct_pos != piece.pos:
		return False

	# check orientation (twist)
	tuples = zip(*[c.colors for c in centers])
	correct_colors = list(map(bigor, tuples))
	if correct_colors != piece.colors:
		return False

	return True

def is_piece_permuted(cube, piece):
	# Just the permutation part of the is_piece_solved function

	# get colors of piece & corresponding centers
	colors = filter(None, piece.colors)
	centers = list(map(cube.find_piece, colors))

	# check permutation (placement)
	tuples = zip(*[c.pos for c in centers])
	correct_pos = list(map(sum, tuples))
	if correct_pos != piece.pos:
		return False

	return True

def bigor(tup):
	# returns the 'OR' of all elements in a tuple
	res = None
	for el in tup:
		res = res or el
	return res

def get_face_edges(cube, face):
	# returns array of edges around a face

	x = face.pos[0]
	y = face.pos[1]
	z = face.pos[2]

	arr = []

	if x != 0:
		arr.append(cube.get_piece(x,1,0))
		arr.append(cube.get_piece(x,-1,0))
		arr.append(cube.get_piece(x,0,1))
		arr.append(cube.get_piece(x,0,-1))
	elif y != 0:
		arr.append(cube.get_piece(0,y,1))
		arr.append(cube.get_piece(1,y,0))
		arr.append(cube.get_piece(-1,y,0))
		arr.append(cube.get_piece(0,y,-1))
	else:
		arr.append(cube.get_piece(1,0,z))
		arr.append(cube.get_piece(-1,0,z))
		arr.append(cube.get_piece(0,1,z))
		arr.append(cube.get_piece(0,-1,z))

	return arr

def get_corner_pieces(cube, face):
	x = face.pos[0]
	y = face.pos[1]
	z = face.pos[2]

	corners = []

	if x != 0:
		for i in range(-1,2,2):
			for j in range(-1,2,2):
				corners.append(cube.get_piece(x,i,j))
	elif y != 0:
		for i in range(-1,2,2):
			for j in range(-1,2,2):
				corners.append(cube.get_piece(i,y,j))
	else:
		for i in range(-1,2,2):
			for j in range(-1,2,2):
				corners.append(cube.get_piece(i,j,z))

	return corners

def get_middle_layer_pieces(cube):
	white_center = cube.find_piece("W")
	x = white_center.pos[0]
	y = white_center.pos[1]
	z = white_center.pos[2]

	middle = []

	if x != 0:
		middle.append(cube.getpiece(0, 1, 1))
		middle.append(cube.getpiece(0, 1, -1))
		middle.append(cube.getpiece(0, -1, 1))
		middle.append(cube.getpiece(0, -1, -1))
	elif y != 0:
		middle.append(cube.getpiece(1, 0, 1))
		middle.append(cube.getpiece(1, 0, -1))
		middle.append(cube.getpiece(-1, 0, 1))
		middle.append(cube.getpiece(-1, 0, -1))
	elif z != 0:
		middle.append(cube.getpiece(1, 1, 0))
		middle.append(cube.getpiece(1, -1, 0))
		middle.append(cube.getpiece(-1, 1, 0))
		middle.append(cube.getpiece(-1, -1, 0))

	return middle

def find_next_cross_edge(cube):
	# finds next unsolved cross edge, assuming white/yellow on U/D

	# first check the yellow side
	yellow_face = cube.find_piece('Y')
	possible_edges = get_face_edges(cube, yellow_face)
	for edge in possible_edges:
		if 'W' in edge.colors:
			return edge

	# next check the middle layer: this assums white/yellow on U/D
	for i in range(-1,2,2):
		for j in range(-1,2,2):
			edge = cube.get_piece(i,0,j)
			if 'W' in edge.colors:
				return edge

	# finally check white side
	white_face = cube.find_piece('W')
	possible_edges = get_face_edges(cube, white_face)
	for edge in possible_edges:
		if not is_piece_solved(cube, edge):
			return edge

def find_next_white_corner(cube):
	# find the next white corner to be solved
	# assuming white on bottom

	# first check the top layer for white corners
	for i in range(-1,2,2):
		for j in range(-1,2,2):
			piece = cube.get_piece(i,1,j)
			if 'W' in piece.colors:
				return piece

	# then check the bottom layer for unsolved corners
	# (all of the corners in the bottom layer are guaranteed to have white)
	for i in range(-1,2,2):
		for j in range(-1,2,2):
			piece = cube.get_piece(i,-1,j)
			if not is_piece_solved(cube, piece):
				return piece

def find_next_middle_layer_edge(cube):
	# find the next unsolved edge of the middle layer
	# assuming white layer is solved on the D face

	# first check the yellow side
	yellow_face = cube.find_piece('Y')
	possible_edges = get_face_edges(cube, yellow_face)
	for edge in possible_edges:
		if not 'Y' in edge.colors:
			return edge

	# then check the middle layer
	for i in range(-1,2,2):
		for j in range(-1,2,2):
			edge = cube.get_piece(i,0,j)
			if not is_piece_solved(cube, edge):
				return edge

from rubik.cube import Cube

"""
Function which reads in a cube and returns a tuple containing:
 - a string containing the next hint for solving the cube
 - a string containing the name of the current step (image of the current step)

TODO:
 - create an image for when two cross piece are swapped (line 38)

"""

def hint(cube, piece):
	# returns tuple of string, name of image, and next piece to solve
	# calls other functions to do so

	if cross_solved(cube):
		# if solved, the piece returned is the white center
		return ("The cross is solved!", "cross-solved.png", cube.find_piece('W'))
	else:
		return get_cross_hint(cube, piece)

def get_cross_hint(cube, piece):
	# checks if a new hint is needed or not, then calls a function
	# that function will return the specific hint for the piece

	# check that white is on bottom
	white_face = cube.find_piece('W')
	if white_face.pos != (0,-1,0):
		return ("Rotate the cube so the white face is on bottom", "rotate.png", white_face)

	# determine if the current edge is solved
	if piece == None or piece == white_face or is_piece_solved(cube, piece):
		next_piece = find_next_cross_edge(cube)
		return get_specific_cross_hint(cube, next_piece)
	elif is_edge_permuted(cube, piece):
		# if the edge is flipped in place

		return get_specific_cross_hint(cube, piece)
	else:
		# piece is still unsolved, don't need to update
		return (None, None, None)

def get_specific_cross_hint(cube, piece):
	# returns tuple of hint text and image
	# assuming white on bottom

	# get some information about the piece
	piece_colors = list(filter(None, piece.colors))
	non_white = piece_colors[0] if piece_colors[1] == 'W' else piece_colors[1]

	# depending on the case, provide the hint to solve that piece
	if piece.pos[1] == 1:
		# piece in U-layer
		s = "1. Put the %s %s edge above\n the %s center\n2. Turn the %s center twice" % (*piece_colors, non_white, non_white)
		s = fix_color_string(s)
		img = "top.png"
	elif piece.pos[1] == 0:
		# piece in E-slice (middle layer)
		s = "1. Move the %s %s edge to the top layer.\n2. Turn the top\n3. Undo the move from step 1" % (*piece_colors,)
		s += "\n\n4. Put the %s %s edge above\n the %s center\n5. Turn the %s center twice" % (*piece_colors, non_white, non_white)
		s = fix_color_string(s)
		img = "middleV2.png"
	elif is_edge_permuted(cube, piece):
		# flipped in place
		s = "We need to flip the %s %s edge" % (*piece_colors,)
		s = fix_color_string(s)
		s += "\n1. Rotate the cube so it is at\n the bottom right"
		s += "\n2. Perform R Di F D"
		img = "flip.png"
	else:
		# in the cross but misplaced
		s = "1. Bring the %s %s edge to the top\n by turning one side twice" % (*piece_colors,)
		s += "\n\n2. Put the %s %s edge above\n the %s center\n3. Turn the %s center twice" % (*piece_colors, non_white, non_white)
		s = fix_color_string(s)
		img = "bottom.png"

	return (s, img, piece)

def fix_color_string(s):
	# replace individual letters with their colors
	s = s.replace(' W ', ' White ')
	s = s.replace(' R ', ' Red ')
	s = s.replace(' O ', ' Orange ')
	s = s.replace(' B ', ' Blue ')
	s = s.replace(' G ', ' Green ')
	s = s.replace(' Y ', ' Yellow ')

	return s

def is_edge_permuted(cube, piece):
	# Just the permutation part of the is_piece_solved function

	# determine faces
	piece_colors = list(filter(None, piece.colors))
	face_one = cube.find_piece(piece_colors[0])
	face_two = cube.find_piece(piece_colors[1])

	# check position
	pos_tuples = zip(face_one.pos, face_two.pos)
	correct_pos = [t[0] + t[1] for t in pos_tuples]
	for i in range(0, 3):
		if correct_pos[i] != piece.pos[i]:
			return False

	return True

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
			if 'W' in cube.get_piece(i,0,j).colors:
				return cube.get_piece(i,0,j)

	# finally check white side
	white_face = cube.find_piece('W')
	possible_edges = get_face_edges(cube, white_face)
	for edge in possible_edges:
		if not is_piece_solved(cube, edge):
			return edge

def cross_solved(cube):
	# determine if the cross is solved

	white_center = cube.find_piece('W')

	cross_pieces = get_face_edges(cube, white_center)

	for edge in cross_pieces:
		if not is_edge_solved(cube, edge):
			return False

	return True

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
		arr.append(cube.get_piece(1,y,0))
		arr.append(cube.get_piece(-1,y,0))
		arr.append(cube.get_piece(0,y,1))
		arr.append(cube.get_piece(0,y,-1))
	else:
		arr.append(cube.get_piece(1,0,z))
		arr.append(cube.get_piece(-1,0,z))
		arr.append(cube.get_piece(0,1,z))
		arr.append(cube.get_piece(0,-1,z))

	return arr

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


def white_solved(cube):
	# If the cross isn't solved, neither will the white side
	if not cross_solved(cube):
		return False
	white_center = cube.find_piece("W")

	# Get corner pieces in the white face
	corner_pieces = get_corner_pieces(cube, white_center)
	for corner in corner_pieces:
		if not is_piece_solved(cube, corner):
			return False
	return True

def bigor(tup):
	# returns the 'OR' of all elements in a tuple
	res = None
	for el in tup:
		res = res or el
	return res

def get_corner_pieces(cube, face):
	x = face.pos[0]
	y = face.pos[1]
	z = face.pos[2]

	corners = []

	if x != 0:
		for i in range(-1,1,2):
			for j in range(-1,1,2):
				corners.append(cube.get_piece(x,i,j))
	elif y != 0:
		for i in range(-1,1,2):
			for j in range(-1,1,2):
				corners.append(cube.get_piece(i,y,j))
	else:
		for i in range(-1,1,2):
			for j in range(-1,1,2):
				corners.append(cube.get_piece(i,j,z))

	return corners
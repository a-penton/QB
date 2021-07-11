from rubik.cube import Cube

"""
Function which reads in a cube and returns a tuple containing:
 - a string containing the next hint for solving the cube
 - a string containing the name of the current step (image of the current step)

TODO:
 - create an image for when two cross piece are swapped (line 38)

"""

def hint(cube, piece, stage):
	# returns tuple of string, name of image, and next piece to solve
	# calls other functions to do so

	if stage == -1:
		if not is_cross_solved(cube):
			stage = 0
		elif not is_white_solved(cube):
			stage = 1

	if stage == 1 and not is_cross_solved(cube):
		stage = 0

	if stage == 0 and is_cross_solved(cube):
		stage = 1
	if stage == 1 and is_white_solved(cube):
		stage = -1

	if stage == 0:
		return get_cross_hint(cube, piece)
	elif stage == 1:
		return get_white_layer_hint(cube, piece)
	else:
		# if solved, the piece returned is the white center
		return ("The white face is solved!", "cross-solved.png", cube.find_piece('W'), -1)

def get_white_layer_hint(cube, piece):
	# checks if a new hint is needed or not, then returns the appropriate hint

	# check that white is on bottom
	white_face = cube.find_piece('W')
	if white_face.pos != (0,-1,0):
		return ("Rotate the cube so the white face is on bottom", "rotate.png", white_face, 1)

	# determine if current piece is solved or a new piece is needed
	if piece == None or piece == white_face or is_piece_solved(cube, piece):
		next_piece = find_next_white_corner(cube)
		return get_specific_white_layer_hint(cube, next_piece)
	elif is_cross_solved(cube):
		# update hint for the current piece
		return get_specific_white_layer_hint(cube, piece)
	else:
		# piece is still unsolved, don't need to update
		return (None, None, None, 1)

def get_specific_white_layer_hint(cube, piece):
	# returns tuple of hint text, image, and piece
	# assuming white on bottom

	# first get information on where it belongs
	centers = list(map(cube.find_piece, piece.colors))
	tuples = zip(*[c.pos for c in centers])
	correct_pos = list(map(sum, tuples))

	if piece.pos[0] != correct_pos[0] or piece.pos[2] != correct_pos[2]:
		if piece.pos[1] == 1:
			# piece is above the wrong slot (just turn the top)
			hint = "Move the %s %s %s corner\n" % (*sorted(piece.colors),)
			hint += " above the %s and %s centers" % (*filter(lambda x: x != 'W', sorted(piece.colors)),)
			hint = fix_color_string(hint)
		# otherwise, the piece is inside the wrong slot: need to take it out
		elif piece.pos[2] == -1:
			# at the back of the cube
			hint = "Rotate the cube so that the\n"
			hint += " %s %s %s corner is at the front" % (*sorted(piece.colors),)
			hint = fix_color_string(hint)
		elif piece.pos[0] == 1:
			# in the front-right slot
			hint = "Use the right-hand sequence\n"
			hint += " to take out the %s %s %s corner\n" % (*sorted(piece.colors),)
			hint = fix_color_string(hint)
			hint += "The sequence is R U Ri Ui"
		elif piece.pos[0] == -1:
			# in the front-left slot
			hint = "Use the left-hand sequence\n"
			hint += " to take out the %s %s %s corner\n" % (*sorted(piece.colors),)
			hint = fix_color_string(hint)
			hint += "The sequence is Li Ui L U"

	elif piece.pos[2] != 1:
		# piece/slot is at the back of the cube
		hint = "Rotate the cube so that the\n"
		hint += " %s %s %s corner is at the front" % (*sorted(piece.colors),)
		hint = fix_color_string(hint)
	else:
		# piece is at front, at the correct slot, but unsolved
		if piece.pos[0] == 1:
			hint = "Repeat the right-hand sequence\n"
			hint += " to solve the %s %s %s corner\n" % (*sorted(piece.colors),)
			hint = fix_color_string(hint)
			hint += "The sequence is R U Ri Ui"
		elif piece.pos[0] == -1:
			hint = "Repeat the left-hand sequence\n"
			hint += " to solve the %s %s %s corner\n" % (*sorted(piece.colors),)
			hint = fix_color_string(hint)
			hint += "The sequence is Li Ui L U"

	return hint, None, piece, 1


def find_next_white_corner(cube):
	# find the next white corner to be solved
	# assuming white on bottom

	# first check the top layer for white
	for i in range(-1,2,2):
		for j in range(-1,2,2):
			piece = cube.get_piece(i,1,j)
			if 'W' in piece.colors:
				return piece

	# then check the bottom layer for unsolved white corners
	for i in range(-1,2,2):
		for j in range(-1,2,2):
			piece = cube.get_piece(i,-1,j)
			if 'W' in piece.colors and not is_piece_solved(cube, piece):
				return piece

def get_cross_hint(cube, piece):
	# checks if a new hint is needed or not, then calls a function
	# that function will return the specific hint for the piece

	# check that white is on bottom
	white_face = cube.find_piece('W')
	if white_face.pos != (0,-1,0):
		return ("Rotate the cube so the white face is on bottom", "rotate.png", white_face, 0)

	# determine if the current edge is solved
	if piece == None or piece == white_face or is_piece_solved(cube, piece):
		next_piece = find_next_cross_edge(cube)
		return get_specific_cross_hint(cube, next_piece)
	elif is_piece_permuted(cube, piece):
		# if the edge is flipped in place

		return get_specific_cross_hint(cube, piece)
	else:
		# piece is still unsolved, don't need to update
		return (None, None, None, 0)

def get_specific_cross_hint(cube, piece):
	# returns tuple of hint text, image, and piece
	# assuming white on bottom

	# get some information about the piece
	piece_colors = list(filter(None, piece.colors))
	non_white = piece_colors[0] if piece_colors[1] == 'W' else piece_colors[1]

	# depending on the case, provide the hint to solve that piece
	if piece.pos[1] == 1:
		# piece in U-layer
		s = "1. Put the %s %s edge above\n the %s center\n2. Turn the %s center twice" % (*sorted(piece_colors), non_white, non_white)
		s = fix_color_string(s)
		img = "top.png"
	elif piece.pos[1] == 0:
		# piece in E-slice (middle layer)
		s = "1. Move the %s %s edge to the top layer.\n2. Turn the top\n3. Undo the move from step 1" % (*sorted(piece_colors),)
		s += "\n\n4. Put the %s %s edge above\n the %s center\n5. Turn the %s center twice" % (*sorted(piece_colors), non_white, non_white)
		s = fix_color_string(s)
		img = "middleV2.png"
	elif is_piece_permuted(cube, piece):
		# flipped in place
		s = "We need to flip the %s %s edge" % (*sorted(piece_colors),)
		s = fix_color_string(s)
		s += "\n1. Rotate the cube so it is at\n the bottom right"
		s += "\n2. Perform R Di F D"
		img = "flip.png"
	else:
		# in the cross but misplaced
		s = "1. Bring the %s %s edge to the top\n by turning one side twice" % (*piece_colors,)
		s += "\n\n2. Put the %s %s edge above\n the %s center\n3. Turn the %s center twice" % (*sorted(piece_colors), non_white, non_white)
		s = fix_color_string(s)
		img = "bottom.png"

	return (s, img, piece, 0)

def fix_color_string(s):
	# replace individual letters with their colors
	s = s.replace(' W ', ' white ')
	s = s.replace(' R ', ' red ')
	s = s.replace(' O ', ' orange ')
	s = s.replace(' B ', ' blue ')
	s = s.replace(' G ', ' green ')
	s = s.replace(' Y ', ' yellow ')

	return s

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

def is_cross_solved(cube):
	# determine if the cross is solved

	white_center = cube.find_piece('W')

	cross_pieces = get_face_edges(cube, white_center)

	for edge in cross_pieces:
		if not is_piece_solved(cube, edge):
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


def is_white_solved(cube):
	# If the cross isn't solved, neither will the white side
	if not is_cross_solved(cube):
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
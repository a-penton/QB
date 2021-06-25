from rubik.cube import Cube

"""
Function which reads in a cube and returns a tuple containing:
 - a string containing the next hint for solving the cube
 - a string containing the name of the current step (image of the current step)

TODO:
 - create an image for when two cross piece are swapped (line 38)

"""

def hint(cube):
	# return tuple of string and name of step/image

	if cross_solved(cube):
		return ("The cross is solved!", '')
	else:
		# find the next cross edge
		next_piece, case = find_next_cross_edge(cube)
		e_colors = list(filter(None, next_piece.colors))
		non_white = e_colors[0] if e_colors[1] == 'W' else e_colors[1]

		if case == 1:
			s = "put the %s %s edge above the %s center, then turn the %s center twice" % (*e_colors, non_white, non_white)
			img = "top.png"
		elif case == 2:
			s = "move the %s %s edge to the top, turn the top, then undo the first move" % (*e_colors,)
			img = "middle.png"
		elif case == 3:
			if is_edge_permuted(cube, next_piece):
				s = "Flip the %s %s edge" % (*e_colors,)
				s += "\n1. Rotate the cube so it is at the bottom right"
				s += "\n2. Perform R Di F D"
				img = "flip.png"
			else:
				s = "Bring the %s %s edge to the top by turning one side twice" % (*e_colors,)
				img = None

		return (s, img)


def is_edge_permuted(cube, piece):
	# Just the permutation part of the is_edge_solved function

	# determine faces
	piece_colors = [c for c in piece.colors if c != None]
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
	# returns a tuple, second value depends on case
	# (e, 1) means e is in yellow layer
	# (e, 2) means e is in middle layer
	# (e, 3) means e is in white layer

	# first check the yellow side
	yellow_face = cube.find_piece('Y')
	possible_edges = get_face_edges(cube, yellow_face)
	for edge in possible_edges:
		if 'W' in edge.colors:
			return (edge, 1)

	# next check the middle layer: this assums white/yellow on U/D
	for i in range(-1,2,2):
		for j in range(-1,2,2):
			if 'W' in cube.get_piece(i,0,j).colors:
				return (cube.get_piece(i,0,j), 2)

	# finally check white side
	white_face = cube.find_piece('W')
	possible_edges = get_face_edges(cube, white_face)
	for edge in possible_edges:
		if not is_edge_solved(cube, edge):
			return (edge, 3)

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

def is_edge_solved(cube, piece):
	# for edge pieces only
	# there's probably a way to extend this to corners too

	# determine faces
	piece_colors = [c for c in piece.colors if c != None]
	face_one = cube.find_piece(piece_colors[0])
	face_two = cube.find_piece(piece_colors[1])

	# check position
	pos_tuples = zip(face_one.pos, face_two.pos)
	correct_pos = [t[0] + t[1] for t in pos_tuples]
	for i in range(0, 3):
		if correct_pos[i] != piece.pos[i]:
			return False

	# check orientation (colors)
	color_tuples = zip(face_one.colors, face_two.colors)
	correct_colors = [t[0] or t[1] for t in color_tuples]
	for i in range(0, 3):
		if correct_colors[i] != piece.colors[i]:
			return False

	return True


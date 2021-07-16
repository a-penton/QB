from rubik.cube import Cube
from cubebasics import *

"""
Function which reads in a cube and returns a tuple containing:
 - a string containing the next hint for solving the cube
 - a string containing the name of the current step (image of the current step)

TODO:
 - create images for steps after the cross

"""

"""
Guide for the 'stage' variable:
0. Solve cross
1. Solve white layer (corners)
2. Solve middle layer
3. EO (orient/twist yellow edges)
4. EP (place yellow edges)
5. CP (place yellow corners)
6. CO (orient/twist yellow corners)

-1 means the cube is solved
"""

def hint(cube, piece, stage):
	# returns tuple of string, name of image, and next piece to solve
	# calls other functions to do so

	# if the cube is scrambled, switch to the appropriate step
	if stage == -1:
		if not is_cross_solved(cube):
			stage = 0
		elif not is_white_solved(cube):
			stage = 1
		elif not is_middle_layer_solved(cube):
			stage = 2
		elif not is_eo_solved(cube):
			stage = 3

	# if the current stage is solved, proceed to the next one
	if stage == 0 and is_cross_solved(cube):
		stage = 1
	if stage == 1 and is_white_solved(cube):
		stage = 2
	if stage == 2 and is_middle_layer_solved(cube):
		stage = 3
	if stage == 3 and is_eo_solved(cube):
		stage = -1

	if stage == 0:
		return get_cross_hint(cube, piece)
	elif stage == 1:
		return get_white_layer_hint(cube, piece)
	elif stage == 2:
		return get_middle_layer_hint(cube, piece)
	elif stage == 3:
		return get_eo_hint(cube)
	else:
		# if solved, the piece returned is the white center
		return ("The first two layers are solved!", "cross-solved.png", cube.find_piece('W'), -1)

def fix_color_string(s):
	# replace individual letters with their colors
	s = s.replace(' W ', ' white ')
	s = s.replace(' R ', ' red ')
	s = s.replace(' O ', ' orange ')
	s = s.replace(' B ', ' blue ')
	s = s.replace(' G ', ' green ')
	s = s.replace(' Y ', ' yellow ')

	return s

def get_cross_hint(cube, piece):
	# checks if a new hint is needed or not, then calls a function
	# that function will return the specific hint for the piece

	# check that white is on bottom
	white_face = cube.find_piece('W')
	if white_face.pos != (0,-1,0):
		return ("Rotate the cube so the white face is on bottom", "rotate-white-bottom.png", white_face, 0)

	# determine if the current edge is solved
	if piece == None or piece == white_face or is_piece_solved(cube, piece):
		next_piece = find_next_cross_edge(cube)
		return get_specific_cross_hint(cube, next_piece)
	elif is_piece_permuted(cube, piece):
		# if the edge is flipped in place

		return get_specific_cross_hint(cube, piece)
	else:
		# piece is still unsolved, don't need to update
		return None, None, piece, 0

def get_specific_cross_hint(cube, piece):
	# returns tuple of hint text, image, piece, and stage number (0)
	# assuming white on bottom

	# get some information about the piece
	piece_colors = sorted(list(filter(None, piece.colors)))
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
	elif is_piece_permuted(cube, piece):
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

	return s, img, piece, 0

def get_white_layer_hint(cube, piece):
	# checks if a new hint is needed or not, then returns the appropriate hint

	# check that white is on bottom
	white_face = cube.find_piece('W')
	if white_face.pos != (0,-1,0):
		return ("Rotate the cube so the white face is on bottom", "rotate-white-bottom.png", white_face, 1)

	# determine if current piece is solved or a new piece is needed
	if piece == None or piece == white_face or is_piece_solved(cube, piece):
		next_piece = find_next_white_corner(cube)
		return get_specific_white_layer_hint(cube, next_piece)
	elif is_cross_solved(cube):
		# update hint for the current piece
		return get_specific_white_layer_hint(cube, piece)
	else:
		# piece is still unsolved, don't need to update
		return None, None, piece, 1

def get_specific_white_layer_hint(cube, piece):
	# returns tuple of hint text, image, piece, and stage number (1)
	# assuming white on bottom

	# first get information on where it belongs
	centers = list(map(cube.find_piece, piece.colors))
	tuples = zip(*[c.pos for c in centers])
	correct_pos = list(map(sum, tuples))

	piece_colors = sorted(piece.colors)

	if piece.pos[0] != correct_pos[0] or piece.pos[2] != correct_pos[2]:
		# piece is not in/above the correct slot
		if piece.pos[1] == 1:
			# piece is above the wrong slot (just turn the top)
			hint = "Move the %s %s %s corner\n" % (*piece_colors,)
			hint += " above the %s and %s centers" % (*filter(lambda x: x != 'W', piece_colors),)
			hint = fix_color_string(hint)
			img = "white-corner-u-ui.png"
		# otherwise, the piece is inside the wrong slot: need to take it out
		elif piece.pos[2] == -1:
			# at the back of the cube
			hint = "Rotate the cube so that the\n"
			hint += " %s %s %s corner is at the front" % (*piece_colors,)
			hint = fix_color_string(hint)
			img = "rotate-y.png"
		elif piece.pos[0] == 1:
			# in the front-right slot
			hint = "Use the right-hand sequence\n"
			hint += " to take out the %s %s %s corner\n" % (*piece_colors,)
			hint = fix_color_string(hint)
			hint += "The sequence is R U Ri Ui"
			# different images if in top/bottom layer
			img = "white-corner-right-wrong.png"
		elif piece.pos[0] == -1:
			# in the front-left slot
			hint = "Use the left-hand sequence\n"
			hint += " to take out the %s %s %s corner\n" % (*piece_colors,)
			hint = fix_color_string(hint)
			hint += "The sequence is Li Ui L U"
			# different images if in top/bottom layer
			img = "white-corner-left-wrong.png"

	elif piece.pos[2] != 1:
		# piece/slot is at the back of the cube
		hint = "Rotate the cube so that the\n"
		hint += " %s %s %s corner is at the front" % (*piece_colors,)
		hint = fix_color_string(hint)
		img = "rotate-y.png"
	else:
		# piece is at front, at the correct slot, but unsolved
		if piece.pos[0] == 1:
			hint = "Repeat the right-hand sequence\n"
			hint += " to solve the %s %s %s corner\n" % (*piece_colors,)
			hint = fix_color_string(hint)
			hint += "The sequence is R U Ri Ui"
			# different images if in top/bottom layer
			img = "white-corner-right-"
			img += "top" if piece.pos[1] == 1 else "bottom"
			img += ".png"
		elif piece.pos[0] == -1:
			hint = "Repeat the left-hand sequence\n"
			hint += " to solve the %s %s %s corner\n" % (*piece_colors,)
			hint = fix_color_string(hint)
			hint += "The sequence is Li Ui L U"
			# different images if in top/bottom layer
			img = "white-corner-left-"
			img += "top" if piece.pos[1] == 1 else "bottom"
			img += ".png"

	return hint, img, piece, 1

def get_middle_layer_hint(cube, piece):
	# determine the type of hint to return for the middle layer

	# check that white is on bottom
	white_face = cube.find_piece('W')
	if white_face.pos != (0,-1,0):
		return ("Rotate the cube so the white face is on bottom", "rotate-white-bottom.png", white_face, 2)

	if piece == None or piece == white_face or is_piece_solved(cube, piece):
		# piece needs to be updated
		next_piece = find_next_middle_layer_edge(cube)
		return get_specific_middle_layer_hint(cube, next_piece)
	elif is_white_solved(cube):
		# may need to update the hint
		return get_specific_middle_layer_hint(cube, piece)
	else:
		# piece is being solved,  don't update the hint
		return None, None, piece, 2

def get_specific_middle_layer_hint(cube, piece):
	# return the specific hint for solving a middle layer edge
	# returns tuple of hint text, image, piece, and stage number (2)

	# get piece information
	piece_colors = sorted(list(filter(None, piece.colors)))

	# first deal with pieces in the middle layer
	if piece.pos[1] == 0:
		if piece.pos[2] == -1:
			hint = "Rotate the cube so the %s %s piece\n" % (*piece_colors,)
			hint += " is at the front"
			hint = fix_color_string(hint)
			img = "rotate-y.png"
		else:
			hint = "We need to take out the %s %s piece\n" % (*piece_colors,)
			hint += "Do this by inserting a random piece in its place\n"
			hint = fix_color_string(hint)
			if piece.pos[0] == 1:
				# insert on the right side
				hint += "1. Perform the right-hand move (R U Ri Ui)\n"
				hint += "2. Rotate the cube to face the right (Y)\n"
				hint += "3. Perform the left-hand move (Li Ui L U)"
				img = "middle-layer-right-wrong.png"
			else:
				# insert on the left side
				hint += "1. Perform the left-hand move (Li Ui L U)\n"
				hint += "2. Rotate the cube to face the left (Yi)\n"
				hint += "3. Perform the right-hand move (R U Ri Ui)"
				img = "middle-layer-left-wrong.png"

	# all other cases concern pieces in the top layer
	else:
		# get the side-facing color of the edge (either on the X or Z axis)
		# this is whichever one is not None
		side_color = piece.colors[2] if piece.colors[0] == None else piece.colors[0]
		side_center = cube.find_piece(side_color)
		# top_center is the center that matches the piece's top color
		top_center = cube.find_piece(piece.colors[1])

		hint = "-- Solve the %s %s edge --\n" % (*piece_colors,)

		if side_center.pos != (0,0,1):
			hint += "Rotate the cube so the %s center is at the front" % side_color
			hint = fix_color_string(hint)
			img = "rotate-y.png"
		elif piece.pos[0] != -1*top_center.pos[0]:
			if top_center.pos[0] == 1:
				hint += "Turn the top so the %s %s edge is on the left" % (*piece_colors,)
				img = "middle-layer-u.png"
			else:
				hint += "Turn the top so the %s %s edge is on the right" % (*piece_colors,)
				img = "middle-layer-ui.png"
			hint = fix_color_string(hint)
		else:
			# the piece is in position to perform the algorithm
			if top_center.pos[0] == 1:
				hint += "Insert the %s %s edge to the right:\n" % (*piece_colors,)
				hint = fix_color_string(hint)
				hint += "1. Perform the right-hand move (R U Ri Ui)\n"
				hint += "2. Rotate the cube to face the right (Y)\n"
				hint += "3. Perform the left-hand move (Li Ui L U)"
				img = "middle-layer-right.png"
			else:
				hint += "Insert the %s %s edge to the left:\n" % (*piece_colors,)
				hint = fix_color_string(hint)
				hint += "1. Perform the left-hand move (Li Ui L U)\n"
				hint += "2. Rotate the cube to face the left (Yi)\n"
				hint += "3. Perform the right-hand move (R U Ri Ui)"
				img = "middle-layer-left.png"

	return hint, img, piece, 2

def get_eo_hint(cube):
	# This step is very straightforward, only three cases to handle
	# solving all yellow edges, so no particular piece to solve

	# check that white is on bottom
	white_face = cube.find_piece('W')
	if white_face.pos != (0,-1,0):
		return ("Rotate the cube so the white face is on bottom", "rotate-white-bottom.png", white_face, 3)

	# may need to update the hint
	if is_middle_layer_solved(cube):
		return get_specific_eo_hint(cube)
	else:
		return None, None, None, 3

def get_specific_eo_hint(cube):
	# assumes white on D (yellow on U)

	# count oriented edges
	num_oriented_edges = 0
	if cube.get_piece(0,1,1).colors[1] == 'Y':
		num_oriented_edges += 1
	if cube.get_piece(0,1,-1).colors[1] == 'Y':
		num_oriented_edges += 1
	if cube.get_piece(1,1,0).colors[1] == 'Y':
		num_oriented_edges += 1
	if cube.get_piece(-1,1,0).colors[1] == 'Y':
		num_oriented_edges += 1

	if num_oriented_edges == 0:
		hint = "No edges have yellow facing up\n"
		hint += "1. Turn the front face clockwise (F)\n"
		hint += "2. Perform the right-hand move (R U Ri Ui)\n"
		hint += "3. Undo the move from step 1 (Fi)"
	if num_oriented_edges == 2:
		# two possible cases: line or L-shape
		uf_edge_oriented = cube.get_piece(0,1,1).colors[1] == 'Y'
		ub_edge_oriented = cube.get_piece(0,1,-1).colors[1] == 'Y'
		# line cases:
		if uf_edge_oriented and ub_edge_oriented:
			hint = "Two edges have yellow facing up (line case)\n"
			hint += "Turn the top so they are on the left and right (U)"
		elif not (uf_edge_oriented or ub_edge_oriented):
			hint = "Two edges have yellow facing up (line case)\n"
			hint += "1. Turn the front face clockwise (F)\n"
			hint += "2. Perform the right-hand move (R U Ri Ui)\n"
			hint += "3. Undo the move from step 1 (Fi)"
		# L-shape cases:
		else:
			hint = "Two edges have yellow facing up (L case)\n"
			ul_edge_oriented = cube.get_piece(-1,1,0).colors[1] == 'Y'
			if ul_edge_oriented and ub_edge_oriented:
				hint += "1. Turn the front face clockwise (F)\n"
				hint += "2. Perform the right-hand move (R U Ri Ui)\n"
				hint += "3. Undo the move from step 1 (Fi)"
			else:
				hint += "Turn the top so that these two edges\n"
				hint += " are at the back and left of the top face"

	return hint, None, None, 3

def is_cross_solved(cube):
	# determine if the cross is solved

	white_center = cube.find_piece('W')

	cross_pieces = get_face_edges(cube, white_center)

	for edge in cross_pieces:
		if not is_piece_solved(cube, edge):
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

def is_middle_layer_solved(cube):
	# If the white isn't solved, this layer doesn't matter
	if not is_white_solved(cube):
		return False
	middle_edges = get_middle_layer_pieces(cube)
	for piece in middle_edges:
		if not is_piece_solved(cube, piece):
			return False
	return True

def is_eo_solved(cube):
	# Check everything before it
	if not is_middle_layer_solved(cube):
		return False

	yellow_center = cube.find_piece("Y")
	x,y,z = yellow_center.pos

	face_edges = get_face_edges(cube, yellow_center)
	if x != 0:
		for edge in face_edges:
			if edge.colors[0] != 'Y':
				return False
	elif y != 0:
		for edge in face_edges:
			if edge.colors[1] != 'Y':
				return False
	elif z != 0:
		for edge in face_edges:
			if edge.colors[2] != 'Y':
				return False
	return True

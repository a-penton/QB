from rubik.cube import Cube

"""
Helper methods:
 - Is white on bottom?
 - Is the cross solved?

 - Get edges around a center piece
 - Is this edge piece solved?

 - Find the next cross piece
 - Solve the next cross piece

"""

c = Cube("RRRRRRRRRBBBWWWGGGYYYBBBWWWGGGYYYBBBWWWGGGYYYOOOOOOOOO")

def perform(cube, move):
	if move == 'U':
		cube.U()
	elif move == 'Ui':
		cube.Ui()
	elif move == 'D':
		cube.D()
	elif move == 'Di':
		cube.Di()
	elif move == 'F':
		cube.F()
	elif move == 'Fi':
		cube.Fi()
	elif move == 'B':
		cube.B()
	elif move == 'Bi':
		cube.Bi()
	elif move == 'R':
		cube.R()
	elif move == 'Ri':
		cube.Ri()
	elif move == 'L':
		cube.L()
	elif move == 'Li':
		cube.Li()
	elif move == 'X':
		c.X()
	elif move == 'Xi':
		c.Xi()
	elif move == 'Z':
		c.Z()
	elif move == 'Zi':
		c.Zi()
	elif move == 'Y':
		c.Y()
	elif move == 'Yi':
		c.Yi()
	elif move == 'M':
		c.M()
	elif move == 'Mi':
		c.Mi()
	elif move == 'S':
		c.S()
	elif move == 'Si':
		c.Si()
	elif move == 'E':
		c.E()
	elif move == 'Ei':
		c.Ei()

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

def is_cross_done(cube):
	# checks if the white cross is finished

	white_face = cube.find_piece('W')

	cross_pieces = get_face_edges(cube, white_face)

	x = white_face.pos[0]
	y = white_face.pos[1]
	z = white_face.pos[2]

	if x != 0:
		for p in cross_pieces:
			if p.colors[0] != 'W':
				return False
	elif y != 0:
		for p in cross_pieces:
			if p.colors[1] != 'W':
				return False
	else:
		for p in cross_pieces:
			if p.colors[2] != 'W':
				return False

	return True

def find_next_cross_piece(cube):
	# find next piece to solve in the cross
	# assume white cross, white face on D

	# first check U layer
	top_face = cube.find_piece('Y')
	u_edges = get_face_edges(cube, top_face)
	for e in u_edges:
		if 'W' in e.colors:
			return e

	# next check middle layer
	for i in range(-1,2,2):
		for j in range(-1,2,2):
			if 'W' in cube.get_piece(i,0,j).colors:
				return cube.get_piece(i,0,j)

	# don't have to do bottom layer

def is_cross_edge_solved(cube, piece):
	# for edge pieces only
	# determine faces
	colors = [c for c in piece.colors if c != None]
	face_one = cube.find_piece(colors[0])
	face_two = cube.find_piece(colors[1])

	# check position
	tuples = zip(face_one.pos, face_two.pos)
	correct_pos = [t[0] + t[1] for t in tuples]
	for i in range(0, 3):
		if correct_pos[i] != piece.pos[i]:
			return False

	# check orientation (colors)
	if piece.colors[1] != 'W':
		return False

	return True


def solve_cross_piece(cube, piece):
	colors = [c for c in piece.colors if c != None]
	# if in the middle, move to the top
	while piece.pos[1] == 0:
		text = "Move the %s %s piece to the top" % (*colors,)
		text = text.replace(' W ', ' White ')
		text = text.replace(' R ', ' Red ')
		text = text.replace(' O ', ' Orange ')
		text = text.replace(' B ', ' Blue ')
		text = text.replace(' G ', ' Green ')
		text = text.replace(' Y ', ' Yellow ')
		print(text)
		while piece.pos[1] != 1:
			print(cube)
			move = input()
			perform(cube, move)

		print("Move the top layer once")
		print(cube)
		move = input()
		perform(cube, move)

		print("Restore the cross") # Need better phrasing TODO
		print(cube)
		move = input()
		perform(cube, move)
	# if in the top, move to the bottom
	text = "Move the %s %s piece above its center" % (*colors,)
	text = text.replace(' W ', ' White ')
	text = text.replace(' R ', ' Red ')
	text = text.replace(' O ', ' Orange ')
	text = text.replace(' B ', ' Blue ')
	text = text.replace(' G ', ' Green ')
	text = text.replace(' Y ', ' Yellow ')
	print(text)
	# https://stackoverflow.com/questions/40676085/why-cant-i-use-a-starred-expression
	print("Then turn that face twice to put it on the bottom")
	while piece.pos[1] != -1:
		print(cube)
		move = input()
		perform(cube, move)

	# if flipped on the bottom, correct it
	if piece.colors[1] != 'W':
		text = "We need to flip the %s %s piece" % (*colors,)
		text = text.replace(' W ', ' White ')
		text = text.replace(' R ', ' Red ')
		text = text.replace(' O ', ' Orange ')
		text = text.replace(' B ', ' Blue ')
		text = text.replace(' G ', ' Green ')
		text = text.replace(' Y ', ' Yellow ')
		print(text)
		print("Rotate the cube so the piece at the bottom right.")
		print("Then perform R Di F D")
		while not is_cross_edge_solved(cube, piece):
			print(cube)
			move = input()
			perform(cube, move)

# Takes a white edge and returns the other color
def get_white_edge_color(piece):
	for i in range(3):
		if piece.colors[i] != None and piece.colors[i] != "W":
			return piece.colors[i]
	return ""

def main():	
	white_face = c.find_piece('W')
	
	print("-- Step 0: White on Bottom --")
	
	while white_face.pos != (0,-1,0):
		print(c)
		print("put the white face on the bottom")
		move = input()
		perform(c, move)
		
	print(c)
	print("yay, the white face is on bottom!")
	
	print("-- Step 1: Cross --")
	
	while not is_cross_done(c):
		print(c)
		p = find_next_cross_piece(c)
		solve_cross_piece(c, p)
		# The above function reads input & executes the move
	
	print(c)
	print("yay, the cross is done!")

if __name__ == '__main__':
	main()
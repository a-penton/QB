

class Cubie:

    # A Cubie is a single block or piece in the rubik's cube. 


    def __init__(self, pos, colors):
        
        # The Cubie constructor takes in a tuple of three integer values ranging from -1 to 1
        self.pos = pos


        # It also takes in a tuple of colors. The colors are arranged in order of x, y, z of the direction they are facing
        self.colors = colors


        # By counting the number of null values in the colors list we can identify if the piece is a CORNER, EDGE, or FACE
        # Corners have three colors, Edges have two colors, and Faces have one color. 
        if colors.count(None) == 0:
            self.type = "CORNER"
        elif colors.count(None) == 1:
            self.type = "EDGE"
        elif colors.count(None) == 2:
            self.type = "FACE"
        else:
            print("Colors list is empty")


    def rotate(self, matrix):
        

        # Save the old position
        old_pos = self.pos

        # Use matrix multiplication to find the new position
        self.pos = matrix * self.pos

        # By comparing between the old and new positions we can see which values changed, which tells us which axis to rotate on
        axis = self.pos - old_pos

        # We iterate through the axis matrix to find non zero values, these are the values of the indices of the two colors we need to swap
        i, j = (i for i, x in enumerate(axis) if x != 0)

        # Then we just swap the two colors
        temp = self.colors[i]
        self.colors[i] = self.colors[j]
        self. colors[j] = temp
        


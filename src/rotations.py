cube = [[2,3,4],[1,2,3],[5,7,1]]#[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5],[6,6,6,6,6,6,6,6,6]]
FACE_ADJACENCY = { 0: [4,3,5,2],  # Front | Top Right Bottom Left
1: {'top': 4, 'bottom': 5, 'left': 3, 'right': 2},  # Back 
2: {'top': 4, 'bottom': 5, 'left': 1, 'right': 0},  # Left 
3: {'top': 4, 'bottom': 5, 'left': 0, 'right': 1},  # Right 
4: {'top': 1, 'bottom': 0, 'left': 2, 'right': 3},  # Top 
5: {'top': 0, 'bottom': 1, 'left': 2, 'right': 3},  # Bottom 
}
rotation_pairs = {}
def rotation(prev_face,curr_face):
    diff = set() 
    for i in range(9):
        print(i)
        if prev_face[i] != curr_face[i]:
            diff.add(i)
    return diff
"""def face_find(prev_face):
    index = 0 #the current position we are on our face
    counter = 0 #keeps track on number of correct faces
    prev_face_index = 0 #The current position of our previous face
    prev_index = 0 #the past index of our index
    for face in range(len(cube)):
        while counter < 3:          
            if prev_face[prev_face_index] == cube[face][index] and prev_face_index == 0:
                #found face but have no memory
                prev_face_index += 1
                index += 1
                prev_index = index
                break
            elif prev_face[prev_face_index] == cube[face][index]:
                #found face and have memory
                prev_face_index += 1
                index += 1
                break
            elif prev_face_index == 0:
                index += 1
            else:
                prev_face_index = 0
                index = prev_index
                counter = 0
        return face"""
def face_find(prev_face):
    center = prev_face[4]
    for face in range(len(cube)):
        if cube[face][4] == center:
            return face
    return -1
def get_orientation(prev_face,face):
    top_of_face = prev_face[0:3]
    face = cube[face]
    if top_of_face == face[0:3]:
        return 0
    elif top_of_face == [face[2],face[3],face[8]]:
        return 1
    elif top_of_face == [face[0],face[5],face[6]]:
        return 2
    else:
        return 3
def orientation_shifter(shifts,positions):
    for s in range(shifts):
        current = positions[0]
        previous = positions[-1]
        for i in range(len(positions)):
            current = positions[i]
            positions[i] = previous 
            previous = current
    return positions

print(orientation_shifter(2,[1,2,3,4]))

            
            
                       
        #move everything to the right 1 and then move the value of the end to the begining, shifts is the number of times we do the shifts, and positions is the list that we're shifting

    

#print(rotation([23,4325,324,2,5,7,3,263,5],[124,21,324,124,5,7,124,213,5]))
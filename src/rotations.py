cube = [[2,3,4],[1,2,3],[5,7,1]]#[0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3],[4,4,4,4,4,4,4,4,4],[5,5,5,5,5,5,5,5,5],[6,6,6,6,6,6,6,6,6]]
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

test = [124,5421,56,423,23,1]
print(test[2,3,5])
#print(rotation([23,4325,324,2,5,7,3,263,5],[124,21,324,124,5,7,124,213,5]))
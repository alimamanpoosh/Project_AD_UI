Width = 4
Length =  4




class car:
    #if Placement_status == 0 ==>Horizontal __
    #if Placement_status == 1 ==>Vertical |
    Placement_status = Status_detection(1,2)
    x=Placement_status % Width
    y = Placement_status / Width



def Status_detection( back_j, front_j):
    if abs(front_j - back_j) == 1:
        return 1
    elif abs(front_j - back_j) == 0:
        return 0

def cheak_Move():
    #if  near node is -1 we can Move car
    #else can't move the car
    # return True or False

def Move(x, y, direction)
    # if vertical Move == > change x ( front ++, back --)
    # if horizontal Move == > change y  ( front ++, back --)
    # Direction up  or Down || left right
    #cheak Move the car
    #if  direction  ==> left --> j-2  || right --> j+2 || up --> i-2 || down --> i+2
    #so call Move agin (repeat 24 ,25,26 and 27 line) recursive function
    #end of recursive function is cheack _move is flase so return and end function
    #else call agin function and





#  0 ==> Empty palce  -1 ==> Camera Place

Parking = [[3,7,7,6],
           [3,5,5,6],
           [4,4,0,-1],
           [1,1,2,2]
        ]
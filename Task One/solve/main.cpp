#include <iostream>
#include<bits/stdc++.h>

#define Width 4
#define Length 4

using namespace std;

//Horizontal or Vertical Car Status
int Status_detection(int back_j,int front_j)
{
    if(abs(front_j - back_j) == 1)
    {
        return 1;
    }
    else if (abs(front_j - back_j) == 0) {
        return 0;
    }
}
void Move(int x , int y,string direction)
{
    //if vertical Move ==> change x ( front ++, back --)
    //if horizontal Move ==> change y  ( front ++, back --)
    //Direction  up  or Down || left right
    //cheak Move the car
    //if  direction  ==> left --> j-2  || right --> j+2 || up --> i-2 || down --> i+2
    //so call Move agin (repeat 24 ,25,26 and 27 line) recursive function

    //end of recursive function is cheack _move is flase so return and end function
    //else call agin function and

}
class car{
public:
    //if Placement_status == 0 ==>Horizontal __
    //if Placement_status == 1 ==>Vertical |
    int Placement_status= Status_detection(1,2);
    int x=Placement_status % Width,y=Placement_status / Width;


};
bool check_Move()
{
        //if  near node is -0 we can Move car .
        //else can't move the car
}

int main()
{

    // 0 ==> Empty palce  -1 ==> Camera Place
    int Parking[Width][Length] = {
                                   {3,7,7,6},
                                   {3,5,5,6},
                                   {4,4,0,-1},
                                   {1,1,2,2}};
    return 0;
}

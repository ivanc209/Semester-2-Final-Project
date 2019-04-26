"""
Ivan C
CS 2
4/24/19
ASSIGNMENT Sem 2 Final Project

This program will create a tile game using an inputted image
"""
import os
import random

def main():
    draw_image()

"""
Description:This method will take an image, create a 2D list of its contents, and make a grid
ontop of the image
Parameters:
    NONE
Return:
    NONE
Plan:The bmp image will first be opened, and each pixel will be added into a 2D list
containing each row and column. Then the image will be opened, and using the 2D list, the
method will create a 4x4 grid on top of the image by turning pixels black at equal distances
"""
def draw_image():
    #os.system("powershell -c H:\CS2\Unit5\class.bmp")
    bin_list=[]

    bin_file=open("class.bmp","rb") 
    header_offset=get_integer(bin_file,10)
    width=get_integer(bin_file,18)
    height=get_integer(bin_file,22)
    #image_data=width*3*height
    # print width,height,image_data
    bin_file.seek(header_offset)
        
    #append the image data into a 2D list
    for i in range(height):
        row=[]
        for i in range(width):
            pixel=bin_file.read(3)
            row.append(pixel)
        bin_list.append(row)
            
    #create copy of orignial file to have grid lines made
    with open("grid_picc.bmp","wb") as copy_binfile:
        copy_header(bin_file,copy_binfile)

        COLUMN=width/4
        ROW=height/4

        #create four columns 
        for i in range(1,4):    
            column_coord=COLUMN*i
            #print column_coord
            
            for j in range(height-1):
                #print j,column_coord
                bin_list[j][column_coord]=bytearray("000")

        #create four rows 
        for i in range(1,4):    
            row_coord=ROW*i
            for j in range(width-1):
                #print j,column_coord
                bin_list[row_coord][j]=bytearray("000")
        #call method to swap 2 desired tiles        
        scramble(bin_list,ROW,COLUMN)
        
        #copy new 2D list onto output file        
        for row in bin_list:
            for num in row:
                copy_binfile.write(num)
        
        
    os.system("powershell -c H:\CS2\FP\Semester-2-Final-Project\grid_picc.bmp")

"""
Description: This method will take two tiles on the image and swap the two tiles.
Parameters:
    tile1:the coordinate of the first desired tile
    tile2: the coordinate of the second desired tile
    grid_pic: the 2D list containing the image data
    ROW: the height of 1 box within the grid
    COLUMN: the width of 1 box within the grid
Return:
    NONE
Plan: The method will go through each individual row within the two boxes passed as parameters
swapping that row for the row of the second box. 
"""
def tile_swap(tile1,tile2,grid_pic,ROW,COLUMN):
    row_coord1=((tile1-1)/4)*ROW
    if tile1>4:
        column_coord1=(tile1-2)/4*COLUMN
    else:
        column_coord1=(tile1-1)*COLUMN
    row_coord2=((tile2-1)/4)*ROW
    if tile2>4:
        column_coord2=(tile2-2)/4*COLUMN
    else:
        column_coord2=(tile2-1)*COLUMN
    print row_coord1,column_coord1,row_coord2,column_coord2
    for i in range(0,ROW):
        for j in range(0,COLUMN):
            #print i +row_coord1,j+row_coord1
            byte_row1=grid_pic[i+row_coord1][j+column_coord1]
            byte_row2=grid_pic[i+row_coord2][j+column_coord2]
            
            grid_pic[i+row_coord1][j+column_coord1]=byte_row2
            grid_pic[i+row_coord2][j+column_coord2]=byte_row1

def scramble(bin_list,ROW,COLUMN):
    for i in range(10):
        random1=random.randint(1,16)
        random2=random.randint(1,16)
        tile_swap(random1,random2,bin_list,ROW,COLUMN)
""" 
Description:
This method will calculate the binary integer represented at the offset inputted
to the method

Parameters:
    bin_file: the bmp file which was given by the user
    offset:  this is an integer which is used to determine where the filemarker
    will be placed
Return:
    integer: this is an integer which is the binary number calculated at a given
    offset

Plan:
Move the filemarker to the given location or offset, then read 4 characters from
their and convert each of those bytes into binary numbers, and finding the sum
of all of those bytes
"""
def get_integer(bin_file,offset):
    integer=0
    bin_file.seek(offset)
    bytes = bin_file.read(4)
    for i in range(4):
        ch=bytes[i]
        decimal=ord(ch)
        integer+=decimal*(256**i)
    return integer        
"""
Description:
This method will take two files and copy the header of the first file onto
the second file

Parameters:
    bin_file:the bmp file which was given by the user opened for reading   
    output_file: duplicate bmp file opened for writing
Return:
    output_file:duplicate bmp file opened for writing(now has the header of
    bin_file)
Plan:
Use previous method to calculate the marker location of the header from the
input or original file, then read the characters in the header of the original
file and copy them onto the output file, and return it
"""
def copy_header(bin_file,output_file):
    header_end=get_integer(bin_file,10)
    bin_file.seek(0)
    header=bin_file.read(header_end)
    output_file.write(header)


"""
Description: This method will copy the bmp file given by the user,
into a duplicate file

Parameters: bin_file: the bmp file which was given by the user

Return: NONE

Plan: A duplicate file will be opened called "Copy.bmp", it will be opened to write on. Then each character from
the original file will be copied into the duplicate file. 
""" 
def copy_file (bin_file): 
    copy_bin=open("Copy.bmp","wb") 
    bin_file.seek(0) 
    for ch in bin_file: 
        copy_bin.write(ch) 
        bin_file.close() 
        copy_bin.close() 
    return copy_bin    
if __name__ == "__main__":
    main()

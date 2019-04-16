# Semester-2-Final-Project
Python picture tile game
"""
Ivan C
CS 2
4/2/19
ASSIGNMENT Sem 2 Final Project

This program will create a tile game using an inputted image
"""
import os
def main():
    draw_image()

"""
Description: This method will take in a file and create a copy with a 4x4 grid
drawn on the image

Parameters:
    NONE

Returns:
    NONE

Plan:
    The image data of the original file will be put into a 2D list, the new file
    will then be drawn the exact same, except the pixels will be turned black in
    four rows and four columns at equal distance, to create a 4x4 grid on the new
    image
"""
def draw_image():
    os.system("powershell -c H:\CS2\Unit5\class.bmp")
    bin_list=[]
    
    with open("class.bmp","rb") as bin_file:
        header_offset=get_integer(bin_file,10)
        width=get_integer(bin_file,18)
        height=get_integer(bin_file,22)
        image_data=width*3*height
        # print width,height,image_data
        bin_file.seek(header_offset)
        
        #append the image data into a 2D list
        for i in range(height*width):
            row=[]
            pixel=bin_file.read(3)
            row.append(pixel)
            bin_list.append(row)
            
        #create copy of orignial file to have grid lines made
        copy_binfile=open("grid_pic","wb")
        copy_header(bin_file,copy_binfile)
        
        #create four grids 
        for i in range(1,5):
            column=width/4
            column_coord=column*i
            print column_coord
            for j in range(1):
                #print j
                #byte=bin_list[column_coord][j]
                #num=ord(byte)
                new_num=0
                new_char=chr(new_num)
                bin_list[column_coord][j]=new_char
        os.system("powershell -c H:\CS2\Unit5\grid_pic.bmp")
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
    return output_file

"""
Description:
This method will copy the bmp file given by the user, into a
duplicate file

Parameters:
    bin_file: the bmp file which was given by the user
    
Return: NONE

Plan:
A duplicate file will be opened called "Copy.bmp", it will be opened to
write on. Then each character from the original file will be copied into the
duplicate file.
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


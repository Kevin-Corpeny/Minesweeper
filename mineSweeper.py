#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 00:00:03 2021

@author: kaimed
    @__str__(self) function provided by: https://github.com/kying18/minesweeper/blob/main/minesweeper.py

PROJECT: command line minesweeper
"""
import random
import sys

class Board:
    '''  "*" means a bomb    '''
    def __init__(self, dimensions, bombs):
        self.dimensions = dimensions
        self.bombs = bombs
        self.bomb_coords = set()
        self.dug = set()
        #board
        self.board = self.make_new_board()
        
    '''
    Makes a board and populates it with self.dimensions bombs. also sets self.bomb_coords
    '''
    def make_new_board(self):
        #this makes a 2D array of None types of dimensions self.dimensions x self.dimensions
        board = [[None for _ in range(0,self.dimensions)] for _ in range(0,self.dimensions)]
        
        #lets plant some bombs!!!
        planted_coords = set()
        coords = ()
        
        #experimental vars:
        loops_run = 0
        while len(planted_coords) < self.dimensions:
            
            loops_run += 1
            coords = (random.randint(0,self.dimensions-1),random.randint(0,self.dimensions-1))
            
            if coords in planted_coords:
                coords = (random.randint(0,self.dimensions-1),random.randint(0,self.dimensions-1))
            board[coords[0]][coords[1]] = "*"
            planted_coords.add(coords)
        print(planted_coords)
        self.bomb_coords = planted_coords
        return board
    
    '''
    returns the number of neigboring bombs at point (x,y)
    '''
    def get_neighboring_bomb_cnt(self, x, y):
        if (x,y) in self.bomb_coords:
            return -1
        cnt = 0
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]
        for item in neighbors:
            if item in self.bomb_coords:
                cnt += 1
        return cnt
    
    '''
    function to reveal tiles
    '''
    def dig(self,x,y):
        if (x,y) in self.bomb_coords:
            self.dug.add((x,y))
        else:
            self.dug.add((x,y))
            self.board[x][y] = self.get_neighboring_bomb_cnt(x,y)            
    
    
    '''
    input and game
    '''
    def play(self): 
        while 1:
            bad_input = True
            while bad_input:
                print(self)
                try:
                    x = int(input("Please select somewhere to dig... Good luck!!!\n\tX coordinate (horizontal) >>"))
                    y = int(input("\tY coordinate (vertical) >>"))
                    self.dig(y,x)
                    if (y,x) in self.bomb_coords:
                        print(self)
                        print("BOOOOOOOOOOM!!!!! \n Please Try Again.")
                
                        again = input("Try again? >>")
                        if again.lower() == 'y':
                            main()
                        else:
                            sys.exit("Thanks for playing :D")
                        bad_input = False
                except IndexError:
                    print("Invalid input, try again!")
                except ValueError:
                    print("Invalid input, try again!")

                
            
    '''
        STUPID. DELETE THIS SHIT
    '''
    def print_board(self):
        for x in self.board:
            for y in x:
                if y != '*':
                    print(y, end=' | ')
                else:
                    print('  * ',end=' | ')
            print()
            
            
    '''
        THIS IS WHAT THE PLAYER WILL SEE
    '''
    '''
    THIS IS NOT MY CODE
    ALL CREDIT FOR THIS FUNCTION GOES TO: https://github.com/kying18/minesweeper/blob/main/minesweeper.py
    '''
    def __str__(self):
        visible_board = [[None for _ in range(self.dimensions)] for _ in range(self.dimensions)]
        for row in range(self.dimensions):
            for col in range(self.dimensions):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dimensions):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dimensions)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dimensions)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
 
                
        
def main(dimensions = 10, bombs = 10,mode = 'easy'):    
    myBoard = Board(dimensions,bombs)

    myBoard.play()
#    myBoard.print_board_empty()
#    print(myBoard.bomb_coords)
#    print(myBoard.get_neighboring_bomb_cnt(0,0))
#    print(myBoard)
main()

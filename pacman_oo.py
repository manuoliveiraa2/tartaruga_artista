"""Pacman, classic arcade game.
Exercises
1. Move the score variable/attribute to Pacman's class. This attribute must be incremented by a new method in Pacman's code. 
    Chose draw_score according to the needed changes in GamePacman.
2. Create a speed attribute and do the needed changes to change Pacman's speed according to its value.
3. Create a subclass of Ghosts that each one of them has ghosts
    with different speeds value (Use the second exercise as an example).
4. Create a superclass for both Pacman and Ghost.
5. Create different types of food.
"""

from random import choice
from turtle import bgcolor, clear, up, down, goto, Turtle, dot, update, ontimer, setup, hideturtle, tracer, listen, onkey, done
from freegames import floor, vector

class Actor:
    def __init__(self,position_x, position_y,aim_x,aim_y):
        self.position = vector(position_x,position_y)
        self.aim = vector(aim_x, aim_y)
        self.speed = 1   

class Pacman:
    def __init__(self,position_x, position_y,aim_x,aim_y):
        self.position = vector(position_x,position_y)
        self.aim = vector(aim_x, aim_y)
        self.direction = "EAST"
        self.state = "ALIVE"
        self.score = 0
        self.speed = 2

    def move(self):
        self.position.move(self.aim * self.speed)

    def eat(self):
            self.score += 1

    def die(self):
        self.state = "DEAD"

    def alive(self):
        return self.state != "DEAD"

    def next_position(self, aim=None):
        if aim != None :
            new_position = self.position + aim
        else:
            new_position = self.position + self.aim
        return new_position

    turn_to_left = {'NORTH': ('WEST', vector(-5, 0)),
                'WEST' : ('SOUTH', vector(0, -5)),
                'SOUTH': ('EAST', vector(5, 0)),
                'EAST' : ('NORTH', vector(0, 5))}

    turn_to_right = {'NORTH': ('EAST', vector(5, 0)),
                'EAST' : ('SOUTH', vector(0, -5)),
                'SOUTH': ('WEST', vector(-5, 0)),
                'WEST' : ('NORTH', vector(0, 5))}

    turn_to_around = {'NORTH': ('SOUTH', vector(0, -5)),
                'SOUTH' : ('NORTH', vector(0, 5)),
                'WEST': ('EAST', vector(5, 0)),
                'EAST' : ('WEST', vector(-5, 0))}

    def left(self):
        self.direction, new_aim = self.turn_to_left[self.direction]
        self.aim = new_aim

    def right(self):
        self.direction, new_aim = self.turn_to_right[self.direction]
        self.aim = new_aim

    def turn_around(self):
        self.direction, new_aim = self.turn_to_around[self.direction]
        self.aim = new_aim


class Ghost:
    def __init__(self,position_x, position_y,aim_x,aim_y):
        self.position = vector(position_x,position_y)
        self.aim = vector(aim_x, aim_y)

    def move(self):
        self.position.move(self.aim )

    def change_direction(self):
        options = [
            vector(5, 0),
            vector(-5, 0),
            vector(0, 5),
            vector(0, -5),
        ]
        self.aim = choice(options)

class FastGhost(Ghost):
    def __init__(self, position_x, position_y,aim_x,aim_y):
        super().__init__self.position = vector(position_x,position_y)
        self.aim = vector(aim_x, aim_y)
        self.speed = 3

class GamePacman:
    def __init__(self):
        self.path = Turtle(visible=False)
        self.writer = Turtle(visible=False)
        self.pacman = Pacman(-40, -80, 5, 0)
        self.ghosts = [Ghost(-180,160,5,0),
                    Ghost(-180,-160,0,5),
                    Ghost(100,160,0,-5),
                    Ghost(100,-160,-5,0)]
        self.tiles = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        self.food = {}
        self.draw_world()

        onkey(lambda: self.on_rightkeypressed() , 'Right')
        onkey(lambda: self.on_leftkeypressed(), 'Left')
        onkey(lambda: self.on_upkeypressed(), 'Up')
        onkey(lambda: self.on_downkeypressed(), 'Down')

    def on_rightkeypressed(self):
        if self.valid(self.pacman.next_position(vector(5,0))):
            if self.pacman.direction == 'NORTH':
                self.pacman.right()
            elif self.pacman.direction == "SOUTH":
                self.pacman.left()
            elif self.pacman.direction == "WEST":
                self.pacman.turn_around()

    def on_leftkeypressed(self):
        if self.valid(self.pacman.next_position (vector(-5,0))):
            if self.pacman.direction == 'NORTH':
                self.pacman.left()
            elif self.pacman.direction == "SOUTH":
                self.pacman.right()
            elif self.pacman.direction == "EAST":
                self.pacman.turn_around()

    def on_upkeypressed(self):
        if self.valid(self.pacman.next_position(vector(0,5))):
            if self.pacman.direction == 'WEST':
                self.pacman.right()
            elif self.pacman.direction == "EAST":
                self.pacman.left()
            elif self.pacman.direction == "SOUTH":
                self.pacman.turn_around()

    def  on_downkeypressed (self):
        if self.valid(self.pacman.next_position(vector(0,-5))):
            if self.pacman.direction == 'WEST':
                self.pacman.left()
            elif self.pacman.direction == "EAST":
                self.pacman.right()
            elif self.pacman.direction == "NORTH":
                self.pacman.turn_around()

    def square(self,x,y):
        self.path.up()
        self.path.goto(x,y)
        self.path.down()
        self.path.begin_fill()

        for count in range(4):
            self.path.forward(20)
            self.path.left(90)
        
        self.path.end_fill()

    def offset(self,point):
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        index = int(x + y * 20)
        return index

    def valid(self,point):
        "Return True if point is valid in tiles."
        index = self.offset(point)

        if self.tiles[index] == 0:
            return False

        index = self.offset(point + 19)

        if self.tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0

    def draw_world(self):
        bgcolor('black')
        self.path.color('blue')

        for index in range(len(self.tiles)):
            tile = self.tiles[index]
            if tile> 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                self.square(x,y)

                if tile == 1:
                    self.path.up()
                    self.path.goto(x + 10, y + 10)
                    self.path.dot(2, 'white')

    def draw_score(self):
        self.writer.goto(140, 160)
        self.writer.color('white')
        self.writer.clear()
        self.writer.write('score: ')
        self.writer.goto(175, 160)
        self.writer.write(self.pacman.score)

    def clear_tile(self,index):
            self.tiles[index] = 2
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            self.square(x, y)

    def move_and_draw_pacman(self):
        if self.valid(self.pacman.next_position()):
            self.pacman.move()

        up()
        goto(self.pacman.position.x +10 , self.pacman.position.y + 10)
        dot(20,'yellow')

    def move_and_draw_ghost(self):
        for ghost in self.ghosts:
            if self.valid(ghost.position + ghost.aim):
                ghost.move()
            else:
                ghost.change_direction()

            up()
            goto(ghost.position.x + 10, ghost.position.y + 10)
            dot(20, 'red')

    def check_collision(self):
        for ghost in self.ghosts:
            if abs(self.pacman.position - ghost.position) < 20:
                self.pacman.die()

            index = self.offset(self.pacman.position )
            if self.tiles[index] == 1:
                self.pacman.eat()
                self.clear_tile(index)
    
    def run(self):
        self.writer.undo()
        self.draw_score()
        clear()
        self.check_collision()
        self.move_and_draw_pacman()
        self.move_and_draw_ghost()

        if self.pacman.alive():
            ontimer(self.run, 100)
        else:
            return

        update()

def init():
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    game = GamePacman()
    game.run()
    done()

if __name__ == '__main__':
    init()
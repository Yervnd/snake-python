import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg='black')
        self.canvas.pack()
        
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.food = self.generate_food()
        self.direction = 'Left'
        self.speed = 100
        
        self.bind_keys()
        self.draw_board()
        self.move_snake()
    
    def bind_keys(self):
        self.master.bind('<Left>', self.change_direction)
        self.master.bind('<Right>', self.change_direction)
        self.master.bind('<Up>', self.change_direction)
        self.master.bind('<Down>', self.change_direction)
        
    def draw_board(self):
        self.canvas.delete(tk.ALL)
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0]+10, segment[1]+10, fill='green')
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0]+10, self.food[1]+10, fill='red')
    
    def change_direction(self, event):
        new_direction = event.keysym
        if new_direction == 'Up' and self.direction != 'Down':
            self.direction = new_direction
        elif new_direction == 'Down' and self.direction != 'Up':
            self.direction = new_direction
        elif new_direction == 'Left' and self.direction != 'Right':
            self.direction = new_direction
        elif new_direction == 'Right' and self.direction != 'Left':
            self.direction = new_direction
    
    def generate_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return (x, y)
    
    def move_snake(self):
        head = self.snake[0]
        if self.direction == 'Up':
            new_head = (head[0], head[1]-10)
        elif self.direction == 'Down':
            new_head = (head[0], head[1]+10)
        elif self.direction == 'Left':
            new_head = (head[0]-10, head[1])
        elif self.direction == 'Right':
            new_head = (head[0]+10, head[1])
        
        self.snake = [new_head] + self.snake[:-1]
        
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.generate_food()
        
        self.draw_board()
        self.master.after(self.speed, self.move_snake)

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
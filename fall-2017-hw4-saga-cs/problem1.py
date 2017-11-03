from abc import ABC, ABCMeta, abstractmethod
import tkinter as tk
import math

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

class drawable(ABC):
	@abstractmethod
	def __contains__(self):
		pass
	def __and__(self, other):
		return Intersection(self, other)
	def __or__(self, other):
		return Union(self, other)
	def __sub__(self, other):
		return Difference(self, other)
	def draw(self, canvas):
		self.canvas = canvas
		h = int(self.canvas['height'])
		w = int(self.canvas['width'])
		for x in range(w):
			xp = x-(w/2)
			for y in range(h):				
				yp = (h/2)-y
				if self.__contains__((xp,yp))== True:
					draw_pixel(self.canvas, x, y)

def draw_pixel(canvas, x, y, color='#000000'):
	"""Draw a pixel at (x,y) on the given canvas"""
	x1, y1 = x - 1, y - 1
	x2, y2 = x + 1, y + 1
	canvas.create_oval(x1, y1, x2, y2, fill=color)


class Circle(drawable):
	def __init__(self,x,y,r):
		self.x = x
		self.y = y
		self.r = r 
	def __contains__(self, point):
		d = math.sqrt((point[0] - self.x)**2 + (point[1] - self.y)**2)
		if d<self.r:
			return True
		else:
			return False
	def __repr__(self):
		return 'Circle(%s %s %s) ' % (self.x, self.y, self.r)

class Rectangle(drawable):
	def __init__(self, x0, y0, x1, y1):
		self.x0 = x0
		self.y0 = y0
		self.x1 = x1
		self.y1 = y1
	def __contains__(self, point):
		if (self.x0<point[0]<self.x1 or self.x1>point[0]>self.x0) and (self.y0<point[1]<self.y1 or self.y1>point[1]>self.y0): 
			return True
		else:
			return False
	def __repr__(self):
		return 'Rectangle (%s, %s, %s, %s ) ' % (self.x0, self.y0, self.x1, self.y1)

class Intersection(drawable):
	def __init__(self, shape1, shape2):
		self.shape1 = shape1
		self.shape2 = shape2
	def __contains__(self, point):
		if self.shape1.__contains__(point) ==True and self.shape2.__contains__(point) ==True:
			return True
		else:
			return False
	def __repr__(self):
		return str(self.shape1) + ' Intersection ' + str(self.shape2)

class Union(drawable):
	def __init__(self, shape1, shape2):
		self.shape1 = shape1
		self.shape2 = shape2 
	def __contains__(self, point):
		if self.shape1.__contains__(point) ==True or self.shape2.__contains__(point) ==True:
			return True
		else:
			return False
	def __repr__(self):
		return str(self.shape1) + ' Union ' + str(self.shape2)

class Difference(drawable):
	def __init__(self, shape1, shape2):
		self.shape1 = shape1
		self.shape2 = shape2
	def __contains__(self, point):
		if self.shape1.__contains__(point) ==True and self.shape2.__contains__(point) ==False:
			return True
		else:
			return False
	def __repr__(self):
		return str(self.shape1) + ' Difference ' + str(self.shape2)

def main(shape):
    """Create a main window with a canvas to draw on"""
    master = tk.Tk()
    master.title("Drawing")
    canvas = tk.Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    print(shape)
    # Render the user-defined shape
    shape.draw(canvas)
    # TODO: Insert your code here!

    # Start the Tk event loop (in this case, it doesn't do anything other than
    # show the window, but we could have defined "event handlers" that intercept
    # mouse clicks, keyboard presses, etc.)
    tk.mainloop()


if __name__ == '__main__':
    # Create a "happy" face by subtracting two eyes and a mouth from a head
    head = Circle(0, 0, 200)
    left_eye = Circle(-70, 100, 20)
    right_eye = Circle(70, 100, 20)
    mouth = Rectangle(-90, -80, 90, -60)
    happy_face = head - left_eye - right_eye - mouth

    # Draw the happy face
    main(happy_face)

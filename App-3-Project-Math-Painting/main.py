from canvas import Canvas
from shapes import Square, Rectangle


canvas_width = int(input("Enter Canvas width: "))
canvas_height = int(input("Enter Canvas height: "))
if input("Enter canvas colour (Black or White)").lower() == "black":
    canvas_color = [0, 0, 0]
else:
    canvas_color = [255, 255, 255]

canvas = Canvas(canvas_height, canvas_width, color=canvas_color)
canvas.make()

decision = input("What would you like to draw? Enter quit to quit: ")

while decision != "quit":

    if decision == "rectangle":
        rect_x = int(input("Enter x of the rectangle: "))
        rect_y = int(input("Enter y of the rectangle: "))
        rect_width = int(input("Enter width of the rectangle: "))
        rect_height = int(input("Enter height of the rectangle: "))
        rect_r = int(input("How much red should the rectangle have? "))
        rect_g = int(input("How much green should the rectangle have? "))
        rect_b = int(input("How much blue should the rectangle have? "))
        rect_color = [rect_r, rect_g, rect_b]

        rec = Rectangle(rect_x, rect_y, rect_height, rect_width, color=rect_color)
        rec.draw(canvas)

    elif decision == "square":
        sq_x = int(input("Enter x of the square: "))
        sq_y = int(input("Enter y of the square: "))
        sq_side = int(input("Enter side of the square: "))
        sq_r = int(input("How much red should the square have? "))
        sq_g = int(input("How much green should the square have? "))
        sq_b = int(input("How much blue should the square have? "))
        sq_color = [sq_r, sq_g, sq_b]

        sq = Square(sq_x, sq_y, sq_side, color=sq_color)
        sq.draw(canvas)

    decision = input("What would you like to draw? Enter quit to quit: ")


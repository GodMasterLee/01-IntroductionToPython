"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Bowen Albert Li.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window=rg.TurtleWindow()
will=rg.SimpleTurtle('turtle')
william=rg.SimpleTurtle('turtle')
will.pen=rg.Pen('green',3)
william.pen=rg.Pen('red',3)
will.speed=100
william.speed=100
size=300
for k in range(13):
    will.draw_square(size)
    will.pen_up()
    will.right(45)
    will.forward(10)
    will.left(45)
    will.pen_down()
    size=size-10
    william.draw_circle(size)
    william.pen_up()
    william.left(45)
    william.forward(10)
    william.right(45)
    william.pen_down()
    size=size-10
window.close_on_mouse_click()
from manim import *
config.frame_height = 14.222222222222221
config.frame_width = 8.0
config.frame_size = (1080,1920)

class DefaultTemplate(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation



class Intro(Scene):
    def construct(self):
        pit = MathTex("a^2", "+", "b^2", "=", "c^2")
        pit[0].set_color(RED)
        pit[2].set_color(BLUE)
        pit[4].set_color(GREEN)

        pit.scale(2)
        #pit.shift(UP * 2)


        self.play(Write(pit))
        self.wait(1)
        self.play(pit.animate.shift(UP * 4), run_time=1)

        A = 2 * LEFT + 2 * UP
        B = 2 * LEFT + 2 * DOWN
        C = 2 * RIGHT + 2 * DOWN

        triangle = Polygon(A, B, C)
        self.add(triangle)

        left_cat = triangle.family_members_with_points()[0]
        #down_cat = triangle.submobjects[1]
        #hipo = triangle.submobjects[2]
        left_cat.set_color(RED)
        #down_cat.set_color(BLUE)
        #hipo.set_color(GREEN)

        

        self.play(Create(triangle))
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
        pit = MathTex("h^2 = c_1^2 + c_2^2")
        pit.to_edge(UP)

        circle = Circle()
        circle.set_fill(RED)

        self.play(Create(circle))

        self.play(Write(pit))
        self.play(FadeOut(pit))
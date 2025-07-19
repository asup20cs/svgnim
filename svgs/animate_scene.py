from manim import *
import sys

class AnimateSVG(Scene):
    def construct(self):
        # This script expects the SVG filename as the last argument
        # passed by the Manim command.
        svg_filename = "react.svg" # Default
        if len(sys.argv) > 1:
            svg_filename = sys.argv[-1]

        # Load the specified SVG file
        svg = SVGMobject(svg_filename).scale(3).center()

        self.play(DrawBorderThenFill(svg), run_time=3)
        self.wait(1)

        for _ in range(4):
            self.play(
                svg.animate.scale(1.15),
                run_time=0.45,
                rate_func=rate_functions.ease_out_sine
            )
            self.play(
                svg.animate.scale(1/1.15),
                run_time=0.45,
                rate_func=rate_functions.ease_in_sine
            )
        self.wait(2)

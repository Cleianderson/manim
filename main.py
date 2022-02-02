import os
from random import uniform, randint, choice
import numpy as np
from manimlib import *


class PythagorasTheorem(Scene):
    def construct(self):
        triangle = Polygon(LEFT + UP, 2 * RIGHT + DOWN, LEFT + DOWN)
        self.play(ShowCreation(triangle))
        self.wait()
        self.play(triangle.animate.scale(2))

        label_a = VGroup(Text("a"))
        a = always(label_a.next_to, triangle, LEFT)
        label_b = VGroup(Text("b"))
        b = always(label_b.next_to, triangle, RIGHT)
        label_c = VGroup(Text("c"))
        c = always(label_c.next_to, triangle, DOWN)
        self.add(a, b, c)
        self.embed()


class Linearization(Scene):
    points = ((-1, 2.05), (-.75, 1.153), (-.3, .5), (.2, .2), (.7, 1.2))

    def construct(self):
        axis = NumberPlane(background_line_style={
            "stroke_opacity": 0.5
        })
        # axis.set_width(10)
        # axis.scale(2.4,about_point=ORIGIN)
        self.play(ShowCreation(axis))
        self.wait()
        self.play(axis.animate.scale(2, about_point=np.array([0, 1, 0])))

        dot_group = Group()
        for i, point in enumerate(self.points):
            x, y = point

            dot = Dot(color=ORANGE)
            dot.move_to(axis.c2p(x, y))
            dot_group.add(dot)
            # self.play(ScaleInPlace(dot, 0.8, run_time=0.3))

        self.wait()
        for _dot in dot_group:
            self.play(ScaleInPlace(_dot, 0.8, run_time=0.2))

        identity_graph = axis.get_graph(lambda t: t, color=BLUE)
        identity_graph_label = axis.get_graph_label(
            identity_graph, label="y(x)=x")
        identity_graph_label.set_color(BLUE)

        minus_idn_graph = axis.get_graph(lambda t: -t, color=GREEN)
        minus_idn_graph_label = axis.get_graph_label(
            minus_idn_graph, label="g(x)=-x")
        minus_idn_graph_label.set_color(GREEN)

        exp_graph = axis.get_graph(lambda t: np.e ** t, color=PURPLE)
        exp_graph_label = axis.get_graph_label(exp_graph, label="h(x)=e^x")
        exp_graph_label.set_color(PURPLE)

        quadratic_graph = axis.get_graph(lambda t: t ** 2, color=PURPLE)
        quadratic_graph_label = axis.get_graph_label(quadratic_graph, label="i(x)=x^2")
        quadratic_graph_label.set_color(PURPLE)

        self.play(ShowCreation(identity_graph), FadeIn(identity_graph_label))
        self.wait()

        idn_points = identity_graph.get_points()
        dist = None
        for point in idn_points:
            _line = Line(dot_group[0], point)
            len_line = _line.get_length()
            if dist is None or len_line < dist.get_length():
                dist = _line
        dashed_dist = DashedLine(dist.get_start(), dist.get_end(), positive_space_ratio=0.2)
        self.play(ShowCreation(dashed_dist))
        self.wait()

        self.play(
            Uncreate(dashed_dist),
            Uncreate(identity_graph_label),
            Uncreate(identity_graph),
            Uncreate(dot_group),
            Uncreate(axis),
        )

        # self.play(
        #     ReplacementTransform(identity_graph, minus_idn_graph),
        #     ReplacementTransform(identity_graph_label, minus_idn_graph_label),
        # )

        # self.wait()
        # self.play(
        #     ReplacementTransform(minus_idn_graph, exp_graph),
        #     ReplacementTransform(minus_idn_graph_label, exp_graph_label),
        # )
        # self.wait()
        # self.play(
        #     ReplacementTransform(exp_graph, quadratic_graph),
        #     ReplacementTransform(exp_graph_label, quadratic_graph_label),
        # )
        config_text = {
            'font_size': 26
        }
        text1 = VGroup(
            Text('Dados ', **config_text),
            Tex('n ', **config_text),
            Text('pontos ', **config_text),
            Tex('(x_1,y_1),\\dots,(x_n,y_n)', **config_text),
            Text('e escolhendo ', **config_text),
            Tex('m', **config_text),
            Text('funções', **config_text),
            Tex('g_1(t), g_2(t),\\dots, g_m(t).', **config_text)
        )
        text2 = VGroup(
            Text('Queremos coeficientes', **config_text),
            Tex('a_1, a_2,\\dots, a_m', **config_text),
            Text(' tais que', **config_text),
        )
        
        text1.arrange(RIGHT)
        text2.arrange(RIGHT)

        points_text = VGroup(text1,text2)
        # points_text.align
        points_text.arrange(DOWN)

        function_phi = Tex('\\phi(x_i)=a_1g_1(x_i)+a_2g_2(x_i)+\\dots+a_mg_m(x_i)\\approx y_i,\\quad i=1,\\dots,n', font_size=42)
        self.play(ShowCreation(points_text))
        self.wait()
        self.play(points_text.animate.shift(3*UP))
        self.wait()

        self.play(ShowCreation(function_phi))
        # self.play(functions_g.animate.shift(3*UP),ShowCreation(function_phi))


        self.wait(2)
        # self.embed()


if __name__ == "__main__":
    file = 'main.py'
    scene = 'Linearization'
    render = True
    if render:
        os.system(f'manimgl -w {file} {scene}')
    else:
        os.system(f'manimgl {file} {scene}')

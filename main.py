import os
import numpy as np
from manimlib import *


class PythagorasTheorem(Scene):
    def construct(self):
        triangle = Polygon(LEFT + UP, 2 * RIGHT + DOWN, LEFT + DOWN)
        self.play(ShowCreation(triangle))
        self.wait(2)
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
        self.wait(2)
        self.play(axis.animate.scale(2, about_point=np.array([0, 1, 0])))

        dot_group = Group()
        for i, point in enumerate(self.points):
            x, y = point

            dot = Dot(color=ORANGE)
            dot.move_to(axis.c2p(x, y))
            dot_group.add(dot)
            # self.play(ScaleInPlace(dot, 0.8, run_time=0.3))

        self.wait(2)
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
        self.wait(2)

        idn_points = identity_graph.get_points()
        dist = None
        for point in idn_points:
            _line = Line(dot_group[0], point)
            len_line = _line.get_length()
            if dist is None or len_line < dist.get_length():
                dist = _line
        dashed_dist = DashedLine(dist.get_start(), dist.get_end(), positive_space_ratio=0.2)
        self.play(ShowCreation(dashed_dist))
        self.wait(2)

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

        # self.wait(2)
        # self.play(
        #     ReplacementTransform(minus_idn_graph, exp_graph),
        #     ReplacementTransform(minus_idn_graph_label, exp_graph_label),
        # )
        # self.wait(2)
        # self.play(
        #     ReplacementTransform(exp_graph, quadratic_graph),
        #     ReplacementTransform(exp_graph_label, quadratic_graph_label),
        # )
        config_text = {
            'font_size': 30
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

        function_phi = Tex('\\phi(x_i)=a_1g_1(x_i)+a_2g_2(x_i)+\\dots+a_mg_m(x_i)\\approx y_i,\\quad i=1,\\dots,n', **config_text)
        self.play(Write(points_text))
        self.wait(2)
        self.play(points_text.animate.shift(3*UP))
        self.wait(2)

        self.play(Write(function_phi))
        self.wait(2)
        # self.play(functions_g.animate.shift(3*UP),Write(function_phi))
        self.play(FadeOut(points_text))
        self.play(function_phi.animate.shift(3 * UP))
        self.wait(2)

        function_F = Tex('F(a_1,\\dots,a_m)=\\sum_{i=1}^m\\left[y_i-\phi(x_i)\\right]^2', **config_text)
        function_dF = Tex('\\frac{\\partial F}{\\partial a_k} = -2\\sum_{i=1}^m\\left[y_i-\\phi(x_i) \\right]g_k(x_i)', **config_text)

        self.play(Write(function_F))
        self.wait(2)

        self.play(function_F.animate.shift(1.5*UP))
        self.wait(0.5)
        self.play(Write(function_dF))
        self.wait(2)

        self.play(
            # FadeOut(function_phi),
            FadeOut(function_F),
            function_dF.animate.shift(2*UP),
        )
        self.wait(2)

        dF_zero_1 = Tex('\\frac{\\partial F}{\\partial a_k} = 0 \\Rightarrow', '\\sum_{i=1}^m', '\\left[y_i-\\phi(x_i) \\right]g_k(x_i)', '=','0', **config_text)
        dF_zero_2 = Tex('\\frac{\\partial F}{\\partial a_k} = 0 \\Rightarrow', '\\sum_{i=1}^m', 'y_ig_k(x_i)', '=','\\sum_{i=1}^m \\phi(x_i)g_k(x_i)', **config_text)
        dF_zero_3 = Tex('\\frac{\\partial F}{\\partial a_k} = 0 \\Rightarrow', '\\sum_{i=1}^m', 'y_ig_k(x_i)', '=','a_1\\sum_{i=1}^m g_1(x_i)g_k(x_i)+\\dots+a_m\\sum_{i=1}^m g_m(x_i)g_k(x_i)', **config_text)
        dF_zero_4 = Tex('\\frac{\\partial F}{\\partial a_k} = 0 \\Rightarrow', ' b_k = a_1 s_{k 1} + \\dots + a_m s_{k m}',',\\quad b_k=\\sum_{i=1}^m y_ig_k(x_i),\\quad s_{k m}=\\sum_{i=1}^m g_m(x_i)g_k(x_i)', **config_text)
        dF_zero_4.shift(0.6*RIGHT)
        dF_zero_4.shift(2 * UP)

        self.play(Write(dF_zero_1))
        self.wait(2)
        self.play(TransformMatchingTex(dF_zero_1, dF_zero_2))
        self.wait(2)
        self.play(TransformMatchingTex(dF_zero_2, dF_zero_3))
        self.wait(2)

        self.play(
            FadeOut(function_phi),
            FadeOut(function_dF),
            dF_zero_3.animate.shift(3*UP)
        )
        self.wait(2)
        self.play(Write(dF_zero_4))
        self.wait(2)

        b_1 = Tex('b_1 = a_1 s_{1 1} + \\dots + a_m s_{1 m}', **config_text)
        b_1.shift(0.5*UP)
        b_2 = Tex('b_2 = a_1 s_{2 1} + \\dots + a_m s_{2 m}', **config_text)
        vdots = Tex('\\vdots', **config_text)
        vdots.shift(0.5*DOWN)
        b_m = Tex('b_m = a_1 s_{m 1} + \\dots + a_m s_{m m}', **config_text)
        b_m.shift(DOWN)

        self.play(TransformFromCopy(dF_zero_4[1], b_1))
        self.wait(0.5)
        self.play(TransformFromCopy(dF_zero_4[1], b_2),FadeIn(vdots))
        self.wait(0.5)
        self.play(TransformFromCopy(dF_zero_4[1], b_m))

        equal = Tex(' =')
        left_right_arrow = Tex(' \\Leftrightarrow')
        left_right_arrow.shift(2.7*LEFT)
        b_matrix = Matrix([
            [' b_1'],
            [' b_2'],
            ['\\vdots'],
            [' b_m']
            ])
        a_matrix = Matrix([
            [' a_1'],
            [' a_2'],
            ['\\vdots'],
            [' a_m']
            ])

        s_matrix = Matrix([
            [' s_{11}', '\\dots', ' s_{1m}'],
            [' s_{21}', '\\dots', ' s_{2m}'],
            ['\\vdots', '\\ddots', ' \\vdots'], 
            [' s_{m1}', '\\dots', ' s_{mm}']
            ])

        equal.shift(0.5*LEFT)
        b_matrix.shift(1.5*LEFT)
        s_matrix.shift(2*RIGHT)
        a_matrix.shift(5*RIGHT)

        sys_matrix = VGroup(left_right_arrow, b_matrix, equal, s_matrix, a_matrix)
        sys_matrix.scale(4/6.5)
        sys_matrix.shift(0.3*DOWN)
        sys_matrix.shift(0.5*RIGHT)
        sys = VGroup(b_1,b_2,vdots,b_m)

        self.wait(2)
        self.play(sys.animate.shift(2.5*LEFT))
        self.wait(2)
        self.play(Write(sys_matrix))

        self.wait(2)
        # self.embed()


if __name__ == "__main__":
    file = 'main.py'
    scene = 'Linearization'
    render = False
    if render:
        os.system(f'manimgl -w {file} {scene}')
    else:
        os.system(f'manimgl {file} {scene}')

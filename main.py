from manim import *

class MainPage(Scene):
    def construct(self): 
        mainText = Text("Algorytm Dijkstry", font_size=64, color=WHITE)
        self.play(Write(mainText), run_time = 1)
        self.play(mainText.animate.shift(UP*3), run_time=1)

        author1 = Text("Szymon Michoń", font_size=20, color=GREY).move_to([0,2.2,0])
        author2 = Text("Patryk Murzyn", font_size=20, color=GREY).move_to([0,1.8,0])

        self.play(Write(author1), Write(author2))
        self.play(FadeOut(author1), FadeOut(author2))

        infoText = Text("Opracowany przez holenderskiego informatyka Edsgera Dijkstrę,\nsłuży do znajdowania najkrótszej ścieżki z pojedynczego źródła w grafie.").move_to([0,1.5,0])
        
        infoText.scale(0.5)

        self.play(Write(infoText))

        photo = ImageMobject("img/Edsger_Wybe_Dijkstra.jpg").move_to([-5,-1.5,0])

        photo.scale(0.35)

        self.play(FadeIn(photo))

        infoText2 = Text("Z algorytmu Dijkstry można skorzystać przy\nobliczaniu najkrótszej drogi do danej miejscowości.\nWystarczy przyjąć, że każdy z punktów\nskrzyżowań dróg to jeden z wierzchołków grafu,\na odległości między punktami to wagi krawędzi.\nJest często używany w sieciach komputerowych,\nnp. przy trasowaniu (wyznaczanie trasy i wysłanie nią\npakietu danych w sieci komputerowej)").move_to([1.5,-1.2,0])

        infoText2.scale(0.5)

        self.play(Write(infoText2))

        self.wait(0.5)

class Graff(Scene):
    def construct(self):

        runTime = 1.0

        a = Circle(radius=0.3, color=RED, fill_opacity=1.0).move_to([-3,-1,0])
        textA = Text("A", font_size=26, color=BLACK).move_to(a.get_center())
        self.play(DrawBorderThenFill(a), FadeIn(textA), run_time=runTime)

        b = Circle(radius=0.3, color=RED, fill_opacity=1.0).move_to([-1,-2,0])
        textB = Text("B", font_size=26, color=BLACK).move_to(b.get_center())
        self.play(DrawBorderThenFill(b), FadeIn(textB), run_time=runTime)

        c = Circle(radius=0.3, color=RED, fill_opacity=1.0).move_to([-1,0,0])
        textC = Text("C", font_size=26, color=BLACK).move_to(c.get_center())
        self.play(DrawBorderThenFill(c), FadeIn(textC), run_time=runTime)

        d = Circle(radius=0.3, color=RED, fill_opacity=1.0).move_to([1,0.5,0])
        textD = Text("D", font_size=26, color=BLACK).move_to(d.get_center())
        self.play(DrawBorderThenFill(d), FadeIn(textD), run_time=runTime)

        e = Circle(radius=0.3, color=RED, fill_opacity=1.0).move_to([-0.5,2,0])
        textE = Text("E", font_size=26, color=BLACK).move_to(e.get_center())
        self.play(DrawBorderThenFill(e), FadeIn(textE), run_time=runTime)

        f = Circle(radius=0.3, color=RED, fill_opacity=1.0).move_to([-2.5,1,0])
        textF = Text("F", font_size=26, color=BLACK).move_to(f.get_center())
        self.play(DrawBorderThenFill(f), FadeIn(textF), run_time=runTime)

        self.wait(0.5)

        SqrA = Square(side_length=0.6, color=YELLOW, fill_opacity=1.0).move_to([-3,-1,0])

        self.play(Transform(a, SqrA), run_time=runTime)

        self.wait(0.5)

        SqrE = Square(side_length=0.6, color=BLUE, fill_opacity=1.0).move_to([-0.5,2,0])

        self.play(Transform(e, SqrE), run_time=runTime)

        self.wait(0.5)



        lAB= Line(a, b, z_index = -1)
        lAB.put_start_and_end_on(a.get_center(), b.get_center())

        lAC= Line(a, c, z_index = -1)
        lAC.put_start_and_end_on(a.get_center(), c.get_center())

        lAF= Line(a, f, z_index = -1)
        lAF.put_start_and_end_on(a.get_center(), f.get_center())

        self.play(Create(lAB), Create(lAC), Create(lAF))

        

        lBC= Line(b, c, z_index = -1)
        lBC.put_start_and_end_on(b.get_center(), c.get_center())

        lBD= Line(b, d, z_index = -1)
        lBD.put_start_and_end_on(b.get_center(), d.get_center())

        lCD= Line(c, d, z_index = -1)
        lCD.put_start_and_end_on(c.get_center(), d.get_center())

        lCE= Line(c, e, z_index = -1)
        lCE.put_start_and_end_on(c.get_center(), e.get_center())

        lCF= Line(c, f, z_index = -1)
        lCF.put_start_and_end_on(c.get_center(), f.get_center())

        lFE= Line(f, e, z_index = -1)
        lFE.put_start_and_end_on(f.get_center(), e.get_center())

        lDE= Line(d, e, z_index = -1)
        lDE.put_start_and_end_on(d.get_center(), e.get_center())

        self.play(Create(lBC), Create(lBD), Create(lCD), Create(lCE), Create(lCF), Create(lFE), Create(lDE))

        self.wait(1)




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

def refreshTable(data):
    t0 = Table(
            [[data[0][0], data[1][0]],
            [data[0][1], data[1][1]],
            [data[0][2], data[1][2]],
            [data[0][3], data[1][3]],
            [data[0][4], data[1][4]],
            [data[0][5], data[1][5]]],
            row_labels=[Text("A"), Text("B"), Text("C"), Text("D"), Text("E"), Text("F")],
            col_labels=[Text("Shortest\ndistance\nfrom A"), Text("Previous\nvertex")],
            top_left_entry=Text("Vertex")).move_to([6,-0.7,0]).scale(0.5)
    return t0

class Graff(MovingCameraScene):
    
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

        lCF= Line(c, f, z_index = -1)
        lCF.put_start_and_end_on(c.get_center(), f.get_center())

        lFE= Line(f, e, z_index = -1)
        lFE.put_start_and_end_on(f.get_center(), e.get_center())

        lDE= Line(d, e, z_index = -1)
        lDE.put_start_and_end_on(d.get_center(), e.get_center())

        self.play(Create(lBC), Create(lBD), Create(lCD), Create(lCF), Create(lFE), Create(lDE))

        self.wait(1)

        valAB = Text("7", font_size=16,).move_to((a.get_center()+b.get_center())/ 2 + [0.15, 0.15, 0])
        valAC = Text("9", font_size=16,).move_to((a.get_center()+c.get_center())/ 2 + [0.15, -0.15, 0])
        valAF = Text("14", font_size=16,).move_to((a.get_center()+f.get_center())/ 2 + [0.3, 0, 0])
        valBD = Text("15", font_size=16,).move_to((b.get_center()+d.get_center())/ 2 + [0.3, 0, 0])
        valBC = Text("10", font_size=16,).move_to((b.get_center()+c.get_center())/ 2 + [0.3, 0.15, 0])
        valCD = Text("11", font_size=16,).move_to((c.get_center()+d.get_center())/ 2 + [0, -0.15, 0])
        valCF = Text("2", font_size=16,).move_to((c.get_center()+f.get_center())/ 2 + [0.15, 0.15, 0])
        valFE = Text("9", font_size=16,).move_to((f.get_center()+e.get_center())/ 2 + [0.15, -0.15, 0])
        valDE = Text("6", font_size=16,).move_to((d.get_center()+e.get_center())/ 2 + [0.15, 0.15, 0])

        self.play(Write(valAB), Write(valAC), Write(valAF), Write(valBD), Write(valBC), Write(valCD), Write(valCF), Write(valFE), Write(valDE))

        self.play(self.camera.frame.animate.move_to(RIGHT* 3))

        visitedText = Text("Visited = []", font_size=26).move_to([6,3,0])

        unvisitedText = Text("Unvisited = [A, B, C, D, E, F]", font_size=26).move_to([6,2.5,0])

        self.play(Write(visitedText), Write(unvisitedText))

        data = [["0", "∞", "∞", "∞", "∞", "∞"], ["-", "-", "-", "-", "-", "-"]]

        t0 = Table(
            [[data[0][0], data[1][0]],
            [data[0][1], data[1][1]],
            [data[0][2], data[1][2]],
            [data[0][3], data[1][3]],
            [data[0][4], data[1][4]],
            [data[0][5], data[1][5]]],
            row_labels=[Text("A"), Text("B"), Text("C"), Text("D"), Text("E"), Text("F")],
            col_labels=[Text("Shortest\ndistance\nfrom A"), Text("Previous\nvertex")],
            top_left_entry=Text("Vertex")).move_to([6,-0.7,0]).scale(0.5)

        self.play(FadeIn(t0))

        b.set_color([YELLOW, GREEN])
        lAB.set_color(GREEN)
        valAB.set_color([YELLOW, GREEN])

        equ = MathTex("0", "+", "7", "=", "7").move_to([-2,-3,0])
        equ[4].set_color(YELLOW)

        self.play(Write(equ))
        self.wait(0.5)

        data[0][1] = "7"
        data[1][1] = "A"

        self.remove(t0)

        t0 = refreshTable(data)

        t0.get_entries((3,2)).set_color(YELLOW)
        t0.get_entries((3,3)).set_color(YELLOW)
        self.add(t0)

        self.wait(1)

        

        b.set_color(RED)
        lAB.set_color(WHITE)
        valAB.set_color(WHITE)

        c.set_color([YELLOW, GREEN])
        lAC.set_color(GREEN)
        valAC.set_color([YELLOW, GREEN])
        
        self.play(FadeOut(equ))

        equ = MathTex("0", "+", "9", "=", "9").move_to([-2,-3,0])
        equ[4].set_color(YELLOW)

        self.play(Write(equ))

        data[0][2] = "9"
        data[1][2] = "A"

        self.remove(t0)
        t0 = refreshTable(data)

        t0.get_entries((4,2)).set_color(YELLOW)
        t0.get_entries((4,3)).set_color(YELLOW)
        self.add(t0)

        self.wait(1)

        


        c.set_color(RED)
        lAC.set_color(WHITE)
        valAC.set_color(WHITE)

        f.set_color([YELLOW, GREEN])
        lAF.set_color(GREEN)
        valAF.set_color([YELLOW, GREEN])
        
        self.play(FadeOut(equ))

        equ = MathTex("0", "+", "14", "=", "14").move_to([-2,-3,0])
        equ[4].set_color(YELLOW)
        self.play(Write(equ))

        data[0][5] = "14"
        data[1][5] = "A"

        self.remove(t0)
        t0 = refreshTable(data)

        t0.get_entries((7,2)).set_color(YELLOW)
        t0.get_entries((7,3)).set_color(YELLOW)
        self.add(t0)

        self.play(FadeOut(visitedText), FadeOut(unvisitedText))
        visitedText = Text("Visited = [A]", font_size=26).move_to([6,3,0])
        unvisitedText = Text("Unvisited = [B, C, D, E, F]", font_size=26).move_to([6,2.5,0])
        self.play(FadeIn(visitedText), FadeIn(unvisitedText))

        
        t0.get_entries((7,2)).set_color(WHITE)
        t0.get_entries((7,3)).set_color(WHITE)
        t0.get_entries((3,1)).set_color(YELLOW)
        t0.get_entries((3,2)).set_color(YELLOW)
        t0.get_entries((3,3)).set_color(YELLOW)
        self.play(FadeOut(equ))
        equ = MathTex("7", " < 9 < 14").move_to([-2,-3,0])
        equ[0].set_color(YELLOW)
        self.play(Write(equ))

        self.wait(1)

        

        t0.get_entries((3,1)).set_color(WHITE)
        t0.get_entries((3,2)).set_color(WHITE)
        t0.get_entries((3,3)).set_color(WHITE)

        c.set_color(RED)
        lAC.set_color(WHITE)
        valAC.set_color(WHITE)

        c.set_color([YELLOW, GREEN])
        lBC.set_color(GREEN)
        valBC.set_color([YELLOW, GREEN])
        
        self.play(FadeOut(equ))

        equ = MathTex("7", "+", "10", "=", "17", "> 9").move_to([-2,-3,0])
        equ[5].set_color(RED)
        equ[4].set_color(YELLOW)
        self.play(Write(equ))

        t0.get_entries((4,2)).set_color(RED)

        self.add(t0)

        self.wait(1)

        


        c.set_color(RED)
        lBC.set_color(WHITE)
        valBC.set_color(WHITE)

        d.set_color([YELLOW, GREEN])
        lBD.set_color(GREEN)
        valBD.set_color([YELLOW, GREEN])
        
        self.play(FadeOut(equ))

        equ = MathTex("7", "+", "15", "=", "22").move_to([-2,-3,0])
        equ[4].set_color(YELLOW)
        self.play(Write(equ))

        data[0][3] = "22"
        data[1][3] = "B"

        self.remove(t0)
        t0 = refreshTable(data)

        t0.get_entries((5,2)).set_color(YELLOW)
        t0.get_entries((5,3)).set_color(YELLOW)
        self.add(t0)

        self.play(FadeOut(visitedText), FadeOut(unvisitedText))
        visitedText = Text("Visited = [A, B]", font_size=26).move_to([6,3,0])
        unvisitedText = Text("Unvisited = [C, D, E, F]", font_size=26).move_to([6,2.5,0])
        self.play(FadeIn(visitedText), FadeIn(unvisitedText))

        
        t0.get_entries((5,2)).set_color(WHITE)
        t0.get_entries((5,3)).set_color(WHITE)
        t0.get_entries((4,1)).set_color(YELLOW)
        t0.get_entries((4,2)).set_color(YELLOW)
        t0.get_entries((4,3)).set_color(YELLOW)
        self.play(FadeOut(equ))
        equ = MathTex("7 < ", "9", " < 14 < 22").move_to([-2,-3,0])
        equ[1].set_color(YELLOW)
        self.play(Write(equ))

        self.wait(1)



        











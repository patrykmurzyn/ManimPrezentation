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

        infoText = Tex("Opracowany przez holenderskiego informatyka Edsgera Dijkstre, służy do znajdowania najkrótszej ścieżki z pojedynczego źródła w grafie.").move_to([0,1.5,0])
        
        infoText.scale(0.8)

        self.play(Write(infoText))

        photo = ImageMobject("img/Edsger_Wybe_Dijkstra.jpg").move_to([-5,-1.5,0])

        photo.scale(0.35)

        self.play(FadeIn(photo))

        infoText2 = Tex("\k{e}")

        #infoText2.width = 0.5

        #self.play(Write(infoText2))

        self.wait(1)

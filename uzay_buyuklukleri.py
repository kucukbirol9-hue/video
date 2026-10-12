"""
Uzay Kâşifleri - Bölüm 1: Uzaydaki şeyler gerçekte ne kadar büyük?

Hızlı önizleme (düşük kalite):  manim -ql uzay_buyuklukleri.py UzayBuyuklukleri
YouTube için (1080p, 60fps):    manim -qh uzay_buyuklukleri.py UzayBuyuklukleri

Not: LaTeX kullanılmadı, sadece Text kullanıldı. Böylece Türkçe karakterler
(ş, ğ, ü, ı, ö, ç) sorunsuz görünür ve render daha hızlı olur.
"""
from manim import *
import random

ARKA_PLAN = "#0B1026"
DUNYA_MAVI = "#3B82F6"
DUNYA_YESIL = "#22C55E"
AY_GRI = "#BFC5CC"
AY_KRATER = "#8E959E"
JUPITER_GOVDE = "#D9A066"
GUNES_SARI = "#FFD43B"
VURGU = "#FFD43B"

# Ölçek: küçük sahnelerde Dünya'nın yarıçapı
DUNYA_KUCUK_R = 0.24


def sayi_yaz(n):
    """1300000 -> '1.300.000' (Türkçe binlik ayracı)"""
    return f"{int(round(n)):,}".replace(",", ".")


def sigdir(mob, max_genislik):
    if mob.width > max_genislik:
        mob.scale_to_fit_width(max_genislik)
    return mob


class UzayBuyuklukleri(Scene):
    def construct(self):
        self.camera.background_color = ARKA_PLAN
        self.arka = self.yildizlar()
        self.add(self.arka)

        self.giris()
        self.dunya_ve_ay()
        self.jupiter()
        self.gunes()
        self.kapanis()

    # ------------------------------------------------------------------
    # Yardımcılar
    # ------------------------------------------------------------------
    def yildizlar(self):
        random.seed(7)
        grup = VGroup()
        for _ in range(160):
            y = Dot(
                point=[random.uniform(-7.1, 7.1), random.uniform(-4, 4), 0],
                radius=random.uniform(0.008, 0.03),
                color=WHITE,
            )
            y.set_opacity(random.uniform(0.3, 0.9))
            grup.add(y)
        return grup

    def temizle(self, haric=()):
        silinecek = [m for m in self.mobjects if m is not self.arka and m not in haric]
        if silinecek:
            self.play(*[FadeOut(m) for m in silinecek])

    def dunya_ciz(self, r):
        okyanus = Circle(radius=r, fill_color=DUNYA_MAVI, fill_opacity=1, stroke_width=0)
        kita1 = Ellipse(width=r * 0.9, height=r * 0.6, fill_color=DUNYA_YESIL,
                        fill_opacity=1, stroke_width=0).shift(LEFT * r * 0.3 + UP * r * 0.25)
        kita2 = Ellipse(width=r * 0.6, height=r * 0.8, fill_color=DUNYA_YESIL,
                        fill_opacity=1, stroke_width=0).shift(RIGHT * r * 0.35 + DOWN * r * 0.3)
        return VGroup(okyanus, kita1, kita2)

    def ay_ciz(self, r):
        yuzey = Circle(radius=r, fill_color=AY_GRI, fill_opacity=1, stroke_width=0)
        kraterler = VGroup(
            Circle(radius=r * 0.22).shift(LEFT * r * 0.35 + UP * r * 0.3),
            Circle(radius=r * 0.15).shift(RIGHT * r * 0.4 + DOWN * r * 0.1),
            Circle(radius=r * 0.10).shift(LEFT * r * 0.1 + DOWN * r * 0.5),
        ).set_style(fill_color=AY_KRATER, fill_opacity=1, stroke_width=0)
        return VGroup(yuzey, kraterler)

    def jupiter_ciz(self, r):
        govde = Circle(radius=r, fill_color=JUPITER_GOVDE, fill_opacity=1, stroke_width=0)
        seritler = VGroup()
        for y, renk in [(0.45, "#B9773E"), (0.10, "#EBCDA5"), (-0.30, "#B9773E"), (-0.65, "#C98B52")]:
            serit = Intersection(
                govde.copy(),
                Rectangle(width=2.2 * r, height=r * 0.16).move_to(UP * y * r),
                fill_color=renk, fill_opacity=1, stroke_width=0,
            )
            seritler.add(serit)
        leke = Ellipse(width=r * 0.35, height=r * 0.2, fill_color="#C1440E",
                       fill_opacity=1, stroke_width=0).move_to(RIGHT * r * 0.3 + DOWN * r * 0.3)
        return VGroup(govde, seritler, leke)

    # ------------------------------------------------------------------
    # 1) Giriş
    # [ANLATIM 1] "Merhaba uzay kâşifleri! Bugün çok büyük bir soru soruyoruz:
    #              Uzaydaki şeyler gerçekte ne kadar büyük?"
    # ------------------------------------------------------------------
    def giris(self):
        t1 = Text("Uzaydaki şeyler", font_size=56)
        t2 = Text("gerçekte ne kadar büyük?", font_size=56, color=VURGU, weight=BOLD)
        grup = VGroup(t1, t2).arrange(DOWN, buff=0.4)
        self.play(Write(t1), run_time=1.5)
        self.play(Write(t2), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(grup))

    # ------------------------------------------------------------------
    # 2) Dünya ve Ay
    # [ANLATIM 2] "Bu bizim evimiz, Dünya. Yanındaki küçük gri top da Ay.
    #              Ay, Dünya'nın yaklaşık dörtte biri genişliğinde."
    # [ANLATIM 3] "Peki Dünya'nın içini Aylarla doldursak kaç tane sığardı?
    #              Sayalım... Yaklaşık 50 tane!"
    # ------------------------------------------------------------------
    def dunya_ve_ay(self):
        baslik = Text("Dünya ve Ay", font_size=40, weight=BOLD).to_edge(UP)
        dunya = self.dunya_ciz(1.4).move_to(LEFT * 3.5)
        dunya_et = Text("Dünya", font_size=28).next_to(dunya, DOWN)
        ay = self.ay_ciz(1.4 / 3.67).next_to(dunya, RIGHT, buff=1.2)
        ay_et = Text("Ay", font_size=28).next_to(ay, DOWN)

        self.play(FadeIn(baslik, shift=DOWN * 0.3))
        self.play(GrowFromCenter(dunya), FadeIn(dunya_et))
        self.wait(1.5)
        self.play(GrowFromCenter(ay), FadeIn(ay_et))
        self.wait(2.5)

        soru = Text("Dünya'nın içine kaç tane Ay sığar?", font_size=34, color=VURGU).to_edge(DOWN)
        self.play(Write(soru))
        self.wait(1.5)
        self.play(FadeOut(ay), FadeOut(ay_et))

        aylar = VGroup(*[self.ay_ciz(0.22) for _ in range(49)])
        aylar.arrange_in_grid(rows=7, cols=7, buff=0.12).move_to(RIGHT * 2.5 + DOWN * 0.2)

        t = ValueTracker(0)
        sayac = always_redraw(
            lambda: Text(f"{sayi_yaz(t.get_value())} Ay", font_size=40, weight=BOLD)
            .next_to(aylar, UP, buff=0.25)
        )
        self.add(sayac)
        self.play(
            LaggedStart(*[GrowFromCenter(a) for a in aylar], lag_ratio=0.1),
            t.animate.set_value(49),
            run_time=5,
            rate_func=linear,
        )
        sayac.clear_updaters()
        sonuc = Text("Yaklaşık 50 tane!", font_size=44, color=VURGU, weight=BOLD).move_to(sayac)
        self.play(ReplacementTransform(sayac, sonuc))
        self.wait(2)
        self.temizle()

    # ------------------------------------------------------------------
    # 3) Jüpiter
    # [ANLATIM 4] "Şimdi Güneş Sistemi'nin en büyük gezegenine bakalım: Jüpiter!
    #              Yanındaki minicik top Dünya. Jüpiter o kadar büyük ki
    #              içine yaklaşık 1.300 tane Dünya sığar!"
    # ------------------------------------------------------------------
    def jupiter(self):
        baslik = Text("Dev gezegen: Jüpiter", font_size=40, weight=BOLD).to_edge(UP)
        jup = self.jupiter_ciz(DUNYA_KUCUK_R * 11).move_to(LEFT * 3.2 + DOWN * 0.3)
        jup_et = Text("Jüpiter", font_size=28).next_to(jup, DOWN, buff=0.15)
        dunya = self.dunya_ciz(DUNYA_KUCUK_R).move_to(RIGHT * 3.5 + UP * 1.6)
        dunya_et = Text("Dünya", font_size=24).next_to(dunya, DOWN, buff=0.15)

        self.play(FadeIn(baslik, shift=DOWN * 0.3))
        self.play(GrowFromCenter(jup), FadeIn(jup_et), run_time=1.5)
        self.wait(1)
        self.play(GrowFromCenter(dunya), FadeIn(dunya_et))
        self.play(Indicate(dunya, scale_factor=1.8, color=WHITE))
        self.wait(1)

        etiket = Text("İçine sığan Dünya sayısı:", font_size=28).move_to(RIGHT * 3.5 + DOWN * 0.3)
        t = ValueTracker(0)
        sayac = always_redraw(
            lambda: Text(sayi_yaz(t.get_value()), font_size=60, weight=BOLD, color=VURGU)
            .next_to(etiket, DOWN, buff=0.35)
        )
        self.play(FadeIn(etiket))
        self.add(sayac)
        self.play(t.animate.set_value(1300), run_time=4, rate_func=smooth)
        sayac.clear_updaters()
        self.wait(2.5)

        self.play(FadeOut(baslik), FadeOut(etiket), FadeOut(sayac))
        # Jüpiter ve Dünya bir sonraki sahnede kalıyor
        self.jup_grup = VGroup(jup, jup_et)
        self.dunya_grup = VGroup(dunya, dunya_et)

    # ------------------------------------------------------------------
    # 4) Güneş
    # [ANLATIM 5] "Ama asıl dev henüz gelmedi... Güneş! Bak, koca Jüpiter bile
    #              Güneş'in yanında küçücük kalıyor. Güneş'in içine 1 milyondan
    #              fazla Dünya sığar! Saniyede bir tane sayarak bir milyona kadar
    #              saysan, gece gündüz hiç durmadan 11 günden fazla sürer!"
    # ------------------------------------------------------------------
    def gunes(self):
        r = DUNYA_KUCUK_R * 109  # Güneş, Dünya'dan ~109 kat geniş
        gunes = Circle(radius=r, fill_color=GUNES_SARI, fill_opacity=1,
                       stroke_color=ORANGE, stroke_width=10)
        parilti = VGroup(*[
            Circle(radius=r + 0.25 * i, fill_opacity=0, stroke_color=GUNES_SARI,
                   stroke_width=24, stroke_opacity=0.25 / i)
            for i in range(1, 4)
        ])
        gunes_g = VGroup(parilti, gunes)
        hedef = LEFT * (r + 2.6)  # sağ kenarı x = -2.6'da görünsün
        gunes_g.move_to(hedef + LEFT * 8)

        self.play(
            gunes_g.animate.move_to(hedef),
            self.jup_grup.animate.shift(RIGHT * 3.8),
            self.dunya_grup.animate.shift(RIGHT * 1.8 + DOWN * 1.6),
            run_time=3,
            rate_func=smooth,
        )
        gunes_et = Text("Güneş", font_size=44, weight=BOLD, color="#7A3E00").move_to(LEFT * 5.2)
        baslik = Text("Ve asıl dev: Güneş!", font_size=36, weight=BOLD).to_corner(UR)
        not_ = Text("Hepsi aynı ölçekte!", font_size=24, color=GREY_B).to_corner(DR)
        self.play(FadeIn(gunes_et), FadeIn(baslik), FadeIn(not_))
        self.wait(3)

        # Jüpiter çekilir, Dünya köşeye gider, sayaç başlar
        self.play(
            FadeOut(self.jup_grup), FadeOut(not_),
            self.dunya_grup.animate.move_to(RIGHT * 5.6 + UP * 1.9),
        )
        etiket = sigdir(Text("Güneş'in içine sığan Dünya sayısı:", font_size=28), 6.2)
        etiket.move_to(RIGHT * 1.6 + UP * 1.0)
        t = ValueTracker(0)
        sayac = always_redraw(
            lambda: Text(sayi_yaz(t.get_value()), font_size=64, weight=BOLD, color=VURGU)
            .next_to(etiket, DOWN, buff=0.4)
        )
        self.play(FadeIn(etiket))
        self.add(sayac)
        self.play(t.animate.set_value(1_300_000), run_time=5, rate_func=smooth)
        sayac.clear_updaters()

        sonuc = Text("1 milyondan fazla!", font_size=40, weight=BOLD).next_to(sayac, DOWN, buff=0.4)
        self.play(FadeIn(sonuc, scale=1.3))
        self.wait(1.5)

        bilgi = VGroup(
            Text("Saniyede bir sayarak saysan bile", font_size=28),
            Text("11 günden fazla sürer!", font_size=28, color=VURGU),
        ).arrange(DOWN, buff=0.15).next_to(sonuc, DOWN, buff=0.45)
        sigdir(bilgi, 6.2)
        self.play(Write(bilgi), run_time=2)
        self.wait(3)
        self.temizle()

    # ------------------------------------------------------------------
    # 5) Kapanış
    # [ANLATIM 6] "Ve işin en şaşırtıcı yanı: Güneş, evrendeki milyarlarca
    #              yıldızdan sadece biri. Bir sonraki videoda görüşmek üzere,
    #              uzay kâşifleri!"
    # ------------------------------------------------------------------
    def kapanis(self):
        t1 = Text("Güneş, evrendeki milyarlarca", font_size=40)
        t2 = Text("yıldızdan sadece biri!", font_size=40, color=VURGU, weight=BOLD)
        grup = VGroup(t1, t2).arrange(DOWN, buff=0.3)
        self.play(FadeIn(grup, shift=UP * 0.3))
        self.play(self.arka.animate.set_opacity(1), run_time=2)
        self.wait(2)
        self.play(FadeOut(grup))

        veda = Text("Bir sonraki videoda görüşmek üzere,\nuzay kâşifleri!",
                    font_size=40, line_spacing=1.2)
        self.play(Write(veda), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(veda))

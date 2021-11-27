import pyxel


class Game():
    def __init__(self):
        pyxel.init(250, 180, caption="SUPER MARIO WORKER")
        pyxel.load("assets/resources.pyxres")
        self.posicionX = 115
        self.posicionY = 80
        self.sentidoX = 1
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_A):
            self.posicionX -= 4
            self.sentidoX = -1
        elif pyxel.btnp(pyxel.KEY_D):
            self.posicionX += 4
            self.sentidoX = 1
        if pyxel.btnp(pyxel.KEY_W):
            self.posicionY -= 4

    def draw(self):
        pyxel.cls(12)
        pyxel.blt(self.posicionX, self.posicionY, 1, 0, 48, self.sentidoX * 16, 32)


Game()

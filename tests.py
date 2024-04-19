from operacoes import Operacoes

class TesteOperacoes:
    def setup_method(self):
        self.operacoes = Operacoes()
        
    def test_soma(self):
        assert self.operacoes.soma(1, 1) == 2
        assert self.operacoes.soma(-1, 1) == 0 
        assert self.operacoes.soma(0, 0) == 0

    def test_sub(self):
        assert self.operacoes.sub(5, 3) == 2
        assert self.operacoes.sub(-1, -1) == 0
        assert self.operacoes.sub(5, 10) == -5

    def test_multi(self):
        assert self.operacoes.multi(10, 3) == 30
        assert self.operacoes.multi(100, 0) == 0
        assert self.operacoes.multi(20, -3) == -60

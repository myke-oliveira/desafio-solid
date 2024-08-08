from abc import ABC, abstractmethod

class Exame:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

class AprovarExame(ABC):

    @abstractmethod
    def aprovar_solicitacao_exame(self, exame: Exame): pass


class AprovarExameSangue(AprovarExame):

    def aprovar_solicitacao_exame(self, exame: Exame):
        if self.__verifica_condicoes_exame(exame):
            print("Exame sanguíneo aprovado!")

    def __verifica_condicoes_exame(self, exame: Exame):
        pass


class AprovarExameRaioX(AprovarExame):

    def aprovar_solicitacao_exame(self, exame: Exame):
        if self.__verifica_condicoes_exame(exame):
            print("Raio-X aprovado!")

    def __verifica_condicoes_exame(self, exame: Exame):
        pass


exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovar_exame_sangue = AprovarExameSangue()
aprovar_exame_raio_x = AprovarExameRaioX()

aprovar_exame_sangue.aprovar_solicitacao_exame(exame_sangue)
aprovar_exame_raio_x.aprovar_solicitacao_exame(exame_sangue)

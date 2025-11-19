package maqest;

import agente.Accao;

/*
Dinamica - Forma como se dá a evolução do estado do Sistema é uma função de transformação que,
perante o estado actual e as entradas actuais, produz o estado seguinte e as saídas seguintes.

 Eventos de mudança da Maquina de Estados (Transição):
	Animal: Procurar/Inspeção, muda para observação.
	Ruído: Procura, muda para inspeção.
	Silêncio: Inspeção, muda para procura.
	Fuga: , muda para inspeção/procura.
	Fotografia: , muda para procura.

	Função de Transição de Estados:
	Representa a lógica de mudança entre estados, dependendo do evento atual.
 */

public class Transicao {

    private Estado estadoSucessor;
    private Accao accao;

    public Transicao(Estado estadoSucessor, Accao accao) {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    //A classe Transicao encapsula informações importantes que precisam ser acessadas
    // por outras partes do código, portanto adicionamos Getters.
    public Estado getEstadoSucessor() {
        return estadoSucessor;
    }

    public Accao getAccao() {
        return accao;
    }
}

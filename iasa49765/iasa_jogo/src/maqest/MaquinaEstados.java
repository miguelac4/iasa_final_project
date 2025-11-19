package maqest;

import agente.Accao;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;

/*
Um sistema computacional refere-se aos seus estados e da forma como estes evoluem ao longo do tempo.

Máquinas de Estados servem para representar a evolução dos sistemas de forma mais precisa. Na
maquina de estados encontramos sempre um estado atual e varias transições para outros estados.

Dois tipos principais de maquinas de estados:
	- Máquinas de Mealy: a função de saída depende das entradas.
	- Máquinas de Moore: a função de saída não depende das entradas

Diagrama de Atividade:
	Retangulos com cantos redondos representam acções (ex: x=0).
	Losangulos representam decisões (ex: x > 0).

 */

public class MaquinaEstados {

    private Estado estado;

    public MaquinaEstados(Estado estadoInicial) {
        this.estado = estadoInicial;
    }

    //
    public Accao processar(Evento evento){
        //Sob o dicionario de transições pedir ao estado atual qual é a transição associada
        // ao evento
        Accao accao = null; //por omissão assumir accao null
        Transicao transicao = estado.processar(evento);

        //se a transicao não for null atualiza o estado e retorna a ação associada
        if (transicao != null) {
            estado = transicao.getEstadoSucessor(); //atualizar estado
            accao = transicao.getAccao();

        }
        return accao; //retornar accao

    }

    public Estado getEstado() {
        return estado;
    }
}

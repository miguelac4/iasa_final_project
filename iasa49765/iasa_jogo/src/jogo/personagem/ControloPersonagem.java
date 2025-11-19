package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;
import maqest.Transicao;

/**
 * Classe que controla a jogo.personagem.
 * Executa a decisão com base nas perceções recebidas do ambiente.
 * Criar uma maquina de estados.
 */
public class ControloPersonagem implements Controlo {

    private MaquinaEstados maqEst;

    public ControloPersonagem(){
        //Definir os Estados
        /**
         * Estados representam os diferentes modos ou condições internas da personagem durante o
         * jogo, estes tem um nome descritivo que reflete a atividade ou comportamento principal
         * da personagem enquanto está nesse estado.
         */
        Estado procura = new Estado("Procura");
        Estado inspecao = new Estado("Inspeção");
        Estado observacao = new Estado("Observação");
        Estado registo = new Estado("Registo");

        //Definir as ações
        /**
         * Ações são comportamentos especificos que a personagem pode realizar em resposta a
         * eventos no ambiente dojogo, cada ação é associada a um comando do jogo especifico.
         */
        Accao procurar = new Accao(ComandoJogo.PROCURAR);
        Accao aproximar = new Accao(ComandoJogo.APROXIMAR);
        Accao observar = new Accao(ComandoJogo.OBSERVAR);
        Accao fotografar = new Accao(ComandoJogo.FOTOGRAFAR);

        //Definir as transições
        /**
         * As transições definem as mudanças de estado que ocorrem em resposta a eventos
         * especificos no ambiente do jogo, estas são definidas de maneira a refletir o
         * comportamento desejado da personagem em diferentes situações no jogo, premitindo-lhe
         * adaptar-se dinamicamente ao ambiente e aos eventos que ocorrem.
         */
        procura
                .transicao(EventoJogo.ANIMAL, observacao, aproximar)
                .transicao(EventoJogo.RUIDO, inspecao, aproximar)
                .transicao(EventoJogo.SILENCIO, procura, procurar);


        inspecao
                .transicao(EventoJogo.SILENCIO, procura)
                .transicao(EventoJogo.ANIMAL, observacao, aproximar)
                .transicao(EventoJogo.RUIDO, inspecao, procurar);
        observacao
                .transicao(EventoJogo.ANIMAL, registo, observar)
                .transicao(EventoJogo.FUGA, inspecao);
        registo
                .transicao(EventoJogo.ANIMAL, registo, fotografar)
                .transicao(EventoJogo.FUGA, procura)
                .transicao(EventoJogo.FOTOGRAFIA, procura);

        //Inicializar o atributo maquina de estados com o estado inicial procura
        maqEst = new MaquinaEstados(procura);

    }

    //Sobre a maquina de estados do controle da personagem vamos processar o evento, esse
    // processar irá retornar uma acção.
    public Accao processar(Percepcao percepcao){
        Evento evento = percepcao.getEvento();
        Accao accao = maqEst.processar(evento);
        mostrar();
        return accao;
    }

    public void mostrar() {
        System.out.println("Estado: " + getEstado().getNome());
    }

    public Estado getEstado() {
        return maqEst.getEstado(); //retorna estado da maquina de estados
    }
}

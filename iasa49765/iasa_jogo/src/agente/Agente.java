package agente;

/**
 *
 *  Engenharia de Software:
 *      - Aplica abstração para definir um comportamento comum para diferentes tipos de agentes.
 *      - Segue o princípio de responsabilidade única (SRP) separando percepção, decisão e ação.
 *
 *  Representa um agente inteligente que interage com o ambiente.
 *
 *  O agente segue o ciclo percepção-processamento-ação.
 *  Ele pode ser baseado em diferentes paradigmas de IA:
 *      - Simbólico: Modelado por regras e lógica formal.
 *      - Conexionista: Baseado em redes neurais.
 *      - Comportamental: Responde a estímulos do ambiente.
 */

import ambiente.Ambiente;
import ambiente.Evento;


public class Agente {
    //Aqui representamos dois atributos

    //No primeiro atributo "ambiente" o agente está inserido para que possa interagir com o ambiente
    private Ambiente ambiente;
    //No segundo atributo "controlo" encontramos o mecanisco do agente
    private Controlo controlo;

    //Neste construtor inicializamos um objeto Agente com um certo ambiente e controle
    public Agente(Ambiente ambiente, Controlo controlo){
        this.ambiente = ambiente;
        this.controlo = controlo;
    }


    //
    public void executar(){
        //evocar metodo percecionar e instacia uma percepcao
        Percepcao percepcao = percepcionar();
        //gera se um objeto que é uma acção a partit da precepcao e retorna uma accao
        // (ação utilizada na atividade processar do controlo)
        Accao accao = controlo.processar(percepcao);
        //actua a accao
        actuar(accao);

    }

    protected Percepcao percepcionar(){
        //obter um evento observando um ambiente
        Evento evento = ambiente.observar();
        //criar uma percepcao com esse evento (com o construtor)
        return new Percepcao(evento);

    }

    protected void actuar(Accao accao){
        //se a acao for diferente de null entao executa o comando dessa acção sobre o ambiente
        if(accao != null){
            //com o metodo getComando da accao
            ambiente.executar(accao.getComando());
        }
    }
}

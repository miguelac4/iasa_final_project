package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

/**
 * Os agentes inteligentes são entidades virtuais que possuem a capacidade de interagir de forma autonoma.
 * Esses agentes são como sensores para perceber o ambiente e atuadores para realizar ações com o objetivo de alcançar
 * metas especificas.
 * Os sistemas autonomos inteligentes constituem um subconjunto dos agentes inteligentes, caracterizados por sua capacidade
 * de operar de forma independente e adptativa em ambientes dinamicos e complexos. Eles são capazes de tomar decisoes sem
 * intervenção humana direta, ajustando o seu comportamento de acordo com as condições do ambiente.
 *  A representação do ambiente é um elemento crucial na realizacao de sistemas baseados em agentes inteligentes.
 *  Consiste na criação de modelos computacionais que capturam as caracteristicas essenciais do ambiente no qual o agente está inserido.
 *  sso envolve a identificacao de estados possiveis, acoes disponiveis e as transicoes entre estados causadas pelas açoes do agente.
 *
 * Modelos de Comportamento
 * 	Dois modelos importantes na perspectiva da modelação:
 * 		Interacção: É representado por um diagram de sequencia, esse diagrama é representado a 2 dimensões (horizontal=tempo,  vertical=instancias).
 *
 * 		Dinâmica: É representado pelos estados que um sistema pode assumir e a forma como eles evoluem ao longo do tempo, determinando o comportamento do sistema
 *
 * Jogo (Safari Fotografico)
 *
 * 	O jogo consiste num ambiente onde a jogo.personagem tem por objectivo registar a presença de animais através de fotografias.
 *
 * 	Estados da Personagem:
 * 		PROCURAR (inicial)
 * 		APROXIMAR (se ouvir ruído)
 * 		OBSERVAR (se encontrar um animal)
 * 		FOTOGRAFAR (se o animal continuar presente)
 *
 * 	Eventos que afetam os Estados:
 * 		SILÊNCIO: Retorna à procura
 * 		RUÍDO: Muda para inspeção
 * 		ANIMAL: Muda para observação
 * 		FUGA: Retorna a procura ou inspeção
 * 		FOTOGRAFIA: Retorna a procura
 *
 * Modelo Reactivo (Ligação entre sensores e atuadores)
 * 	Percepção - Agregado de estimulos (observa a informação do ambiente, uma unica percepção pode ativar várias
 * 	respostas)
 * 	Respostas - Incluem a ação (pode haver mais informações como prioridade da ação)
 *
 * 	 * Main Classe do jogo.
 *  * Responsável por inicializar o ambiente e a jogo.personagem e executa a lógica do jogo
 */
public class Jogo {

    private static AmbienteJogo ambiente;
    private static Personagem personagem;

    //Neste construtor criamos um ambiente e jogo.personagem associada ao mesmo
    public Jogo(){
        this.ambiente = new AmbienteJogo();
        this.personagem = new Personagem(ambiente);
    }

    //Instancia o jogo e chama o método executar
    public static void main(String[] args) {
        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);
        executar();
    }

    //Usamos um Do While pois queremos uma verificação do getEvento() depois de executar os métodos para não dar null.

    private static void executar(){
        do{
            ambiente.evoluir();
            personagem.executar();
        }while(ambiente.getEvento() != EventoJogo.TERMINAR);
    }
}

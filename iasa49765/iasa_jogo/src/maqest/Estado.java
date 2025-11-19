package maqest;

import agente.Accao;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;

/*
Estado é toda a informação que determina a configuração atual de um sistema computacional num dado
momento.

Estados e transições são definidos matematicamente:
	- O estado de um sistema pode ser representado por um conjunto de possíveis configurações (Q).
	- A função de transformação de estado (δ) define como o sistema muda de estado baseado em entradas.
	- A função de saída (λ) define qual a saída do sistema para um determinado estado e entrada.

Dinamica da Personagem:
	A personagem tem um conjunto de estados e ações que mudam conforme os eventos do ambiente, dependendo do que acontece no jogo, a personagem altera o seu estado e executa um ação correspondente.

Estados da Personagem:
	Procura: Estado inicial, onde a personagem está à procura de animais.
	Inspeção: Se ouvir um ruído, a personagem aproxima-se para investigar.
	Observação: Se encontrar um animal, entra neste estado e começa a analisar o ambiente.
	Registo: Se o animal permanece, a personagem tira uma fotografia.

Função de Saida:
	Cada estado está associado a uma ação, que é a resposta da personagem ao evento.

 */

public class Estado {

    public String nome;
    private Map<Evento, Transicao> transicoes;

    public Estado(String nome){
        this.nome = nome;
        this.transicoes = new HashMap<Evento, Transicao>();
    }

    public Transicao processar(Evento evento){
        //so fazer return transicoes.getEvento
        return transicoes.get(evento);
    }

    public Estado transicao(Evento evento, Estado estadoSucessor){
        //dicionario transicoes, fazer put em que a chave é o evento e o valor é uma nova
        // transisao em que o estado sucessor é o estado sucessor e accao null
        transicoes.put(evento, new Transicao(estadoSucessor, null));
        return this;

    }

    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao){
        //igual ao primeiro transicao, mas em vez de passar o segundo parametro = null passa a propria
        // accao recebida
        transicoes.put(evento, new Transicao(estadoSucessor, accao));
        return this;
    }

    public String getNome(){ //O atributo nome é para ser implementado como se estivesse no UML (readOnly)
        return nome;
    }
}

package jogo.ambiente;

import ambiente.Evento;

//enum em Java serve para criar um enumerarado de diferentes eventos que podem decorer no ambiente do jogo
public enum EventoJogo implements Evento {
    SILENCIO,
    RUIDO,
    ANIMAL,
    FUGA,
    FOTOGRAFIA,
    TERMINAR;

    //este método serve para mostrar na consola o nome do evento que está a decorrer no atual momento
    public void mostrar(){
        System.out.println("Evento: " + this); //"this" chama implicitamente o método toString() da enumeração
    }
}

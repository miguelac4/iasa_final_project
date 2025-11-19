package jogo.ambiente;

//enum em Java serve para criar um enumerarado de diferentes comandos que o agente pode executar no ambiente do jogo
public enum ComandoJogo implements ambiente.Comando{ //No diagrama UML temos que a classe herda Comando
    PROCURAR,
    APROXIMAR,
    OBSERVAR,
    FOTOGRAFAR;

    //este médodo serve para mostrar na consola o nome do comando
    public void mostrar() {
        System.out.println("Comando: " + this); //"this" chama implicitamente o mdtodo toString()
        // da enumeração
    }
}

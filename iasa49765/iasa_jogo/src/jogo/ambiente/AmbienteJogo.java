package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 *  Nesta classe "AmbienteJogo" encontramos a Representação do Ambiente, são definidos estados possiveis do ambiente e as açoes
 *  que o agente pode executar. Este "Ambiente" irá enviar um evento e receber um comando do agente.
 *
 *  this é usado dentro de um metodo ou construtor para referenciar o próprio objeto atual da classe.
 *
 *  O sublinhado por baixo de um nome de uma classe na linguagem UML significa o nome da instancia.
 *
 *  Desacoplamento: O código que utiliza a interface não precisa conhecer as implementações concretas, facilitando a substituição e evolução das classes, quando se usam interfaces fica-se independente das implementações concretas.
 *
 *  Métricas de arquitetura (Indicam a qualidade da arquitetura de software)
 *
 * 	    Acoplamento: Grau de interdependência entre partes de um sistema
 *
 * 	    Coesão: Nível coerência funcional de um subsistema/módulo (até que ponto esse módulo realiza uma única função)
 * 		Um modulo é coeso se todas as partes internas significam uma responsabilidade desse modulo.
 *
 * 	    Simplicidade: Nível de facilidade de compreensão/comunicação da arquitectura.
 *
 * 	    Adaptabilidade: Nível de facilidade de alteração da arquitectura para incorporação de novos requisitos ou de alterações nos requisitos previamente definidos (alterações em uma implementação não afetam o código que usa a interface, desde que o contrato permaneça o mesmo).
 *
 *  Processo de Desenvolvimento de Software (como por exemplo nesta classe começou-se por impplementar só o codigo estrutural,
 *  isto para filtrar erros de estrotura e erros de desenvolvimento e assim resolver todos esses primeiro):
 *
 * 	    1º Código Estrutural
 * 	    2º Código Comportamental (este necessita do código estrutural para reduzir o número de erros)
 *
 * 	    Para reduzir erros de métodos não Void que ainda não foram implementados podemos adicionar "throw new RuntimeException();",
 * 	     assim conseguimos analizar outros erros mais importantes para serem encontrados.
 *
 *  Este vai pedir teclas ao utilizador para simular eventos como:
 * 	    SILENCIO,
 *      RUIDO,
 *      ANIMAL,
 *      FUGA,
 *      FOTOGRAFIA,
 *      TERMINAR;
 */

public class AmbienteJogo implements Ambiente {

    private EventoJogo evento; //atributo privado mas com getter para só poder ser lido
    Map<String, EventoJogo> eventos;

    public AmbienteJogo(){

        //Aqui criamos um dicionário "Map" para conseguir mapear cada letra (string) a um determinado evento (EventoJogo)
        eventos = new HashMap<String, EventoJogo>();
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("o", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);
    }
//Métodos como evoluir e observar são responsaveis por atualizar o estado do ambiente e permitir que o agente observe o estado atual.
    //Quando pedimos ao evento para evoluir vai ser gerado um novo evento, esse evento vai ficar no atributo privado evento,
    // (read-only é uma propriedade so de leitura e nao de escrita implementada com um getter) Evoluir  irá então atualizar
    // o atributo evento com o método gerarEvento.
    public void evoluir(){
        this.evento = gerarEvento();
    }

    //Se existir evento ja atribuido (se nao for null) mostra o evento no ecra
    public Evento observar(){
        if(this.evento != null){
            this.evento.mostrar();
        }
        return this.evento;
    }

    //Mostra o comando no ecra
    public void executar (Comando comando){
        if (comando != null) {
            System.out.print("Comando: ");
            comando.mostrar();
        } else {
            System.out.println("Nenhum comando recebido");
        }
    }

    private EventoJogo gerarEvento(){ //pedir uma tecla ao utilizador e gerar o evento dependendo da tecla que o utilizador digita
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um evento: (s)SILENCIO, (r)RUIDO, (a)ANIMAL, (f)FUGA, (o)FOTOGRAFIA, (t)TERMINAR:");
        String codigoEvento = scanner.next();

        return eventos.get(codigoEvento);
    }

    public EventoJogo getEvento(){  //read only (função para ler "evento" noutras classes e não permitir alteraraçoes)
        return evento;
    }
}

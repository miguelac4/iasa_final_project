package ambiente;

/**
 *  Engenharia de Software:
 *      - Baseado no conceito de eventos e assincronismo.
 *      - Segue o princípio da modularização, separando eventos do restante do código.
 *
 *  Representa um evento detectado no ambiente.
 *  Eventos podem ser mudanças ambientais ou informações relevantes
 *  para a tomada de decisão do agente.
 */

public interface Evento {

    void mostrar();
}

//pequena nota: interfaces me Java já assumem que os seus métodos são public e abstract

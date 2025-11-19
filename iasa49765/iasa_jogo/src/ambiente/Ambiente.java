//Define o ambiente do jogo
package ambiente;

/**
 *  Engenharia de Software:
 *      - Segue o princípio de abstração para modelar o ambiente.
 *      - Implementação modular permite reutilização e manutenção facilitada
 *
 *  Um ambiente pode ser:
 *      - Observável ou parcialmente observável
 *      - Determinístico ou estocástico
 *      - Estático ou dinâmico
 */

public interface Ambiente {

    void evoluir();

    Evento observar();

    void executar(Comando comando);

}

/**
Nota sobre interfaces: interface é um contrato que garante certa funcionalidade num certo sitio. Desta forma
 simplificamos a complexidade do codigo.

 */

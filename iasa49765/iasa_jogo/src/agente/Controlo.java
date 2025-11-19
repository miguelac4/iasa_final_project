package agente;

/**
 *  Engenharia de Software:
 *      - Usa encapsulamento para definir comandos genéricos.
 *      - Permite a extensão do sistema sem modificar código existente.
 *
 * Interface responsável pelo controle do agente.
 * O controle pode ser baseado em máquinas de estados ou em sistemas mais sofisticados de decisão.
 *
 * Nesta classe "Controlo" processamos percepções e retornamos ações, com objetivo de implementarmos diferentes
 * estrategias de controle para o agente.
 */

public interface Controlo {

    Accao processar(Percepcao percepcao);

}

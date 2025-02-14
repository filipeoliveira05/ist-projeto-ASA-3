from pulp import LpMaximize, LpProblem, LpVariable, lpSum, GLPK
import sys


def solve_toy_distribution(n, m, t, factories, countries, requests):
    # Criar o modelo de otimização
    model = LpProblem(name="toy-distribution", sense=LpMaximize)

    # Variáveis de decisão: x[k, i] é 1 se um brinquedo for entregue à criança k da fábrica i
    x = {
        (k, i): LpVariable(name=f"x_{k}_{i}", cat="Binary")
        for k, (p_k, factories_k) in requests.items()
        for i in factories_k
    }

    # Objetivo: Maximizar o número de crianças atendidas
    model += lpSum(x[k, i] for k, (p_k, factories_k) in requests.items() for i in factories_k)

    # Restrições: Cada criança recebe no máximo um brinquedo
    for k, (p_k, factories_k) in requests.items():
        model += lpSum(x[k, i] for i in factories_k) <= 1

    # Restrições de estoque das fábricas
    for i, (p_j, f_maxi) in factories.items():
        model += lpSum(
            x[k, i]
            for k, (p_k, factories_k) in requests.items()
            if i in factories_k
        ) <= f_maxi

    # Restrições de distribuição para os países
    for j, (p_maxj, p_minj) in countries.items():
        # Restrições mínimas
        children_in_country = sum(1 for k, (p_k, _) in requests.items() if p_k == j)
        export_min = min(p_minj, children_in_country)  # Ajuste para considerar o número de crianças
        model += lpSum(
            x[k, i]
            for k, (p_k, factories_k) in requests.items()
            for i in factories_k
            if p_k == j
        ) >= export_min

        # Restrições máximas
        model += lpSum(
            x[k, i]
            for k, (p_k, factories_k) in requests.items()
            for i in factories_k
            if factories[i][0] == j and j != p_k
        ) <= p_maxj

    # Resolver o modelo com limite de tempo
    model.solve(GLPK(msg=0))

    # Verificar a solução
    if model.status == 1:  # Solução ótima
        return int(model.objective.value())
    else:
        return -1


def main():
    # Obter todo o input
    input_data = sys.stdin.read().splitlines()

    # Ler número de fábricas, países e crianças
    n, m, t = map(int, input_data[0].split())

    # Ler fábricas
    factories = {}
    for i in range(1, n + 1):
        f_i, p_j, f_maxi = map(int, input_data[i].split())
        if f_maxi > 0:  # Apenas considerar fábricas com estoque > 0
            factories[f_i] = (p_j, f_maxi)

    # Ler países
    countries = {}
    for i in range(n + 1, n + m + 1):
        p_j, p_maxj, p_minj = map(int, input_data[i].split())
        countries[p_j] = (p_maxj, p_minj)

    # Ler pedidos das crianças
    requests = {}
    for i in range(n + m + 1, n + m + t + 1):
        parts = list(map(int, input_data[i].split()))
        c_k, p_k, factories_k = parts[0], parts[1], parts[2:]
        valid_factories = [f for f in factories_k if f in factories]
        if len(valid_factories) > 0:  # Apenas considerar pedidos válidos
            requests[c_k] = (p_k, valid_factories)

    # Resolver o problema
    result = solve_toy_distribution(n, m, t, factories, countries, requests)
    print(result)


if __name__ == "__main__":
    main()
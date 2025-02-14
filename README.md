# ASA 24/25 - Projeto 3
**Filipe Oliveira**  
**Número de estudante**: ist1110633

## 📌 Descrição do Projeto  

O projeto consiste na resolução de um problema de **programação linear** com recurso à biblioteca **PuLP**. A descrição do problema é a seguinte:  

O **Professor Natalino Caracol** foi contratado pela empresa do **Pai Natal**, a **UbiquityInc**, para desenvolver um programa que otimize a **distribuição de brinquedos** pelas crianças ao redor do mundo.  

A empresa segue uma **estratégia descentralizada**, onde:  
- Existem `n` **fábricas**, cada uma produzindo **apenas um tipo de brinquedo**.  
- As fábricas estão distribuídas por `m` **países**, cada um com **limites de exportação e quotas mínimas de entrega**.  
- Existem `t` **crianças**, cada uma fazendo **um pedido de brinquedos**, podendo indicar múltiplas fábricas como fontes possíveis.  

O objetivo do projeto é **maximizar o número de crianças que recebem pelo menos um brinquedo**, respeitando todas as **restrições comerciais e de stock**.  

---

## 🎯 Definição do Problema  

A distribuição dos brinquedos precisa obedecer às seguintes **restrições**:  
- **Cada fábrica** tem um **stock máximo** de brinquedos que pode produzir.  
- **Cada país** tem um **mínimo e um máximo** de brinquedos que pode importar/exportar.  
- **Cada criança** pode receber no máximo **um brinquedo**, escolhido entre os disponíveis na sua lista de pedidos.  

### 📌 **Entrada**  
O programa recebe um ficheiro de entrada contendo:  
1. **Uma linha com três inteiros**:  
   - `n` → Número total de fábricas.  
   - `m` → Número total de países.  
   - `t` → Número total de crianças.  
2. **Uma lista de `n` linhas**, onde cada linha contém:  
   - `i` → Identificador da fábrica (`1 ≤ i ≤ n`).  
   - `j` → Identificador do país (`1 ≤ j ≤ m`) onde a fábrica está localizada.  
   - `f_max` → Stock máximo de brinquedos dessa fábrica.  
3. **Uma lista de `m` linhas**, onde cada linha contém:  
   - `j` → Identificador do país (`1 ≤ j ≤ m`).  
   - `p_max` → Limite máximo de exportação do país.  
   - `p_min` → Número mínimo de brinquedos a serem distribuídos nesse país.  
4. **Uma lista de `t` linhas**, onde cada linha contém:  
   - `k` → Identificador da criança (`1 ≤ k ≤ t`).  
   - `j` → País onde a criança vive (`1 ≤ j ≤ m`).  
   - **Lista de fábricas** onde o brinquedo desejado é produzido.  

Os números em cada linha são separados por espaços e **não há caracteres adicionais** além do fim de linha.  

### 📌 **Saída**  
O programa imprime **um único número inteiro**:  
- **Se for possível satisfazer todas as restrições**, imprime **o número máximo de crianças** que podem receber um brinquedo.  
- **Se não for possível distribuir brinquedos respeitando todas as restrições**, imprime **`-1`**.  

---

## 📄 Relatório  

O ficheiro [relatorio-ASA2425P3.pdf](./relatorio-ASA2425P3.pdf) contém informações detalhadas sobre este projeto, incluindo:  
- **Descrição do problema e da solução**: formalização do modelo linear (variáveis do problema, restrições do problema, função objetivo)  
- **Análise teórica**: complexidade da codificação em função dos parâmetros do problema 
- **Avaliação experimental dos resultados**: gráfico do tempo em função dos parâmetros do problema  

---

📄 **Nota:** Para mais exemplos e explicações detalhadas, consultar [enunciado-ASA2425P3.pdf](./enunciado-ASA2425P3.pdf)

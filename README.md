# Trabalho Prático 2 - TPPE 23.2

Aluno: Victor Eduardo Araújo Ribeiro - 190038926

## Descrição
As características de um bom projeto de software apresentadas estão, de certo modo, associadas aos maus cheiros de código apresentados por Martin Fowler em seu catálogo de refatorações e relacionados às operações que tratam tais maus cheiros. De acordo com a definição do próprio Martin Fowler, refatoração é uma maneira de aperfeiçoar o projeto de código existente sem alterar o seu comportamento externamente observável.

Para esse trabalho o grupo deverá escolher 5 características dentre as 9 características de um bom projeto de software apresentadas acima e, para cada uma delas, apresentar:

- Uma descrição da característica, mostrando claramente quais são os seus efeitos no código (em termo de estrutura, claridade, coesão, acoplamento dentre outros efeitos aplicáveis);
- Uma relação da característica com os maus cheiros de código definidos por Fowler. Uma descrição dos maus cheiros está disponível nos slides sobre o conteúdo de refatoração;
- Pelo menos uma operação de refatoração capaz de levar o projeto de código a ter a característica em análise.

## Características exploradas:

### 1. Simplicidade

A simplicidade de código refere-se à qualidade do código que facilita a compreensão, manutenção e evolução do software. Um código simples é direto, claro, conciso e não possui complexidades desnecessárias. É fácil para os desenvolvedores entenderem o que está acontecendo e realizar alterações sem introduzir erros.

#### Efeitos no código:

- **Legibilidade**: Códigos simples são mais legíveis, facilitando a compreensão do seu funcionamento.
- **Manutenibilidade**: A simplicidade facilita a manutenção do código, pois alterações e correções podem ser feitas de forma mais rápida e segura.
- **Redução de Bugs**: Códigos simples têm menos chances de conter erros, uma vez que a complexidade desnecessária é eliminada.
- **Facilidade de Evolução**: A simplicidade permite que o código seja mais adaptável a mudanças, facilitando a adição de novos recursos ou a modificação de funcionalidades existentes.

#### Relação com os mau cheiros de Fowler:

- **Duplicação de Código**: Códigos complexos frequentemente envolvem duplicações. A simplicidade busca eliminar redundâncias e promover a reutilização de código.
- **Método Longo**: Métodos longos geralmente indicam complexidade e dificultam a compreensão. A simplicidade incentiva a decomposição de métodos em partes menores e mais específicas.
- **Switches Longos**: Estruturas de controle extensas, como switch ou case, são indicadores de complexidade. A simplicidade sugere o uso de abordagens mais flexíveis, como mapas ou polimorfismo.
- **Dependência Cíclica**: A dependência cíclica entre classes cria complexidade. A simplicidade encoraja a quebrar essas dependências, utilizando injeção de dependência ou estratégias similares.

#### Como alcançar por meio da refatoração de código:

- **Identificação de Mau Cheiros**: Utilize as características de mau cheiro, como duplicação, métodos longos, etc., como indicadores de complexidade.
- **Decomposição de Métodos**: Quebre métodos longos em funções menores e mais específicas para tornar o código mais legível e modular.
- **Eliminação de Duplicação**: Procure por duplicações de código e crie funções ou classes reutilizáveis para promover simplicidade.
- **Redução de Dependências Cíclicas**: Refatore classes para eliminar dependências cíclicas, utilizando injeção de dependência ou reorganizando a estrutura do código.
- **Abstração Adequada**: Utilize abstrações apropriadas, como funções, classes e interfaces, para encapsular a complexidade e tornar o código mais simples e compreensível.

### 2. Elegância

Elegância de código refere-se à qualidade estética, simplicidade e eficiência na implementação de soluções. Um código elegante é aquele que, além de cumprir sua função, é expressivo, conciso e utiliza padrões que facilitam a leitura e compreensão do desenvolvedor. Elegância está relacionada à beleza e eficácia na expressão das soluções no código fonte.

#### Efeitos no código:

- **Legibilidade Aprimorada**: Códigos elegantes são mais fáceis de serem lidos e compreendidos, facilitando a colaboração entre os membros da equipe.
- **Manutenção Simplificada**: A elegância muitas vezes está associada a uma estrutura modular e organizada, tornando a manutenção mais direta e menos propensa a erros.
- **Expressividade e Clareza**: Códigos elegantes expressam ideias de forma clara e concisa, tornando a intenção do código evidente.
- **Eficiência e Performance**: Um código elegante pode, muitas vezes, ser mais eficiente, uma vez que evita abordagens desnecessariamente complexas.

#### Relação com os mau cheiros de Fowler:

- **Duplicação de Código**: A duplicação de código muitas vezes torna o código menos elegante. Remover duplicações pode melhorar a elegância.
- **Método Longo**: Métodos longos podem prejudicar a elegância do código, pois dificultam a compreensão. A elegância favorece a decomposição de métodos em partes mais simples e específicas.
- **Switches Longos**: Estruturas de controle extensas podem comprometer a elegância. Alternativas mais elegantes, como polimorfismo, podem ser consideradas.
- **Dependência Cíclica**: Dependências cíclicas entre classes geralmente indicam um design menos elegante. A reorganização para reduzir a complexidade pode aumentar a elegância.

#### Como alcançar por meio da refatoração de código:

- **Simplificação de Estruturas**: Simplificar estruturas complexas, como loops aninhados e estruturas condicionais longas, pode melhorar a elegância do código.
- **Refatoração de Nomes**: Escolher nomes descritivos e significativos para variáveis, funções e classes pode aumentar a elegância e a compreensibilidade do código.
- **Abstração Adequada**: Utilizar abstrações apropriadas, como funções, classes e interfaces, pode tornar o código mais elegante ao encapsular detalhes complexos.
- **Remoção de Duplicação**: Identificar e remover duplicações de código pode simplificar o código e aumentar a elegância, promovendo a reutilização e a consistência.

### 3. Modularidade

A modularidade refere-se à prática de dividir um sistema de software em partes independentes e autônomas chamadas módulos. Cada módulo realiza uma função específica e pode ser desenvolvido, testado, mantido e reutilizado de maneira independente. A modularidade promove a separação de responsabilidades, facilitando a compreensão, manutenção e expansão do código.

#### Efeitos no código:

- **Facilidade de Manutenção**: Módulos independentes são mais fáceis de serem mantidos, uma vez que as alterações em um módulo não devem afetar outros, desde que a interface seja preservada.
- **Reutilização de Código**: Módulos bem definidos podem ser reutilizados em diferentes partes do sistema ou em projetos futuros, economizando tempo e esforço.
- **Testabilidade Aprimorada**: Módulos isolados são mais fáceis de serem testados, pois as dependências são claras e podem ser substituídas por mocks ou simulações durante os testes.
- **Escalabilidade**: A modularidade facilita a escalabilidade do sistema, permitindo que novos módulos sejam adicionados sem afetar negativamente os existentes.

#### Relação com os mau cheiros de Fowler:

- **Duplicação de Código**: A modularidade ajuda a reduzir a duplicação, uma vez que módulos reutilizáveis podem ser compartilhados entre diferentes partes do código.
- **Método Longo**: Métodos longos podem ser decompostos em módulos menores e mais específicos para promover a modularidade.
- **Switches Longos**: Estruturas de controle extensas podem ser substituídas por chamadas de módulos específicos, melhorando a modularidade.
- **Dependência Cíclica**: A modularidade ajuda a reduzir dependências cíclicas, pois módulos bem definidos têm interfaces claras e podem ser independentes.

#### Como alcançar por meio da refatoração de código:

- **Identificação de Responsabilidades**: Analise o código para identificar responsabilidades distintas e agrupe-os em módulos independentes.
- **Encapsulamento Adequado**: Utilize técnicas de encapsulamento para esconder detalhes de implementação e expor apenas interfaces necessárias.
- **Divisão de Métodos e Funções**: Ao encontrar métodos ou funções muito extensos, divida-os em módulos menores e mais específicos.
- **Organização de Diretórios e Pacotes**: Mantenha uma estrutura de diretórios e pacotes bem organizada para refletir a modularidade do código. Isso facilita a navegação e compreensão do sistema.

### 4. Boas Interfaces

Uma boa interface em código refere-se à definição clara e eficaz de como os componentes de software interagem entre si. Isso inclui a especificação de métodos, parâmetros e comportamentos, facilitando o uso correto e intuitivo de uma classe ou módulo por outros componentes do sistema.

#### Efeitos no Código:

- **Facilidade de Uso**: Uma boa interface torna fácil para outros desenvolvedores entenderem como usar uma classe ou módulo, reduzindo a probabilidade de erros.
- **Manutenção Simples**: Interfaces bem projetadas facilitam a manutenção, pois mudanças internas em uma classe podem ser feitas sem afetar os clientes que usam a interface.
- **Reutilização Facilitada**: Interfaces claras e intuitivas encorajam a reutilização de componentes em diferentes partes do sistema ou até mesmo em projetos distintos.
- **Testabilidade Aprimorada**: Interfaces definidas de maneira adequada simplificam a criação de testes, pois os componentes podem ser isolados e testados de forma independente.

#### Relação com os mau cheiros de Fowler:

- **Duplicação de Código**: Boas interfaces podem reduzir a duplicação de código, pois promovem a reutilização de componentes sem a necessidade de duplicar implementações.
- **Método Longo**: Interfaces bem definidas podem evitar a criação de métodos longos, incentivando a decomposição em métodos menores e mais específicos.
- **Dependência Cíclica**: Interfaces claras ajudam a evitar dependências cíclicas, fornecendo uma visão clara de como os componentes interagem.
- **Switches Longos**: Interfaces bem projetadas podem substituir estruturas switch extensas, favorecendo o polimorfismo ou padrões de estratégia.

#### Como Alcançar por Meio da Refatoração de Código:

- **Simplicidade na Assinatura de Métodos**: Mantenha a assinatura dos métodos o mais simples e clara possível, fornecendo apenas os parâmetros necessários.
- **Encapsulamento Adequado**: Proteja os detalhes de implementação e exponha apenas o que é necessário por meio da interface.
- **Aprimoramento Incremental**: Refatore gradualmente, ajustando e melhorando a interface conforme necessário, em vez de tentar fazer grandes mudanças de uma vez.
- **Padrões de Design**: Utilize padrões de design, como interfaces, abstrações e injeção de dependência, para promover uma arquitetura mais modular e interfaces bem definidas.

### 5. Idiomático

Código idiomático refere e ao estilo de codificação que segue as práticas comuns e padrões aceitos dentro de uma linguagem de programação específica. É a maneira "natural" de escrever código em uma linguagem, levando em consideração as convenções e normas da comunidade de desenvolvedores.

#### Efeitos no Código:

- **Leitura Mais Fácil**: O código idiomático é mais fácil de ler e entender para outros desenvolvedores que estão familiarizados com as práticas da linguagem, melhorando a colaboração e a manutenção do código.
- **Prevenção de Armadilhas**: Ao seguir os padrões idiomáticos, é menos provável cair em armadilhas ou cometer erros que podem ocorrer ao desviar das convenções da linguagem.
- **Desempenho Aprimorado**: Em muitos casos, o código idiomático pode ser otimizado automaticamente pelo compilador ou interpretador, levando a um desempenho melhor.
- **Consistência**: O código idiomático promove consistência dentro do projeto e entre diferentes projetos, tornando o estilo de codificação mais uniforme.

#### Relação com os Mau Cheiros de Fowler:

- **Duplicação de Código**: Código idiomático frequentemente evita duplicações desnecessárias, pois segue padrões que promovem a reutilização.
- **Método Longo**: Padrões idiomáticos muitas vezes encorajam métodos e funções mais curtos e específicos, combatendo a tendência de criar métodos longos.
- **Switches Longos**: Em muitos casos, padrões idiomáticos favorecem o uso de construções que substituem switches longos, como polimorfismo ou estruturas de dados mais apropriadas.
- **Dependência Cíclica**: Código idiomático pode sugerir padrões de design que evitam dependências cíclicas, como injeção de dependência.

#### Como Alcançar por Meio da Refatoração de Código:

- **Estudo da Linguagem**: Familiarize e com as melhores práticas e padrões de codificação da linguagem que está sendo utilizada.
- **Revisão de Código**: Realize revisões de código regularmente para garantir que as práticas idiomáticas estejam sendo seguidas e para fornecer feedback aos membros da equipe.
- **Utilização de Ferramentas de Análise**: Utilize ferramentas de análise de código estático que podem identificar violações de padrões idiomáticos.
- **Refatoração Gradual**: Introduza mudanças graduais no código para seguir padrões idiomáticos. Isso pode ser feito à medida que novos recursos são adicionados ou durante a resolução de problemas existentes.

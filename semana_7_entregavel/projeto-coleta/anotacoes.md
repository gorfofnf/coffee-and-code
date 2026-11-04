Diferença entre página estática e montada por JavaScript



* Página estática: Em uma página estática, todos os dados estão incluídos diretamente no HTML, sendo assim possível ver os itens da lista ao apertar Ctrl+U para ver o código base da página.



* Página montada por JavaScript: Em uma página montada por JavaScript, ela é inicialmente vazia, sem os itens listados, mas após um momento, recebe dados para preenchê-la vindos de uma API. A diferença pode ser vista caso tente usar Ctrl+U, vendo que a lista está vazia e somente esperando os dados para adicionar itens.



==================================================================================



|Campo|Onde está|Seletor|Exemplo|O que pode faltar|
|-|-|-|-|-|
|id da vaga|atributo data-id do article|article.vaga|v003|Não|
|título|texto do link dentro do h2|h2.titulo a|Engenheiro(a) de Software Sênior|Não|
|empresa|texto do p|.empresa|Araucária Labs|Não|
|salário|texto do span|.salario|R$14.000 a <br />R$18.000|Sim|
|data|atributo datetime|time|2026-10-07|Não|
|tags|texto de cada li|ul.tags li|java, spring...|Sim|
|link do detalhe|atributo href|h2.titulo a|/vagas/v003|Não|
|local|texto do p|.local|Curitiba, PR|Não|
|nível|texto do span|.nivel|Sênior|Sim|
|requisitos|dentro de article.vaga-detalhe|ul.requisitos li|Experiência com Java, Experiência com spring...|Sim|



==================================================================================



User-Agent



* User-Agent: ColetatronMurais/1.0 (projeto de estudo; contato: pedrohg0505@gmail.com)



==================================================================================



Perguntas antes de coletar



1 - O site oferece uma API, um feed ou um arquivo de dados?

2 - Os termos de uso permitem a coleta autorizada?

3 - O robots.txt permite este caminho para o seu User-Agent?

4 - O robots.txt pede uma espera (Crawl-delay)?

5 - A página tem dados pessoais (nome, E-mail, telefone)?


# Movie

Código desenvolvido para para o Projeto Movie para o Curso de Web Full-Stack da Udacity.

## Visão geral do projeto

Esse projeto é um código server-side para armazenar uma lista de filmes sobre comida, incluindo cartazes e a URL de trailers.
A partir dessa lista, é gerada uma página web estática que permite aos visitantes assistir aos respectivos trailers.

### Pré-requisito

 - Biblioteca Python
 - Navegador

## Explicação dos arquivos

No arquivo media.py está a implementação da Classe Video e a Classe Movie(Herança de Video).

O arquivo entertainment_center.py estão cadastrados os Filmes (instância do objeto Movie), cadastrando o Título, Duração do Vídeo, Resumo da história, Imagem do Pôster e a URL do Trailer no Youtube.
No final do arquivo existe uma lista composta com todos as instâncias, e a partir da lista, é gerado o HTML.

Esse HTML é gerado no arquivo fresh_tomatoes.py, nem tem o código de HTML base usado para a geração da lista de filmes e depois abre a página gerada.


```
movies = [toast, chef, julieEJulia, burnt, jiro, ratatouille]
fresh_tomatoes.open_movies_page(movies)
```

## Autor

* **Fabio Rego** - *Trabalho inicial* - [fabiotavarespr](https://github.com/fabiotavarespr)

Veja a lista de pessoas que [contribuiram](https://github.com/fabiotavarespr/Movie/contributors) nesse projeto.
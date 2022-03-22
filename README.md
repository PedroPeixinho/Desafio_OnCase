# Desafio_OnCase

Para esse projeto, foi feito um scrapper que coleta informações de lojas que vendem jogos. Foi utilizado o frameword scrapy em python e o sistema operacional escolhido foi o linux.

Para rodar o código, basta acessar a pasta spiders dentro do projeto e executar o comando runspider, escolhendo o tipo de arquivo que serão guardadas as informações:
cd Desafio_Oncase/Desafio_Oncase/spiders
scrapy runspider CODIGO.py -o ARQUIVO.FORMATO_DO_ARQUIVO
Ex: scrapy runspider Amazon.py -o Amazon.json

Em relação aos jogos, o foco foi dados aos jogos de nintendo switch (console da Nintendo), já que os preços variam bastante entre as lojas, diferente dos jogos de outras empresas. Além disso, os sites escolhidos foram a Amazon, o Atacado dos Games e o Cogumelo shop, e fiz essas escolhas pois esses sites vendem os jogos citados e já conhecia eles. Os links para as abas direcionadas aos jogos citados nesses sites são:

https://www.amazon.com.br/b/?ie=UTF8&node=16253312011&pf_rd_p=839aede6-171f-4368-861e-8efcbb5db1b1&pf_rd_r=KMJX8AZSZ99GJ669GTTJ&pf_rd_s=br-videogames-flyout-content-3&pf_rd_t=SubnavFlyout&ref_=sn_gfs_co_nintendoswitchgeral_fo_16253312011_2
https://www.atacadodosjogos.com.br/c/nintendo/nintendo-switch/144528-SIT.html
https://www.cogumeloshop.com.br/jogos/nintendoswitch

Em relação ao código, ele foi feito utiizando o scrapy e coleta as informações de nome do jogo, preço, preço parcelado, avaliação e quantidade de avaliações. Esses atributos foram escolhidos pois são importantes na hora de comprar um jogo e seriam de grande influência ao escolher em qual site vale mais a pena comprar o jogo, comparando tais atributos (o site Cogumelo shop possuia pouquíssimas avaliações, então elas não foram coletadas).
Como seletores, utilizei tanto o xpath quanto o css, mais por questão de aprendizado, mas majoritariamente utilizei o css, pois achei mais simples de usar.

Foram criados os spiders utilizando a função scrapy genspider NOME_DA_SPIDER URL_DO_SITE, e foram coletados dados utilizando a função parse. Além disso, quando todos os dados de uma página eram coletados, a spider seguia para a página seguinte.
O site Atacado dos Jogos, em especial, só mostrava as avaliações e o número de avaliações dos jogos quando a página do jogo era aberta, assim foi necessário acessar a página de cada jogo no site utiizando a função follow, permitindo que fossem coletados todos os dados desejados. (O código demora bastante para terminar de executar por conta que a spider acessa cada página)

Além desses atributos, tentei calcular a média das avaliações e da quantidade de avaliações dos sites para usar como métrica, mas não consegui realizar essa implementação. Ela permitiria analisar o nível de satisfação e a popularidade dos sites escolhidos. A ideia que tive foi utilizar do arquivo pipelines.py para guardar tais atributos em uma lista, utilizando a função process_item, e ao final da execução da spider seria realizado o cálculo das médias, escrevendo-as em um arquivo de texto, porém não obtive sucesso.

Esse projeto permite a um consumidor comparar as ofertas das lojas de forma fácil e rápida, porém também pode ser utilizado de outras formas como por exemplo se outra loja quisesse comparar suas ofertas com as das outras. Além disso, o projeto pode ser escalado para coletar dados de produtos gerais, não somente jogos, e em muito mais sites, permitindo que essas comparações sejam feitas em escalas muito maiores.

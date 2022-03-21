import scrapy

from Desafio_Oncase.items import DesafioOncaseItem


class AmazonSpider(scrapy.Spider):
    name = 'Amazon'
    #allowed_domains = ['www.amazon.com.br']
    start_urls = ['https://www.amazon.com.br/b/?ie=UTF8&node=16253312011&pf_rd_p=839aede6-171f-4368-861e-8efcbb5db1b1&pf_rd_r=KMJX8AZSZ99GJ669GTTJ&pf_rd_s=br-videogames-flyout-content-3&pf_rd_t=SubnavFlyout&ref_=sn_gfs_co_nintendoswitchgeral_fo_16253312011_2']
    
    def parse(self, response):
        for jogos in response.css('.s-list-col-right > .sg-col-inner'):  #Coleta as informacoes dos jogos
            loja = "Amazon"
            nome = jogos.css('.a-size-medium.a-text-normal::text').get()
            #as coletas sao organizadas para ficar em um formato apropriado
            preco = jogos.css('.a-text-normal .a-price-whole::text').get() + ',' + jogos.css('.a-text-normal .a-price-fraction::text').get()     #preco = reais + ',' + centavos
            parcelamento = jogos.css('.a-color-base .a-size-base.a-color-secondary::text').get()[7:16] + jogos.css('.a-color-base .a-size-base.a-color-secondary::text').get()[-15:-10]    #formato de Yx de RSXX,XX
            avaliacao = jogos.css('.aok-align-bottom .a-icon-alt::text').get()[0:1] + '.' + jogos.css('.aok-align-bottom .a-icon-alt::text').get()[2:3]   #colocando '.' nas avaliacos (ao inves de ',' como esta no site)
            qnt_avaliacoes = jogos.css('.s-link-style .s-underline-text::text').get()
            qnt_avaliacoes = qnt_avaliacoes.replace(".", "")    #tirando o '.' que representa mil no site

            jogo = DesafioOncaseItem(loja=loja, nome=nome, preco=preco, parcelamento=parcelamento, avaliacao=avaliacao, qnt_avaliacoes=qnt_avaliacoes)
            yield jogo    #escreve no arquivo

        prox_pag = response.css('.s-pagination-next::attr(href)').get()    #pega o endereco da proxima pag

        if prox_pag is not None:   #se nao for nula chama a funcao parse na pagina
            yield scrapy.Request(response.urljoin(prox_pag), callback=self.parse)

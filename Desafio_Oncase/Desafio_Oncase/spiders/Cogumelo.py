import scrapy


class CogumeloSpider(scrapy.Spider):
    name = 'Cogumelo'
    #allowed_domains = ['www.cogumeloshop.com.br']
    start_urls = ['https://www.cogumeloshop.com.br/jogos/nintendoswitch']

    def parse(self, response):
        for jogos in response.xpath('*//div[@class="info-produto"]'):   #Coleta as informacoes dos jogos, escrevendo no arquivo
            yield{
                'loja': "CogumeloShop",
                'nome': jogos.xpath('.//span[@itemprop = "name"]/text()').get(),
                'preco': jogos.xpath('.//span[@id = "PrecoPrincipal1"]/text()').get(),
                'parcelamento': jogos.xpath('.//strong[@style="color:#cd0004;"]/text()')[0].get() + jogos.xpath('.//strong[@style="color:#cd0004;"]/text()')[1].get()  #formato Yx de RSXX,XX
                #praticamente nao ha avaliacoes nos sites entao nao foram coletadas
                #'avaliacao':
                #'qnt_avaliacoes':
            }

        prox_pag = response.xpath('*//span[@class = "page-next page-link"]/a/@href').get()  #pega o endereco da proxima pag

        if prox_pag is not None:  #se nao for nula chama a funcao parse na pagina
            yield scrapy.Request(response.urljoin(prox_pag), callback=self.parse)
    
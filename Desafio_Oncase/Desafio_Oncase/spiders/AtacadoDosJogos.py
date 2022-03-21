import scrapy

from Desafio_Oncase.items import DesafioOncaseItem

class AtacadodosjogosSpider(scrapy.Spider):
    name = 'AtacadoDosJogos'
    #allowed_domains = ['www.atacadodosjogos.com.br']
    start_urls = ['https://www.atacadodosjogos.com.br/c/nintendo/nintendo-switch/144528-SIT.html']

    def parse(self, response):
        for jogos in response.css('.coluna'):
            
            link = jogos.css('.labelproduto a::attr(href)').get()   #pega o link para acessar a pagina do jogo
            yield response.follow(link, self.parse_jogo)   #acessa a pagina do jogo

        prox_pag = response.css('.icon-seta-proximo::attr(href)').get()   #pega o endereco da proxima pag

        if prox_pag is not None:   #se nao for nula chama a funcao parse na pagina
            yield scrapy.Request(response.urljoin(prox_pag), callback=self.parse)

    def parse_jogo(self, response):    #Coleta as informacoes do jogo (na formatacao escolhida)
        loja = "Atacado dos Jogos"
        nome = response.css('.p_coluna_meio h1::text').get()
        preco = response.css('.p_preco_avista::text').get()
        parcelamento = response.css('.p_comjuros strong::text')[1].get()
        avaliacao = response.css('.p_resultado strong::text').get()[10:13]
        qnt_avaliacoes = response.css('.p_resultado small::text').get()[1:-12]
        
        jogo = DesafioOncaseItem(loja=loja, nome=nome, preco=preco, parcelamento=parcelamento, avaliacao=avaliacao, qnt_avaliacoes=qnt_avaliacoes)
        yield jogo   #Escreve no arquivo
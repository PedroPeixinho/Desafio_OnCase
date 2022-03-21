# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DesafioOncaseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #Define o formato dos atributos que queremos coletar
    loja = scrapy.Field()
    nome = scrapy.Field()
    preco = scrapy.Field()
    parcelamento = scrapy.Field()
    avaliacao = scrapy.Field()
    qnt_avaliacoes = scrapy.Field()
    pass

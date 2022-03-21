# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class DesafioOncasePipeline:

    loja = "Amazon"    #Variavel para saber de que loja sao as medias
    #listas para guardas as avaliacoes e a quantidade de avaliacoes
    avaliacoes = []
    n_avaliacoes = []
    #Variaveis para guardar a media que sera calculada
    media_avaliacoes = 0
    media_n_avaliacoes = 0

    def open_spider(self, spider):
        self.file = open('medias.txt', 'w')   #Abree o arquivo onde serao guardadas as medias

    def close_spider(self, spider):
        #Sao calculadas as medias comando os elementos das listas e dividindo pelo tamanho delas
        self.media_avaliacoes = sum(self.avaliacoes)/len(self.avaliacoes)
        self.media_n_avaliacoes = sum(self.n_avaliacoes)/len(self.n_avaliacoes)
        #Eh feita a escrita das medias no arquivo
        self.file.write("Media das avaliacoes de {self.loja} = {self.media_avaliacoes}\n")
        self.file.write("Media do numero de avaliacoes de {self.loja} = {self.media_n_avaliacoes}\n")
        self.file.close()

    def process_item(self, item, spider):
        #Quando uma avaliacao for coletada, ela sera transformada em float e guardada na lista avaliacoes
        self.avaliacoes.append(float(item['avaliacao']))
        if (item['qnt_avaliacoes'] != ""):   #se a qnt_avaliacoes nao for 0, ela sera transformada em inteiro e guardada na lista n_avaliacoes
            self.n_avaliacoes.append(int(item['qnt_avaliacoes']))
        if(item['loja'] == "Amazon"):  #Registra a loja que esta sendo acessada
            self.loja = "Amazon"
        if(item['loja'] == "Atacado dos Jogos"):
            self.loja = "Atacado dos Jogos"
        return item

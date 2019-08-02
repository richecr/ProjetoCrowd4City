# Scraping jpb
> Código tem como objetivo fazer web scraping nos vídeos do quadro, Calendário, do JPB. E depois fazer estudos sobre os textos, extraindo os problemas urbanos citados em cada vídeo e sua localidade.

## Fluxo de execução:

### scrape_links:

- Script que realiza o web scraping no site do [Calendário JPB](http://g1.globo.com/busca/?q=calendario+jpb&page=1&order=recent&species=v%C3%ADdeos).

- Captura as urls de uma quantidade específica de vídeos e salvando-as em um arquivo json, `links.json`.

### baixar_videos:

- Script que realiza o download dos áudios dos vídeos através dos links salvos no arquivo `links.json`. E converte todos os áudios para `wav`.

- Utiliza a lib `youtube_dl`.

- OBS: Mova os áudios para pasta `audios`. Por enquanto isso esta manual.

### speech_rec:

- Script que realiza a conversão/extração dos áudios para texto. E salvo todos os textos de cada áudio no arquivo `textos_videos.csv`.

- Utiliza a lib `speech_recognition`

### processa_texto:

- Script que realiza o processamento inteligente dos textos. Excluíndo palavras desnecessárias, como: Stop Words e etc.

- Utiliza a lib `Spacy`.


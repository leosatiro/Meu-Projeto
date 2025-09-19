#Como todos os testes qque executei foram localmente,deixei o comando do diretorio apenas para titulo de informação.

#setwd("C:/PROJETOS/FIAP 1 PROJETO")

csv_path <- "data/culturas_detalhado.csv"

# Caminho do arquivo exportado pelo script do python.
csv_path <- "data/culturas_detalhado.csv"

# Lê os dados
dados <- read.csv(csv_path, sep=",", header=TRUE, stringsAsFactors=FALSE)

# Converte para numérico as colunas quantitativas
to_num <- function(x) suppressWarnings(as.numeric(x))

dados$Ruas                 <- to_num(dados$Ruas)
dados$Quantidade_por_metro <- to_num(dados$Quantidade_por_metro)
dados$Comprimento          <- to_num(dados$Comprimento)
dados$Largura              <- to_num(dados$Largura)
dados$Base                 <- to_num(dados$Base)
dados$Altura               <- to_num(dados$Altura)
dados$Area_total           <- to_num(dados$Area_total)
dados$Quantidade_total     <- to_num(dados$Quantidade_total)

# Cria vetores
ruas        <- dados$Ruas
qtd_metro   <- dados$Quantidade_por_metro
comprimento <- dados$Comprimento
largura     <- dados$Largura
base        <- dados$Base
altura      <- dados$Altura
area_total  <- dados$Area_total
qtd_total   <- dados$Quantidade_total

# Calcula média e desvio padrão arredondados
resumo <- data.frame(
  Variavel = c("Ruas","Quantidade_por_metro","Comprimento","Largura",
               "Base","Altura","Area_total","Quantidade_total"),
  Media = round(c(mean(ruas, na.rm=TRUE),
                  mean(qtd_metro, na.rm=TRUE),
                  mean(comprimento, na.rm=TRUE),
                  mean(largura, na.rm=TRUE),
                  mean(base, na.rm=TRUE),
                  mean(altura, na.rm=TRUE),
                  mean(area_total, na.rm=TRUE),
                  mean(qtd_total, na.rm=TRUE)), 2),
  Desvio_Padrao = round(c(sd(ruas, na.rm=TRUE),
                          sd(qtd_metro, na.rm=TRUE),
                          sd(comprimento, na.rm=TRUE),
                          sd(largura, na.rm=TRUE),
                          sd(base, na.rm=TRUE),
                          sd(altura, na.rm=TRUE),
                          sd(area_total, na.rm=TRUE),
                          sd(qtd_total, na.rm=TRUE)), 2) # coloquei apenas para simplicar o arredondamento do desvio P. para 2 casas decimais 
)

# Exibe o resumo
print(resumo)


#CONEXAO DA API PARA O CLIMA DA CIDADE ESCOLHIDA DO PROJETO

suppressWarnings(suppressMessages({
  library(httr)
  library(jsonlite)
}))

# Informar a chave da API
api_key <- "155ba7f53a1b2d6ffe95380872e75f8e"

# Coordenadas de Curitiba
# Coloquei o codigo com as coordenadas para garantir que nao haja erro de digitação por conta de espaçõs e acentos

lat <- -25.504
lon <- -49.2908

# Monta URL com latitude/longitude
url <- sprintf(
  "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric&lang=pt_br",
  lat, lon, api_key
)

# Faz a requisição
res <- GET(url)
conteudo <- content(res, "text", encoding = "UTF-8")
clima <- fromJSON(conteudo, simplifyVector = TRUE)

# Exibe os dados formatados
cat("=== Clima atual ===\n")
cat("📍 Local:", clima$name, "-", clima$sys$country, "\n")
cat("🌡️ Temperatura:", clima$main$temp, "°C\n")
cat("🌡️ Sensação térmica:", clima$main$feels_like, "°C\n")
cat("📉 Mínima:", clima$main$temp_min, "°C\n")
cat("📈 Máxima:", clima$main$temp_max, "°C\n")
cat("💧 Umidade:", clima$main$humidity, "%\n")
cat("🌥️ Condição:", clima$weather$description[1], "\n")
cat("💨 Vento:", clima$wind$speed, "m/s\n")





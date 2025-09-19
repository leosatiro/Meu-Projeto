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

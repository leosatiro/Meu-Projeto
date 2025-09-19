# 🌱 Projeto Farmatech – Agricultura Digital

## 📌 Descrição
O **Farmatech** é um sistema desenvolvido em **Python** e **R** para auxiliar no gerenciamento e análise de culturas agrícolas.  
- No **Python**, o sistema permite cadastrar culturas, calcular áreas/insumos e exportar dados em CSV.  
- No **R**, os scripts permitem gerar análises estatísticas e integrar informações climáticas da API OpenWeatherMap.  
- Na pasta **docs/** ficam armazenados documentos complementares, como resumos e links de demonstração da aplicação, conforme orientação no portal.  

---

## 📂 Estrutura do Projeto
```
/FIAP 1 PROJETO
│
├── Projeto_Farmatech.py       # Script principal em Python
├── data/
│   └── culturas_detalhado.csv # Arquivo exportado com os dados das culturas
├── R/
│   ├── analise_agro_clima.R   # Análises estatísticas do CSV
│   ├── clima.R                # Consulta API OpenWeatherMap
│   └── estatisticas.R         # Estatísticas avançadas (médias, desvios, gráficos)
├── docs/
│   ├── video_link.txt         # Link para vídeo demonstrando a aplicação
│   └── Resumo artigo.docx     # Resumo do artigo científico
└── README.md                  # Este arquivo
```

---

## ⚙️ Funcionalidades

### Python (`Projeto_Farmatech.py`)
- 📥 Entrada de dados (culturas, áreas, insumos).  
- 📊 Cálculo automático de área e insumos.  
- 📤 Exportação em `data/culturas_detalhado.csv`.  
- 🔄 Atualização e ❌ Exclusão de dados.  

### R
#### `analise_agro_clima.R`
- Lê `culturas_detalhado.csv`.  
- Calcula médias e desvios-padrão.  
- Gera um resumo estatístico das variáveis.  

#### `clima.R`
- Conecta à **API OpenWeatherMap**.  
- Consulta dados climáticos **por cidade** ou **latitude/longitude**.  
- Retorna **temperatura, umidade, condição do tempo e vento**.  
- Permite integração entre clima e dados agrícolas.  

#### `estatisticas.R`
- Expande a análise estatística com:   
  - 📊 - Métricas realizadas conforme solicitado.
  - 📂 - Resumo dos dados para melhor visualização.



### Docs (`/docs/`)
- 🎥 `video_link.txt` → contém o link para vídeo mostrando a aplicação em funcionamento .py e .R.  
- 📑 `Resumo artigo.docx` → resumo do artigo científico relacionado ao projeto.  

---

## ▶️ Como executar

### Python
```bash
python Projeto_Farmatech.py
```

### R
Rodar cada script dentro da pasta `R/`.

#### Estatísticas básicas:
```r
source("R/analise_agro_clima.R")
```

#### Consulta clima:
```r
source("R/clima.R")
```

#### Estatísticas avançadas:
```r
source("R/estatisticas.R")
```

---

## 📊 Exemplos de saída

### Python
```
Área total da cultura Milho: 5000 m²
Fertilizante: 250.0 KG
Sementes: 500.0 Unidade
```

### R (`analise_agro_clima.R`)
```
       Variavel    Media Desvio_Padrao
1     Area_total 5000.00          0.00
2   Comprimento   100.00          0.00
3       Largura    50.00          0.00
4 Quantidade_total 375.00       176.78
```

### R (`clima.R`)
```
=== Clima atual em Curitiba ===
🌡️ Temperatura: 15 °C
💧 Umidade: 88 %
🌥️ Condição: nublado
💨 Vento: 6.1 m/s
```

### R (`estatisticas.R`)
- Geração de histogramas das áreas plantadas.  
- Boxplots de quantidade total por cultura.  
- Tabela com **mínimo, máximo, média e desvio padrão** de cada variável numérica.  

---

 📌 FIM
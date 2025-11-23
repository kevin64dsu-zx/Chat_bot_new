import re
from typing import List, Tuple

# === DADOS DO RELATÓRIO CONSOLIDADO DA WHIRLPOOL (PORTUGUÊS) ===
# Este é o conteúdo integral do Relatório de Sustentabilidade 2024,
# dividido por seções principais (marcador "### ") para simular "chunks" de dados.
REPORT_TEXT = """
# Relatório de Sustentabilidade 2024 - Whirlpool Corporation

Este documento apresenta um resumo consolidado da estrutura, inovações, desempenho e estratégias de sustentabilidade da Whirlpool Corporation, focando em produtos, operações e compromisso com colaboradores e comunidades ao longo de 2024.

---

## INTRODUÇÃO: Quem Somos

### A Whirlpool
Somos uma líder global em eletrodomésticos, presente no Brasil há mais de 70 anos com as marcas Brastemp, Consul, KitchenAid, B.blend, Compra Certa, Yummly e Compra Direta. Em busca constante de melhorar a vida em casa e inspirar gerações com nossas marcas, a Whirlpool é uma empresa líder global em eletrodomésticos para cozinha e lavanderia. Com mais de 110 anos de história, a Companhia tem cerca **50.000 funcionários** e **55 centros de fabricação e pesquisa tecnológica** no mundo.

### Missão
Ganhar confiança e criar demanda para nossas marcas em um mundo digital.

### Valores
* Integridade
* Respeito
* Inclusão e Diversidade
* One Whirlpool
* Espírito de Vitória

### A Whirlpool no Brasil
No Brasil, a Whirlpool está presente em milhares de lares com a Brastemp, Consul, KitchenAid, B.Blend e Compra Certa, e emprega cerca de **11 mil colaboradores** distribuídos em quatro Unidades: São Paulo, Rio Claro, Joinville e Manaus

#### Inovação com Propósito
O compromisso da Whirlpool é inovar com propósito, sempre com atenção às reais necessidades dos consumidores. Para isso, investimos cerca de **3% a 4% do nosso faturamento anual** em pesquisa, desenvolvimento e inovação (PD&I). Com mais de 800 profissionais dedicados a PD&I no Brasil, a Whirlpool conta com o maior polo de produção e pesquisa de refrigeração da Empresa no mundo, com exportação de tecnologias para mais de 45 países.

#### Iniciativas Sociais e Éticas
* **Consulado da Mulher:** Iniciativa Social da Whirlpool Corporation no Brasil que atua há mais de 20 anos e já impactou mais de **40 mil empreendedoras brasileiras**.
* **ESG:** Estamos comprometidos com o tema há mais de 60 anos. Nosso propósito é melhorar a vida das pessoas em casa e no planeta.
* **Manual de Integridade:** Acreditamos que não há jeito certo de fazer a coisa errada. Nosso Manual de Integridade ajuda a traduzir em ações a forma como conduzimos nossos negócios.

---

## 1. Soluções de Produtos Sustentáveis

### 1.1. Lavadora de Roupas: Definição de um Novo Padrão Ecológico
A Whirlpool Corporation continua a inovar em soluções de lavanderia sustentável. No Brasil, foi lançada uma nova linha de lavadoras Consul com foco em redução da pegada ambiental, incluindo:
* **Modo Eco:** Economiza até **15% de água** e **25% de eletricidade**.
* **Reutilização de água:** Permite que os consumidores usem a água para outras finalidades domésticas.
* **Indicadores de nível de água** e **Dosagem medida** para uso otimizado de recursos.

Globalmente, a empresa aumentou o investimento em lavadoras de carregamento frontal de alta eficiência. Na Índia, 100% do portfólio de lavadoras manteve a classificação **5 estrelas**, o mais alto selo de eficiência energética. As lavadoras modernas usam quase **78% menos energia** do que as de 1992.

### 1.2. Promoção da Sustentabilidade em Outras Categorias de Produtos
A Whirlpool promove a sustentabilidade em todo o seu portfólio:

| Categoria | Inovação de Sustentabilidade em 2024 | Impacto |
| :--- | :--- | :--- |
| **Refrigeração** | **Isolamento SlimTech:** Aumenta a capacidade em até 25% ou torna o refrigerador **até 50% mais eficiente**. | Parceria com a Green Works (Goodwill) para reciclar o metal e o pó de isolamento do SlimTech. |
| **Culinária** | **Colaboração com BORA:** Tecnologia de fogão de indução com exaustor descendente. | Reduz a necessidade de unidades de ventilação suspensas. |
| **Lava-louças** | **Sistema de Abertura de Porta:** Utiliza ar fresco para secar, reduzindo o consumo de energia. | As lava-louças economizam mais de **2.500 galões de água por ano** em comparação com a lavagem à mão. |

### 1.3. Uso Sustentável e Economia Circular
A maior área de impacto ambiental da Whirlpool está na **fase de uso dos produtos** (Escopo 3, Categoria 11).
* **Emissões Escopo 3 (Cat. 11):** Redução de aproximadamente **2,5%** nas emissões de GEE geradas pelo uso de produtos em 2024, progredindo em direção à meta de redução de 20% até 2030 (comparado a 2016).
* **Uso de Materiais:** Aumento do teor de **Resina Pós-Consumo (PCR)** para **12%** nos cestos de lavadoras e **60%** nas bandejas de evaporação de refrigeradores no Brasil.

#### Gestão de Fim de Vida, Reparabilidade e Qualidade
| Área | Destaques de 2024 | Métricas |
| :--- | :--- | :--- |
| **Logística Reversa (Brasil)** | Primeira empresa de eletrodomésticos a oferecer **coleta domiciliar gratuita** em 100% dos municípios brasileiros. | Mais de **55.000 toneladas** de resíduos eletrônicos tratados. |
| **Reparabilidade** | Oferece peças sobressalentes por no mínimo **7 a 10 anos**. | A equipe de Greenville, Ohio, recondicionou mais de **95.000 produtos** (43% dos devolvidos). |
| **Recondicionamento Global** | Os centros globais restauraram **63%** dos produtos devolvidos (**390.076** produtos recondicionados no total). | **0 recalls** emitidos em 2024. |

---

## 2. NOSSAS UNIDADES E OPERAÇÕES

### 2.1. Energia e Emissões Net Zero
A meta global é alcançar emissões **Net Zero (Escopo 1 e 2)** nas fábricas e operações até **2030**.
* **Redução de Emissões:** As emissões de Escopo 1 e 2 foram reduzidas em **36%** em 2024.
* **Liderança em Energia Verde (EUA):** **86%** das necessidades de manufatura dos EUA supridas por energia renovável.
* **Projetos de Descarbonização:** Eletrificação do processo de limpeza em **Celaya, México** (redução de 5% nas emissões de Escopo 1).

| Região | Cobertura de Energia Renovável em 2024 | Destaques |
| :--- | :--- | :--- |
| **EUA** | **100%** do consumo de eletricidade não gerada por sistemas próprios é compensado por RECs. | Metas de energia própria em 100% das fábricas de pequenos e grandes eletrodomésticos até 2025. |
| **Brasil** | **100%** do consumo de eletricidade é compensado por RECs. | Possui uma pequena fazenda solar na unidade de Joinville. |
| **Índia** | **18%** do consumo total de energia coberto por fontes renováveis próprias. | 9 MW de capacidade solar no telhado. |

### 2.2. Gestão de Recursos
* **Água:** Atingida a meta de redução de **3%** na intensidade do uso da água em 2024. Unidades no Brasil, Índia e México reutilizam **100%** dos efluentes tratados.
* **Resíduos:** Taxa de **desvio de aterro de 97% ou mais** em todas as unidades globais (**Zero Resíduos para Aterros - ZWtL**).
* **Segurança Ocupacional:** Lesões graves reduzidas em **50%** e taxa de lesões e doenças registráveis reduzida em **12%** em 2024 (vs. 2023).

---

## 3. NOSSAS PESSOAS E COMUNIDADES

### 3.1. Experiência, Liderança e Bem-Estar
* **Modelo de Liderança:** Focado em **Viés para Ação**, **Responsabilização** e **Lidere com Impacto**.
* **Estratégia Be*Well:** Estrutura global holística de bem-estar.
* **Apoio a Pais que Trabalham:** Incluída na lista da **Seramount das 100 Melhores Empresas para Pais que Trabalham em 2024**.

### 3.2. Aprendizado e Engajamento
* **WeLEARN:** Plataforma digital de aprendizagem global.
* **WeGROW:** Programa lançado em 2024 para desenvolver talentos, com mais de **4.700 colaboradores** envolvidos.
* **Engajamento:** O engajamento atingiu a melhor pontuação desde 2021 em Outubro.

### 3.3. Inclusão e Diversidade (I&D)
* **Reconhecimento:** Incluída no **Seramount Inclusion Index 2024**.
* **Grupos de Colaboradores (ERGs):** Fortalecem a cultura, com expansão para o **Pune Tech Center, na Índia** em 2024.
* **Apoio Comunitário dos ERGs:** O **WVA** (Veterans & Allies) apoiou o programa *Homes for Our Troops* por 10 anos.

### 3.4. Impacto na Comunidade
A Whirlpool Foundation concentra subsídios na estratégia **House+Home** com foco em I&D.
* **Habitat for Humanity:** Celebrando 25 anos de parceria com **US$ 150 milhões** em financiamento e **250.000 eletrodomésticos** doados.
* **BuildBetter with Whirlpool:** Renovação do apoio com **US$ 2,5 milhões** (2025–2026) para construir moradias **Net Zero Ready**, que oferecem **45%** de economia média nos custos de energia.
* **The Washing Machine Project (TWMP):** Apoio ao fornecimento de lavadoras manuais, visando afetar **150.000 pessoas**.
* **Consulado da Mulher (Brasil):** Ajudou **1.657 mulheres** a concluir programas de educação em empreendedorismo em 2024.
* **Care Counts (Marca Whirlpool):** Em 2024, **164 escolas em 41 estados** foram beneficiadas, resultando em cerca de **87% de aumento na taxa de frequência** entre alunos de alto risco.
* **Feel Good Fridge:** Doação de **1.431 refrigeradores** desde 2021 para combater a insegurança alimentar.

---

## APÊNDICE: Sobre este Relatório, ODS da ONU e Políticas

### Sobre o Relatório
* **Período de Cobertura:** 1º de janeiro de 2024 a 31 de dezembro de 2024.
* **Abrangência:** Inclui 100% das unidades de fabricação e da força de trabalho própria. **Nota:** Inclui dados do negócio EMEA apenas até 1º de abril de 2024 (data da transação com a *Arcelik*).
* **Estrutura de Relatório:** Preparado com base nos **GRI Standards**, e inclui índices **SASB**, **TCFD** e **ODS (Objetivos de Desenvolvimento Sustentável)**.
* **Garantia:** Obteve garantia limitada de terceiros da **Ernst & Young LLP**.

### ODS da ONU - Metas e Resultados de 2024
Este índice detalha o progresso da Whirlpool Corporation em relação às áreas materiais e aos Objetivos de Desenvolvimento Sustentável da ONU (ODS).

| Questão Material | Metas e Compromissos | Resultados e ações de 2024 | Objetivos ODS |
| :--- | :--- | :--- | :--- |
| **Inovação e Design for Sustainability** | Reduzir as emissões de nossos produtos em uso (escopo 3, categoria 11) em 20%¹ até 2030. | Alcançamos uma redução de aproximadamente 2,5% nas emissões de nossos produtos em uso (escopo 3, categoria 11) em 2024 em comparação com o ano anterior. | ODS 7, 12, 13 |
| **Economia Circular e Uso de Materiais** | Facilitamos a reutilização de produtos por meio de centros globais de recondicionamento. | 63% dos produtos devolvidos foram recondicionados em nossos centros globais de recondicionamento em 2024. | ODS 12 |
| **Cadeia de Suprimentos Responsável** | Auditar fornecedores priorizados com base em risco. Revisar 100% de quaisquer descobertas de alto-risco da Due Diligence. | Realizadas mais de 271 auditorias do Código de Conduta de Fornecedores. 100% dos fornecedores de alto risco foram avaliados e categorizados. | ODS 8, 12 |
| **Segurança do Produto** | Identificar, avaliar e fechar todos os relatos de possíveis questões de segurança em tempo hábil. | 18 possíveis problemas de segurança resolvidos. Nenhum recall voluntário e involuntário de segurança de produtos emitido. | ODS 3, 12 |
| **Qualidade de Produtos** | Proporcionar a melhor experiência ao consumidor com cada eletrodoméstico a qualquer hora e em qualquer lugar. | Resolvemos problemas 35% mais rápido ao implementar um novo sistema de gestão, melhorando a visibilidade de todas as questões em aberto. | ODS 9, 12 |
| **Emissões de Gases de Efeito Estufa (GEE)** | Atingir Net Zero Emissões em nossas unidades (escopos 1 e 2) até 2030. | Alcançamos uma redução de emissões de GEE de 36% nas emissões dos escopos 1 e 2 em comparação com o ano anterior. | ODS 7, 13 |
| **Gestão de Resíduos** | Manter uma taxa de desvio de aterro de pelo menos 97% em todas as unidades de manufatura (acima do nível Ouro do UL Zero Waste to Landfill [ZWtL]). | Alcançamos uma taxa de desvio de aterro de 97% ou mais em todas as nossas unidades de manufatura globais. | ODS 12 |
| **Gestão de Água** | Reduzir a intensidade hídrica em 3% a cada ano em nossas unidades. | Alcançada uma redução de 3% na intensidade hídrica em 2024 em comparação com o ano anterior. | ODS 6, 12 |
| **Gestão de Energia** | Reduzir a intensidade energética em 3% a cada ano em nossas unidades. | A Whirlpool não atingiu essa meta, mas continuamos trabalhando na redução da intensidade energética. | ODS 7 |
| **Inclusão e Diversidade** | Promover uma força de trabalho que represente a diversidade de talentos disponíveis no mercado em todos os níveis da organização e uma cultura onde cada colaborador sinta um senso de pertencimento. | Recebemos reconhecimento por nossa liderança na promoção de um ambiente de trabalho inclusivo, com destaque no Seramount Inclusion Index 2024. | ODS 5, 8, 10 |
| **Saúde e Segurança Ocupacionais** | Atingir zero fatalidades e incidentes graves no mundo todo. Reduzir as taxas de incidentes globalmente em 10% a cada ano. | Zero fatalidades e 4 ferimentos graves. Redução de 12% na taxa de lesões e doenças registráveis em comparação com o ano anterior. | ODS 3, 8 |
| **Comunidades Locais** | Construir mais de 250 casas resistentes ao clima e com eficiência energética junto com a Habitat for Humanity dos EUA até 2024. | 260 casas resistentes ao clima e com eficiência energética construídas nos EUA até 2024 por meio da iniciativa BuildBetter with Whirlpool da Habitat. | ODS 11, 13 |

---
*¹ Em comparação com a linha de base de 2016.*

### Políticas Corporativas Globais
A Whirlpool Corporation está comprometida com um catálogo robusto de políticas que promovem tratamento justo para todos, supervisionadas pela alta liderança e, em muitos casos, pelo Conselho de Administração.

| Área de Política | Compromisso Principal | Governança Chave |
| :--- | :--- | :--- |
| **Anticompetitivo** | Compromisso em cumprir as leis antitruste globais com um programa de compliance robusto. | Supervisão pelo conselho e liderança sênior. |
| **Anticorrupção** | Tolerância zero a suborno e corrupção; uso de programa global de *due diligence* para terceiros. | Supervisão pelo conselho, Comitê Executivo e Comitê de Direção Global de Ética. |
| **Cibersegurança** | Gerir riscos, proteger ativos de informação e seguir a Estrutura NIST. | Supervisão do Conselho de Administração e Comitê de Auditoria. |
| **Privacidade de Dados** | Proteger dados, cumprir obrigações de compliance e ser transparente sobre o uso. | Diretor de Proteção de Dados Global e Comitê Diretor de Segurança Cibernética e Privacidade. |
| **Meio Ambiente, Saúde, Segurança** | Proteger colaboradores, preservar o meio ambiente e garantir a segurança física. | Supervisão pela liderança sênior e conselho. |
| **Remuneração Executiva** | Remuneração por desempenho, com elementos ESG incluídos nos objetivos executivos. | Supervisão pelo conselho (Comitê de Remuneração). |
| **Direitos Humanos** | Apoio aos direitos humanos, combate à discriminação, escravidão e trabalho infantil; Código de Conduta de Fornecedores (SCoC). | Supervisão pelo conselho, Linha de Integridade. |
| **Direitos Trabalhistas** | Respeito aos direitos de associação e negociação coletiva. 50% dos colaboradores horistas cobertos por acordo coletivo em 2024. | Supervisão pela liderança sênior. |
| **Não Discriminação e Antiassédio** | Garantir um ambiente de trabalho profissional, respeitoso e livre de assédio. | Supervisão pela liderança sênior e treinamento obrigatório. |
| **Pagamento e Igualdade de Remuneração** | Oferecer remuneração total competitiva e equitativa internamente; revisão anual por escritório de advocacia externo para igualdade salarial. | Supervisão pelo conselho e liderança sênior; Verificação externa. |
| **Risco Regulatório e Políticas Públicas** | Cumprir todos os requisitos legais e regulatórios; atividades de *advocacy* revisadas anualmente. | Supervisão pelo conselho, liderança sênior e comitês multifuncionais. |
| **Fiscal** | Administrar obrigações fiscais de maneira responsável e cumprir o espírito e a intenção das leis fiscais. | Supervisão pelo conselho e liderança sênior. |
"""

def get_report_chunks(text: str) -> List[Tuple[str, str]]:
    """Divide o texto do relatório em 'chunks' (pedaços) baseados em cabeçalhos Markdown."""
    chunks = [("INTRODUÇÃO", text[:text.find("---")].strip())]

    sections = re.split(r'(\n## [^\n]+|\n### [^\n]+)', text)
    
    current_title = "Diversos"
    current_content = ""

    for item in sections[3:]: 
        if item.startswith('\n## ') or item.startswith('\n### '):
            if current_content:
                chunks.append((current_title.strip(), current_content.strip()))
            current_title = item.strip().replace('\n', '')
            current_content = ""
        else:
            current_content += item

    if current_content:
        chunks.append((current_title.strip(), current_content.strip()))
        
    return chunks

def retrieve_context(query: str, chunks: List[Tuple[str, str]], top_k: int = 3) -> str:
    """
    Simula a fase de Recuperação (Retrieval) do RAG.
    """
    query_words = set(query.lower().split())
    relevance_scores = []

    for title, content in chunks:
        content_lower = content.lower()
        score = sum(1 for word in query_words if word in content_lower or word in title.lower())
        
        if score > 0:
             relevance_scores.append((score, title, content))

    relevance_scores.sort(key=lambda x: x[0], reverse=True)
    
    context = ""
    retrieved_chunks_count = 0
    for score, title, content in relevance_scores:
        if retrieved_chunks_count < top_k:
            # Limita para não ser muito longo
            context += f"\n\n--- Seção Relevante: {title} ---\n{content[:500]}..." 
            retrieved_chunks_count += 1
    
    if not context:
        return "Nenhum contexto relevante encontrado no relatório."
        
    return context

def simulate_llm_generation(query: str, context: str) -> str:
    """
    Simula a fase de Geração (Generation) com o LLM.
    
    Para uma implementação real, use o contexto recuperado para chamar a API do Gemini.
    """
    if "Nenhum contexto" in context:
        return "Não foi possível encontrar informações específicas para sua pergunta no relatório."
        
    # --- AQUI ESTARIA A CHAMADA REAL À API GEMINI ---
    
    # Simulação de resposta baseada no contexto:
    return (
        f"RESPOSTA GERADA (SIMULAÇÃO):\n\n"
        f"Pergunta: '{query}'\n\n"
        f"A resposta seria sintetizada pelo Gemini com base nos seguintes trechos recuperados do relatório:\n"
        f"{context}\n\n"
        f"Para obter uma resposta precisa, substitua esta função (simulate_llm_generation) pela chamada real à API Gemini."
    )

def run_rag_system():
    """Função principal para rodar o sistema RAG."""
    print("\n===================================================================")
    print("     ASSISTENTE DE PESQUISA RAG PARA RELATÓRIO WHIRLPOOL 2024")
    print("===================================================================")
    print("O relatório foi carregado. Faça perguntas sobre o conteúdo (em português).")
    print("Ex: Qual o percentual de redução de emissões de GEE alcançado em 2024?")
    print("Ex: Quais são os valores da empresa?")
    print("Digite 'sair' para encerrar.")
    
    chunks = get_report_chunks(REPORT_TEXT)
    
    while True:
        query = input("\nSua Pergunta > ")
        if query.lower() == 'sair':
            print("Encerrando o assistente de pesquisa. Até mais!")
            break
        
        if not query.strip():
            continue

        # 1. Recuperação do Contexto
        context = retrieve_context(query, chunks)
        
        # 2. Geração da Resposta (Simulação)
        answer = simulate_llm_generation(query, context)
        
        print("\n--- Resultado da Pesquisa ---")
        print(answer)
        print("-----------------------------\n")

# A chamada para run_rag_system() foi removida daqui
# para permitir que seja chamada pelo app.py.
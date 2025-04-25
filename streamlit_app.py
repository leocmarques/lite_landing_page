import streamlit as st
import openai

# --- Interface ---
st.set_page_config(page_title="Gerador de Landing Page Médica", layout="wide")
st.title("Gerador de Landing Page Médica via OpenAI")

# --- Inputs do Usuário ---
api_key = st.text_input("🔑 API Key da OpenAI", type="password")

st.header("👩‍⚕️ Dados do Médico(a)")
nome_medico = st.text_input("Nome completo com título (Dr./Dra.)")
especialidade = st.text_input("Especialidade médica principal")
subespecialidades = st.text_input("Subespecialidades (opcional)")
crm_estado = st.text_input("Número de CRM e estado")
anos_experiencia = st.text_input("Anos de experiência (opcional)")
formacoes = st.text_input("Principais formações e especializações (opcional)")
associacoes = st.text_input("Associações profissionais (opcional)")
filosofia = st.text_area("Filosofia de atendimento (em uma frase)")

st.header("🩺 Condição/Tratamento")
condicao = st.text_input("Nome da condição/tratamento principal")
sintomas = st.text_area("Principais sintomas associados")
publico_alvo = st.text_area("Público-alvo (idade, gênero, características)")
diferenciais = st.text_area("Diferenciais do tratamento oferecido")
eficacia = st.text_input("Eficácia do tratamento (opcional)")
tempo_tratamento = st.text_input("Tempo médio de tratamento/recuperação")

st.header("📍 Informações Práticas")
localizacao = st.text_input("Localização do consultório (bairro, cidade)")
atendimento = st.selectbox("Opções de atendimento", ["Presencial", "Teleconsulta", "Ambos"])
convenios = st.text_input("Aceita convênios? (Sim/Não/Quais)")
pagamento = st.text_input("Facilidades de pagamento")
palavras_chave = st.text_area("Palavras-chave para SEO (5-10 palavras separadas por vírgula)")

if st.button("🚀 Gerar Landing Page"):
    if not api_key:
        st.error("Por favor, insira sua API Key.")
    else:
        openai.api_key = api_key

        # Instruções fixas (podem ser carregadas de um arquivo separado se quiser)
        instrucoes_lp = """PROMPT PARA CRIAÇÃO DE COPY PARA LANDING PAGE MÉDICA

 CONTEXTO GERAL
 Crie um copy completo e persuasivo para uma landing page médica destinada a captar pacientes que chegam através de anúncios do Google Ads. A página deve transmitir profissionalismo, confiança e empatia, enquanto apresenta claramente os serviços médicos oferecidos e incentiva o agendamento de consultas.

DADOS DE ENTRADA (para personalização do copy):
- Dados do Médico:
- Nome completo com título (Dr./Dra.)
- Especialidade médica principal
- Subespecialidades (se houver)
- Número de registro no CRM e estado
- Anos de experiência
- Principais formações e especializações
- Associações profissionais
- Filosofia de atendimento em uma frase
- Condição/Tratamento:
- Nome da condição ou tratamento principal
- Principais sintomas associados
- Público-alvo (idade, gênero, características específicas)
- Diferenciais do tratamento oferecido
- Eficácia do tratamento (dados ou estatísticas, se disponíveis)
- Tempo médio de tratamento ou recuperação
- Informações Práticas:
- Localização do consultório (bairro, cidade)
- Opções de atendimento (presencial, teleconsulta)
- Aceitação de convênios (sim/não, quais)
- Facilidades de pagamento
- Horários de atendimento
- Palavras-chave (Lista de 5-10 palavras-chave principais para SEO)

 ESTRUTURA DA LANDING PAGE
 1. HEADLINE PRINCIPAL
 Crie um headline impactante que: - Aborde diretamente o problema ou condição
Ofereça uma solução clara ou alívio - Inclua um benefício emocional - Contenha a
 localização geográfica (para SEO) - Seja conciso e direto (máximo 10-12 palavras)
 2. SUB-HEADLINE
 Desenvolva um sub-headline que: - Complemente o headline principal - Adicione
 credibilidade (mencione experiência ou abordagem) - Reforce o benefício principal - Crie
 senso de urgência ou importância - Seja ligeiramente mais longo que o headline (15-20
 palavras)
 3. INTRODUÇÃO AO PROBLEMA
 Escreva um parágrafo introdutório que: - Descreva os sintomas ou desafios da condição
Crie identificação com o leitor ("Você sente...") - Valide as preocupações do paciente
Sugira que há uma solução disponível - Termine com uma mensagem de esperança ou
 empatia
 4. APRESENTAÇÃO DO MÉDICO
 Crie um parágrafo que: - Apresente o médico de forma calorosa e profissional - Destaque
 suas principais credenciais e experiência - Mencione sua abordagem única ou filosofia
 de tratamento - Inclua um elemento humano ou pessoal - Construa confiança e
 autoridade
 5. BENEFÍCIOS DO TRATAMENTO
 Desenvolva uma lista de 4-6 benefícios que: - Comece cada item com um verbo ou
 resultado positivo - Combine benefícios físicos e emocionais - Seja específica e evite
generalidades - Inclua diferenciais competitivos - Use marcadores (bullets) para facilitar
 a leitura
 6. PROCESSO DE TRATAMENTO
 Descreva as etapas do tratamento: - Divida em 3-6 etapas numeradas e nomeadas
Explique brevemente cada etapa - Enfatize a simplicidade ou eficácia do processo
Mencione o acompanhamento personalizado - Inclua o tempo estimado quando
 relevante
 7. DEPOIMENTOS
 Crie espaço para 2-3 depoimentos que: - Representem pacientes com diferentes perfis
Incluam nome, idade ou ocupação (pode ser fictício) - Foquem em resultados
 específicos e mensuráveis - Contenham elementos emocionais - Abordem objeções
 comuns indiretamente
 8. PERGUNTAS FREQUENTES (FAQ)
 Desenvolva 5-8 perguntas e respostas que: - Abordem as principais dúvidas sobre o
 tratamento - Incluam questões sobre eficácia, segurança e recuperação - Mencionem
 aspectos práticos (convênios, pagamentos) - Respondam objeções comuns - Sejam
 concisas e diretas
 9. CHAMADAS PARA AÇÃO (CTAs)
 Crie 3 variações de CTAs para usar ao longo da página: - CTA principal para agendamento
 de consulta - CTA secundário para mais informações - CTA final com senso de urgência
Todas devem ser claras, diretas e no imperativo
 10. SEÇÃO DE CONTATO/LOCALIZAÇÃO
 Finalize com uma seção que: - Reforce a facilidade de acesso ou contato - Mencione
 opções de agendamento (WhatsApp, telefone) - Inclua o endereço completo - Destaque
 facilidades (estacionamento, acesso) - Termine com uma última mensagem de incentivo
 DIRETRIZES DE ESTILO E TOM

Tom de Voz:
- Profissional mas acessível
- Empático e compreensivo
- Confiante sem ser arrogante
- Educativo sem excesso de termos técnicos
- Focado no paciente ("você", "seu/sua")

 Linguagem:
- Use frases de tamanho variado para ritmo natural
- Evite jargão médico excessivo
- Explique termos técnicos quando necessários
- Prefira voz ativa à passiva
- Mantenha parágrafos curtos (3-4 linhas)

 Elementos Persuasivos:
- Inclua gatilhos de escassez quando apropriado ("vagas limitadas")
- Use prova social (número de pacientes atendidos, taxa de sucesso)
- Destaque a autoridade do médico
- Aborde e neutralize objeções comuns

 SEO:
- Incorpore naturalmente as palavras-chave fornecidas
- Use a localização geográfica em pontos estratégicos
- Inclua a especialidade e condição no título e subtítulos
- Crie subtítulos (H2, H3) otimizados para SEO
- Mantenha densidade de palavras-chave natural

 EXEMPLOS DE HEADLINES E SUB-HEADLINES
 Para cada tipo de especialidade médica, forneça 3 opções de headline e sub-headline correspondente:
 EXEMPLOS ABAIXO:
 PARA GINECOLOGIA/OBSTETRÍCIA:
 Opção 1: - Headline: "Liberte-se dos Incômodos Femininos com Tratamento
 Especializado em São Paulo" - Sub-headline: "Diagnóstico preciso e tratamento
 personalizado para infecções recorrentes, com acompanhamento humanizado da Dra.
 [Nome]"
Opção 2: - Headline: "Método Contraceptivo Eficaz e Sem Preocupações Diárias em São
 Paulo" - Sub-headline: "Conheça o Implanon: 99% de eficácia, colocação rápida e até 3
 anos de proteção com a Dra. [Nome], especialista em saúde da mulher"
 Opção 3: - Headline: "Cólicas Intensas e Dor na Relação? Pode Ser Endometriose" -
Sub-headline: "Tratamento minimamente invasivo com o Dr. [Nome], especialista em
 cirurgia de endometriose com mais de [X] casos de sucesso em São Paulo"
 PARA OFTALMOLOGIA:
 Opção 1: - Headline: "Tratamento Completo para Estrabismo em São Paulo – Infantil e
 Adulto" - Sub-headline: "Recupere o alinhamento visual e a autoestima com a Dra.
 [Nome], especialista em oftalmologia pediátrica e estrabismo há [X] anos"
 Opção 2: - Headline: "O Estrabismo Afeta Mais que a Aparência: Tratamento
 Especializado em SP" - Sub-headline: "Cirurgia segura e eficaz com a Dra. [Nome],
 devolvendo qualidade de vida e confiança para crianças e adultos"
 Opção 3: - Headline: "Olhos Desalinhados? Tratamento Moderno para Estrabismo em
 São Paulo" - Sub-headline: "Avaliação completa e opções de tratamento personalizadas
 com a Dra. [Nome], referência em oftalmologia pediátrica"
 PARA PSIQUIATRIA:
 Opção 1: - Headline: "Ajude Seu Filho a Superar Desafios Emocionais em Fortaleza" -
Sub-headline: "Atendimento especializado em psiquiatria infantil com a Dra. [Nome],
 criando um ambiente seguro para desenvolvimento e bem-estar"
 Opção 2: - Headline: "TDAH, Autismo e Ansiedade: Diagnóstico Preciso em Fortaleza" -
Sub-headline: "Avaliação completa e tratamento individualizado para crianças e
 adolescentes com a Dra. [Nome], psiquiatra infantil há [X] anos"
 Opção 3: - Headline: "Comportamento Preocupante do Seu Filho? Psiquiatra Infantil em
 Fortaleza" - Sub-headline: "Abordagem acolhedora e humanizada para transtornos
 emocionais e comportamentais com a Dra. [Nome], especialista em saúde mental
 infantil"
 PARA DERMATOLOGIA:
 Opção 1: - Headline: "Pele Renovada e Autoestima Restaurada: Tratamentos
 Dermatológicos em [Cidade]" - Sub-headline: "Procedimentos avançados para acne,
 manchas e rejuvenescimento com o Dr. [Nome], dermatologista com [X] anos de
 experiência"
Opção 2: - Headline: "Adeus Acne e Marcas: Tratamento Dermatológico Completo em
 [Cidade]" - Sub-headline: "Protocolos personalizados e tecnologia de ponta para uma
 pele saudável e radiante com a Dra. [Nome]"
 Opção 3: - Headline: "Problemas de Pele Afetando Sua Confiança? Dermatologista em
 [Cidade]" - Sub-headline: "Diagnóstico preciso e tratamentos eficazes para todas as
 condições de pele com o Dr. [Nome], membro da Sociedade Brasileira de Dermatologia"
 PARA ORTOPEDIA:
 Opção 1: - Headline: "Dor nas Costas ou Articulações? Tratamento Ortopédico
 Especializado em [Cidade]" - Sub-headline: "Alívio duradouro e recuperação da
 mobilidade com o Dr. [Nome], ortopedista especializado em coluna e articulações"
 Opção 2: - Headline: "Recupere seus Movimentos: Ortopedista Especializado em
 [Cidade]" - Sub-headline: "Tratamentos conservadores e cirúrgicos de última geração
 para lesões esportivas e problemas articulares com o Dr. [Nome]"
 Opção 3: - Headline: "Joelho, Ombro ou Quadril: Tratamento Ortopédico Avançado em
 [Cidade]" - Sub-headline: "Diagnóstico preciso com exames de imagem modernos e
 abordagem personalizada pelo Dr. [Nome], especialista em medicina esportiva"

 CONSIDERAÇÕES FINAIS
- Adapte o conteúdo ao perfil demográfico e psicográfico do público-alvo.
- Enfatize os benefícios emocionais além dos físicos.
- Mantenha o foco na solução, não apenas no problema.
- Inclua elementos de urgência sem criar pânico desnecessário.
- Teste diferentes versões de headlines para otimizar a conversão.
- Garanta que o copy esteja alinhado com as diretrizes éticas da publicidade médica do CFM.
- Mantenha um equilíbrio entre informação educativa e persuasão.
- Certifique-se de que todas as afirmações possam ser comprovadas.
- Revise o texto para garantir clareza, empatia e profissionalismo.
- Inclua microcopy para botões e formulários que reduza a fricção para agendamento."""

        # Montar o "pergunta_lp" com os dados inputados
        pergunta_lp = f"""Abaixo, temos todos os dados de entrada. Agora, gere este resultado seguindo as instruções dadas anteriormente:

📥 Coleta de Dados:
- Nome do médico: {nome_medico}
- Especialidade médica principal: {especialidade}
- Subespecialidades: {subespecialidades or "não informado"}
- Número de registro no CRM e estado: {crm_estado}
- Anos de experiência: {anos_experiencia or "não exibir"}
- Principais formações e especializações: {formacoes or "não exibir"}
- Associações profissionais: {associacoes or "não informado"}
- Filosofia de atendimento: {filosofia}
- Nome da condição ou tratamento principal: {condicao}
- Principais sintomas associados: {sintomas}
- Público-alvo: {publico_alvo}
- Diferenciais do tratamento oferecido: {diferenciais}
- Eficácia do tratamento: {eficacia or "não informado"}
- Tempo médio de tratamento ou recuperação: {tempo_tratamento}
- Localização do consultório: {localizacao}
- Opções de atendimento: {atendimento}
- Aceitação de convênios: {convenios}
- Facilidades de pagamento: {pagamento}
- Palavras-chave para SEO: {palavras_chave}
"""

        with st.spinner("Aguarde, gerando a landing page..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": instrucoes_lp},
                        {"role": "user", "content": pergunta_lp}
                    ]
                )
                resposta = response['choices'][0]['message']['content']
                st.success("✅ Landing page gerada com sucesso!")
                st.markdown(resposta)
            except Exception as e:
                st.error(f"Erro ao gerar: {e}")

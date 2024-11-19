import streamlit as st
import json

# Texto base com placeholders
texto_base = """
Reclamação Trabalhista – Rito Sumaríssimo

PROCESSO Nº RTSum-{{processo}}

Reclamante: {{nome_autor}}

Reclamad{{genero_reu}}: {{nome_reus}}

Vistos,

Submetido o feito a julgamento foi proferida a seguinte

SENTENÇA

I - RELATÓRIO

Dispensado na forma do artigo 852-I, da CLT.

Reclamação Trabalhista – Rito Ordinário

PROCESSO Nº RTOrd-{{processo}}

Reclamante: {{nome_autor}}

Reclamad{{genero_reu}}: {{nome_reus}}

Vistos,

Submetido o feito a julgamento foi proferida a seguinte

SENTENÇA

I - RELATÓRIO

{{nome_autor}}, qualificad{{genero_autor}} na petição inicial, ajuizou a presente RECLAMAÇÃO TRABALHISTA em face d{{genero_reu}} reclamad{{genero_reu}} {{nome_reus}}.

Atribuiu à causa o valor de {{valor_causa}} e apresentou procuração e documentos.

Notificad{{genero_reu}}, {{genero_reu}} reclamad{{genero_reu}} compareceu em Juízo e apresentou defesa escrita, com documentos.

Houve manifestação d{{genero_autor}} reclamante.

Na sessão de prosseguimento foram ouvidas as partes e testemunhas. Não foram produzidas outras provas, encerrando-se a instrução processual.

As partes permaneceram inconciliadas.

Este é o Relatório.

Decido.

II - FUNDAMENTAÇÃO

QUESTÕES PRELIMINARES

LIMITAÇÃO DOS VALORES DOS PEDIDOS E PRINCÍPIOS DA INFORMALIDADE E SIMPLICIDADE

Em decisão recente, a Subseção I Especializada em Dissídios Individuais do Tribunal Superior do Trabalho para, por unanimidade de votos, uniformizou a jurisprudência sobre o tema, proferindo a seguinte decisão:

EMBARGOS. RECURSO DE REVISTA. LIMITAÇÃO DA CONDENAÇÃO AOS VALORES ATRIBUÍDOS AOS PEDIDOS NA PETIÇÃO INICIAL. IMPOSSIBILIDADE. INTERPRETAÇÃO TELEOLÓGICA DO ART. 840, §1º, DA CLT. APLICAÇÃO DA REGRA ESPECIAL PREVISTA NA IN 41/2018 C/C ART. 840, §1º, DA CLT. VALORES INDICADOS NA PETIÇÃO COMO MERA ESTIMATIVA. Embargos conhecidos e não providos. (TST, SDI-I, Relator Ministro Alberto Bastos Balazeiro, PROCESSO Nº TST-Emb-RR-555-36.2021.5.09.0024, julgado em 30/11/2023, Publicação: 07/12/2023).

Com isso, este Juízo passa a adotar os valores indicados na inicial como mera estimativa, sem limitação em eventual cálculo.

ASSISTÊNCIA JUDICIÁRIA

A ação foi ajuizada depois do início da vigência da Lei 13.467/2017, em 11-11-2017 (Reforma Trabalhista).

Para a Primeira, Segunda, Terceira, Sexta, Sétima e Oitava Turmas do C. TST, basta que a parte autora declare sua condição de hipossuficiência: RRAg-1000142-27.2021.5.02.0371 (DEJT 18/12/2023), RRAg-1000243-58.2022.5.02.0006 (DEJT 18/12/2023), Ag-AIRR-11661-32.2017.5.03.0014 (DEJT 18/12/2023), RR-1000097-52..2022.5.02.0447 (DEJT 18/12/2023), RRAg-1001257-66.2021.5.02.0021 (DEJT 19/12/2023) e Ag-RR-101028-47.2020.5.01.0037 (DEJT 19/12/2023).

A declaração se encontra nos autos.

Assim, à míngua de outras provas, tenho que {{genero_autor}} reclamante não possui rendimentos que justifiquem a não concessão dos benefícios da assistência judiciária gratuita.

Preenchidos os requisitos legais, ficam deferidos os benefícios da assistência judiciária gratuita.

INÉPCIA

A petição inicial indica o Juiz a quem é dirigida e contém a qualificação das partes, a exposição dos fatos de que resulte o dissídio e os pedidos.

Sobre isso:

PETIÇÃO INICIAL. INÉPCIA. NÃO CONFIGURAÇÃO. O processo trabalhista exige apenas uma breve exposição dos fatos e o pedido, conforme o artigo 840 da CLT, regendo-se pelo princípio da simplicidade. Se do sucinto relato dos fatos decorre de forma lógica qual a pretensão buscada pelo reclamante, tendo havido ampla defesa pela reclamada, impõe-se seja afastada a inépcia da petição inicial. (TRT18, RO - 0011819-39.2013.5.18.0102, Rel. GENTIL PIO DE OLIVEIRA, 1ª TURMA, 10/09/2014).

PETIÇÃO INICIAL. AUSÊNCIA DE PEDIDO CERTO OU DETERMINADO. É certo que o processo do trabalho, instrumento assecuratório de prestação de natureza alimentar, tem vocação para a celeridade e para a simplicidade, especialmente em razão do jus postulandi. Mas, se a parte constitui advogado, nada justifica que a ação seja apresentada sem os requisitos de técnica que buscou assegurar com a contratação do profissional legalmente habilitado para tanto. Portanto, se a petição inicial prescinde de complexa narrativa - CLT, art. 840, § 1º, não prescinde, ainda assim, do pedido, sendo norma cogente a apresentação deste de modo certo ou determinado, para que dele possa haver contestação ou impugnação específica, e que seja interpretado restritivamente, de modo a configurando litispendência ou coisa julgada dentro dos seus limites claros (CPC, art. 286, 300, 293 e 460, colhidos em subsídio autorizado pelo art. 769, CLT). No caso, Embora a petição inicial não observe a melhor técnica, sua narração revela-se compreensível quanto à disposição dos fatos e pedidos deduzidos, tendo sido suficiente à articulação da defesa, sem qualquer prejuízo à parte ré. É o quanto basta ao atendimento da norma do art. 840 da CLT e do art. 282 do CPC. (TRT18, RO - 0010385-78.2014.5.18.0102, Rel. EUGÊNIO JOSÉ CESÁRIO ROSA, 1ª TURMA, 25/08/2014).

Cabe registrar que {{genero_reu}} reclamad{{genero_reu}} não teve dificuldade na elaboração de sua defesa, eis que apresentou a contestação de ID {{contestacao}}.

Dessa forma, rejeito a preliminar de inépcia arguida tendo em vista que a petição inicial atendeu satisfatoriamente os requisitos do § 1º do artigo 840 da CLT, não se vislumbrando, de outra parte, qualquer prejuízo à defesa d{{genero_reu}} reclamad{{genero_reu}}.

PREJUDICIAL DE MÉRITO

PRESCRIÇÃO QUINQUENAL

Em razão da arguição na contestação e como foi dado à parte autora a oportunidade de se manifestar, pronuncio a prescrição daquelas parcelas cujos direitos materiais correspondentes hajam sido violados em data anterior a {{prescricao}} (Constituição Federal, art. 7º, XXIX), razão pela qual o feito em relação a elas fica julgado extinto com resolução do mérito, na forma do art. 487, II, do CPC/2015.

III - DISPOSITIVO

Ante o exposto, nesta RECLAMAÇÃO TRABALHISTA movida por {{nome_autor}} em face de {{nome_reus}}, decido:
a)
b)
c) julgar IMPROCEDENTES todos os pedidos formulados.

Custas processuais pel{{genero_autor}} reclamante, calculadas sobre o valor dado à causa de {{valor_causa}}, no importe de {{custas}}, que do pagamento fica dispensad{{genero_autor}} na forma da Lei, em razão dos benefícios da justiça gratuita que lhe são concedidos.

INTIMEM-SE.

III - DISPOSITIVO

Ante o exposto, nesta RECLAMAÇÃO TRABALHISTA movida por {{nome_autor}} em face de {{nome_reus}}, decido:
a)
b)
c) julgar PROCEDENTES EM PARTE os pedidos formulados acolhendo as seguintes parcelas: .

"""

# Função para processar os dados simples no formato chave=valor
def processar_dados_simples(dados_input):
    dados = {}
    for linha in dados_input.split("\n"):
        if "=" in linha:
            chave, valor = linha.split("=", 1)
            dados[chave.strip()] = valor.strip()
    return dados

# Função para preencher os placeholders no texto
def preencher_texto(texto, dados):
    for campo, valor in dados.items():
        texto = texto.replace(f"{{{{{campo}}}}}", valor)
    return texto

# Configuração da página
st.set_page_config(page_title="Projeto Galaxy", layout="wide")

# Inicializar sessão para armazenar dados e texto
if "dados_inicial" not in st.session_state:
    st.session_state["dados_inicial"] = {}
if "dados_contestacao" not in st.session_state:
    st.session_state["dados_contestacao"] = {}
if "texto_gerado" not in st.session_state:
    st.session_state["texto_gerado"] = texto_base

# Divisão em abas
tab1, tab2 = st.tabs(["📄 Formulário de Preenchimento", "📝 Texto Gerado"])

# Aba 1 - Formulário de preenchimento
with tab1:
    st.subheader("Preencha os dados para personalizar o texto:")
    
    # Campo para inserir os dados no formato chave=valor
    dados_input = st.text_area(
        "Dados (chave=valor)",
        placeholder="Insira os dados no formato:\nprocesso=0010027-31.2024.5.18.0016\nnome_autor=JAIME COSTA E SOUZA\nnome_reus=LINE EXPRESS TRANSPORTES E DISTRIBUIÇÃO LTDA\ngenero_autor=o\ngenero_reu=a",
        height=200
    )
    
    # Campos para colar os dados JSON
    dados_inicial_input = st.text_area(
        "Dados JSON da Inicial",
        placeholder="Cole aqui o JSON da Inicial...",
        height=150
    )
    dados_contestacao_input = st.text_area(
        "Dados JSON da Contestação",
        placeholder="Cole aqui o JSON da Contestação...",
        height=150
    )
    
    # Botão para processar os dados
    if st.button("Gerar Texto"):
        try:
            # Processar os dados fornecidos
            dados = processar_dados_simples(dados_input)
            
            # Preencher o texto com os dados processados
            st.session_state["texto_gerado"] = preencher_texto(texto_base, dados)
            
            # Processar os JSONs da inicial e contestação
            st.session_state["dados_inicial"] = json.loads(dados_inicial_input)
            st.session_state["dados_contestacao"] = json.loads(dados_contestacao_input)

            st.success("Texto gerado com sucesso! Vá para a aba 'Texto Gerado'.")
        except json.JSONDecodeError:
            st.error("Erro ao processar os dados JSON. Verifique o formato.")
        except Exception as e:
            st.error(f"Erro ao processar os dados: {e}")

# Aba 2 - Texto gerado
with tab2:
    # Ajuste de proporção das colunas
    col1, col2, col3 = st.columns([1, 1, 3])

    with col1:
        st.subheader("Títulos da Inicial")
        titulos_inicial = st.session_state["dados_inicial"].get("titulos", [])
        st.text_area("Todos os Títulos da Inicial", "\n".join(titulos_inicial), height=150)

        st.subheader("Pedidos da Inicial")
        pedidos_inicial = st.session_state["dados_inicial"].get("pedidos", "")
        st.text_area("Pedidos da Inicial", pedidos_inicial, height=100)

        st.subheader("Resumos da Inicial")
        resumos_inicial = st.session_state["dados_inicial"].get("resumos", [])
        for i in range(min(10, len(resumos_inicial))):
            st.text_area(f"Resumo {i+1} - Inicial", resumos_inicial[i], height=100)

    with col2:
        st.subheader("Títulos da Contestação")
        titulos_contestacao = st.session_state["dados_contestacao"].get("titulos", [])
        st.text_area("Todos os Títulos da Contestação", "\n".join(titulos_contestacao), height=150)

        st.subheader("Preliminares e Prejudiciais da Contestação")
        preliminares_contestacao = st.session_state["dados_contestacao"].get("preliminares", [])
        st.text_area("Preliminares e Prejudiciais da Contestação", value="\n".join(preliminares_contestacao), height=100)

        st.subheader("Resumos da Contestação")
        resumos_contestacao = st.session_state["dados_contestacao"].get("resumos", [])
        for i in range(min(10, len(resumos_contestacao))):
            st.text_area(f"Resumo {i+1} - Contestação", resumos_contestacao[i], height=100)

    with col3:
        st.subheader("Editor de Texto")
        texto_editado = st.text_area("Texto Editado", st.session_state["texto_gerado"], height=600)

        # Botão para salvar o texto no editor
        if st.button("Salvar Alterações"):
            st.session_state["texto_gerado"] = texto_editado
            st.success("Alterações salvas com sucesso!")

        # Botão para baixar o texto em formato .txt
        st.download_button(
            label="Baixar como .txt",
            data=st.session_state["texto_gerado"],
            file_name="texto_gerado.txt",
            mime="text/plain",
        )

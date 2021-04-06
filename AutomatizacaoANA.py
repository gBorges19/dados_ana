import requests
from xml.etree import ElementTree
import numpy
from numpy import genfromtxt

EscolhaPrograma = input("Digite P para pesquisar conteúdos de estações específicas ou Digite D para fazer donwload de estações: ")

if (EscolhaPrograma == 'P'):
    
    localarq = input("Digite o local em que o arquivo se encontra: ")
    nomearq = input("Digite o nome do arquivo que deseja visualizar: ")
    my_data = genfromtxt(""+localarq+"/"+nomearq+".csv",delimiter=";",dtype=None,encoding='UTF8')
    DataHora = 'NULL'
    dadosEstacao = []

    while DataHora != 'EXIT':
        DataHora = input("Digite a data e horario que quer visualizar no formato YYYY-MM-DD HH-MM-SS : ")

        for line in my_data:
            if(DataHora==line[1]):
                print(line)
                dadosEstacao.append(line)
                
    numpy.savetxt("resultadoteste.csv", dadosEstacao, fmt = '%s',delimiter= ';')
    
else:
    
    EscolhaEstacao = input("Digite a sigla do estado que deseja fazer download em letra maiúscula: ")

    if(EscolhaEstacao == 'MS'):
        estacoesArray = ['60959500', '60968000', '63000050', '63000100', '63001080', '63001100', '63001117', '63001120', '63001125', '63001130', '63001223', '63001225', '63001228', '63001230', '63001260', '63001263',
        '63001265', '63001550', '63001560', '63001580', '63001602', '63001603', '63001605', '63001608', '63001635', '63001638', '63001642', '63001650', '63001670', '63001675', '63001680', '63001740',
        '63003200', '63250700', '63250800', '63250850', '63250880', '63250900', '63250910', '63250950', '63257000', '63259000', '63260000', '63270000', '63400000', '63850000', '63905000', '63910000',
        '63920080', '63921000', '63968000', '63970000', '64618500', '64725000', '66483600', '66483800', '66484000', '66484500', '66493900', '66494000', '66810000', '66825000', '66859000', '66861000',
        '66870000', '66900000', '66910000', '66941000', '66945000', '66960008', '67100000']
   
    if(EscolhaEstacao == 'PR'):
        estacoesArray = ['02251081','02351080','02449067','02450009','02548079','02548098','02551015','02551063','02551069','02551070','02551071','02551072','02552009',
        '02552030','02552055','64230200','64230230','64230250','64230300','64230350','64230400','64230450','64230500','64231000','64234000','64240000',
        '64240100','64240150','64240200','64241200','64241300','64241400','64241500','64242000','64247000','64360000','64362001','64370000','64390000',
        '64441020','64444000','64450001','64452190','64461000','64464995','64469850','64474800','64477000','64478100','64478150','64480995','64482000',
        '64489000','64490800','64491000','64494000','64497000','64497010','64501000','64504210','64506000','64507000','64508500','64515920','64516080',
        '64541000','64545840','64545860','64546900','64547500','64547600','64560000','64565500','64575000','64575001','64630050','64630100','64630500',
        '64630600','64631800','64632000','64633000','64633050','64638000','64670005','64670011','64671500','64671600','64672050','64672100','64675002',
        '64682000','64767000','64773500','64773750','64773880','64773890','64785000','64815000','64831000','64833000','64838000','64849000','64850050',
        '64850100','64850150','64863100','64864100','64864150','64864200','64892500','64899500','64902080','64918000','65004995','65006090','65010000',
        '65015400','65017006','65025000','65026950','65028000','65035001','65060001','65100001','65136550','65140000','65141000','65155001','65175001',
        '65220001','65310001','65365801','65370001','65764001','65774400','65775901','65803001','65808500','65808900','65809000','65812000','65813100',
        '65815040','65815050','65819300','65824991','65825497','65826612','65826720','65831000','65831020','65831900','65832000','65854500','65855080',
        '65855110','65875500','65883051','65889700','65894991','65927001','65945200','65945400','65945500','65945600','65948000','65950200','65954200',
        '65954250','65954300','65954400','65954900','65954950','65955000','65956000','65958000','65960001','65962000','65963071','65970001','65973501',
        '65975300','65980500','65981500','65983100','65984000','65987000','65987001','65992500','65992502','81018900','81019000','81019350','81028000',
        '81030000','81107000','81135000','81139500','81299001','81301001','81303001','81312000','81315000','82002000','82065000','82121002','82188000',
        '82230001','82230015','82230815','82234000']
    
    dataInicio = input("Digite a Data de Inicio no formato YYYY-MM-DD : ")
    dataFim = input("Digite a Data Final no formato YYYY-MM-DD : ")
    Local = input("Digite o Local em que o arquivo será baixado, como D:/Dados/PR por exemplo: ")

    for estacao in estacoesArray:
        codEstacao = estacao
        url = "http://telemetriaws1.ana.gov.br/ServiceANA.asmx/DadosHidrometeorologicos?codEstacao="+codEstacao+"&dataInicio="+dataInicio+"&dataFim="+dataFim
        response = requests.get(url)

        t = ElementTree.fromstring(response.content)
        x = t[1]
        documentElement = x[0]

        tableArray=[]
        attribArray_lineOfTable = []

        for child in documentElement:
            attribArray_lineOfTable = []
            for attrib in child:
                if (len(tableArray) == 0):
                    attribArray_lineOfTable.append(attrib.tag)
                else:
                    attribArray_lineOfTable.append(attrib.text)
            tableArray.append(attribArray_lineOfTable)

        print('Creating csv')
        numpy.savetxt(""+Local+"/DadosEstacao_"+codEstacao+"_"+dataInicio+"_"+dataFim+".csv", tableArray, fmt = '%s',delimiter= ';')
        print('Csv created')
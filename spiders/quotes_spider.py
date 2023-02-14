from pathlib import Path

import scrapy
import re



class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        base_url = 'https://pubmed.ncbi.nlm.nih.gov/?term='
        plus = '%2B'
        page_size = '&size=200'
        urls = [
            # 'https://pubmed.ncbi.nlm.nih.gov/?term=RNAseq%2Bgenewiz',
            # 'https://pubmed.ncbi.nlm.nih.gov/?term=RNAseq%2Bgenewiz&size=200',
            # 'https://pubmed.ncbi.nlm.nih.gov/?term=RNAseq%2Bgenewiz&size=200',
        ]
        # key_words = ['Abbott']
        key_words = ['Abbott',
                    'Acepodia',
                    'AgeX+Therapeutics',
                    'AllCells',
                    'Alveo+Technologies',
                    'Emery+Pharma',
                    'Exelixis',
                    'Fluxion+Biosciences',
                    'iota+Biosciences',
                    'Magnetic+Insight',
                    'Penumbra',
                    'Resilience',
                    'Scribe+Therapeutics',
                    'Miltenyi+Biotec',
                    'JGB+BioPharma+Consulting',
                    'Acrigen+Biosciences',
                    'Actym+Therapeutics',
                    'C.Light+Technologies',
                    'Caribou+Biosciences',
                    'CellFE',
                    'Chameleon+Biosciences',
                    'Channel+Medsystems',
                    'Coagulant+Therapeutics',
                    'Correlia+Biosystems',
                    'Demetrix',
                    'Equator+Therapeutics',
                    'Flightpath+Biosciences',
                    'ImmunoMind',
                    'Indee+Labs',
                    'Integrated+Analytical+Solutions',
                    'InterX',
                    'iQ+Biosciences',
                    'Kimia+Therapeutics',
                    'Kyverna+Therapeutics',
                    'Lygos',
                    'Machaon+Diagnostics',
                    'Nanotein',
                    'Newomics',
                    'Quintara+Bio',
                    'ResVita+Bio',
                    'Solaris+Biotech',
                    'SonALAsense',
                    'Synvivia',
                    'Valitor',
                    'YourChoice+Therapeutics',
                    'Aimmune+Therapeutics',
                    'Annexon+Biosciences',
                    'Antiva+Biosciences',
                    'Cureline',
                    'Delpor',
                    'MacroGenics',
                    'Mammoth+Biosciences',
                    'Myovant+Sciences',
                    'NephroSant',
                    'Nitrase+Therapeutics',
                    'Razor+Genomics',
                    'Second+Genome',
                    'Ultragenyx+Pharmaceutical',
                    'Vera+Therapeutics',
                    'YenZym+Antibodies',
                    'Cala+Health',
                    'Collaborative+Drug+Discovery',
                    'Color',
                    'Confidence+Pharmaceutical+Research',
                    'Corvus+Pharmaceuticals',
                    'Excel+BioPharm',
                    'Genesis+Therapeutics',
                    'Halo+Labs',
                    'Hinge+Bio',
                    'Humanigen',
                    'Inflammatix',
                    'Magnus+Medical',
                    'Phoenix+Pharmaceuticals',
                    'Protein+Fluidics',
                    'Protillion+Biosciences',
                    'Radimmune+Therapeutics',
                    'SciBac',
                    'Tallac+Therapeutics',
                    'Adona+Medical',
                    'Atia+Vision',
                    'CardioDiagnostics',
                    'Imperative+Care',
                    'List+Biological+Laboratories',
                    'Precise+Light+Surgical',
                    'Saama+Technologies',
                    'Truvic+Medical',
                    'VIVUS',
                    'Cerus',
                    'Element',
                    'Heraeus+Medical',
                    'MedAutonomic',
                    'Durect',
                    'MindRhythm',
                    'Protein+Metrics',
                    'PyrAmes',
                    'Reviva+Pharmaceuticals',
                    'Spruce+Biosciences',
                    'BryoLogyx',
                    'Antibodies+Incorporated',
                    'ARIZ+Precision+Medicine',
                    'Aves+Labs',
                    'Cell+Technology',
                    'EicOsis',
                    'EXPRESSION+SYSTEMS',
                    'Infinant+Health',
                    'Novozymes',
                    'Ravata+Solutions',
                    'Azee+Pharmaceuticals',
                    'Carl+Zeiss+Meditec',
                    'Ampac+Analytical',
                    'Consensus+Orthopedics',
                    'eMed+Technologies',
                    '4D+Molecular+Therapeutics',
                    'Abalone+Bio',
                    'Ansa+Biotechnologies',
                    'BeiGene',
                    'Berkeley+Lights',
                    'BiosPacific',
                    'Dynavax+Technologies',
                    'Estrella+Biopharma',
                    'Eureka+Therapeutics',
                    'Fauna+Bio',
                    'Gritstone+Bio',
                    'InjectSense',
                    'Kite+Pharma',
                    'Lucira+Health',
                    'Metagenomi',
                    'Milagen',
                    'Nanomix',
                    'NovaBay+Pharmaceuticals',
                    'Novartis',
                    'Nutcracker+Therapeutics',
                    'Octant+Biotech',
                    'OmniAb',
                    'Profusa',
                    'Radiance+Therapeutics',
                    'Santen',
                    'Slingshot+Biosciences',
                    'Totus+Medicines',
                    'Vivani+Medical',
                    'Vivani+Medical',
                    'Agilent',
                    'Apollomics',
                    'Asegua+Therapeutics',
                    'Cartography+Biosciences',
                    'Dren+Bio',
                    'Geron',
                    'Gilead',
                    'MedGenome',
                    'MicuRx+Pharmaceuticals',
                    'Mirum+Pharmaceuticals',
                    'Notable+Labs',
                    'Pointcross+Life+Sciences',
                    'TeraRecon',
                    'Terns+Pharmaceuticals',
                    'TrueBinding',
                    'Abcam',
                    'Alamar+Biosciences',
                    'AlterG',
                    'AnaSpec',
                    'AngioDynamics',
                    'Applied+Viromics',
                    'APstem+Therapeutics',
                    'Arbor+Vita',
                    'Ardelyx',
                    'Ark+Diagnostics',
                    'Assay+Biotechnology',
                    'Atonarp',
                    'BioGenex',
                    'Bionova+Scientific',
                    'Biotium',
                    'Boehringer+Ingelheim',
                    'Cerus+Endovascular',
                    'Clip+Health',
                    'CoaguSense',
                    'Confluent+Medical+Technologies',
                    'Cytek+Biosciences',
                    'Devoro+Medical',
                    'Ellex',
                    'eLum+Technologies',
                    'Encoll',
                    'Intuity+Medical',
                    'iovera',
                    'Moximed',
                    'Neodyne+Biosciences',
                    'NeuralInk',
                    'Novo+Nordisk',
                    'PrinterPrezz',
                    'QApel+Medical',
                    'Thermo+Fisher',
                    'THINK+Surgical',
                    'Verseon',
                    'Viant+Medical',
                    'Limb+Preservation+Platform',
                    'Biosure',
                    'AltiBio',
                    'Axcess+Surgical',
                    'Potrero+Hill+Therapeutics',
                    'Aarvik+Therapeutics',
                    'Ab+Studio',
                    'AcelRx+Pharmaceuticals',
                    'Acepix+Biosciences',
                    'Applied+Biomics',
                    'Arcus+Biosciences',
                    'Avirmax',
                    'Benitec+Biopharma',
                    'BioAssay+Systems',
                    'Biolog',
                    'Eikon+Therapeutics',
                    'Elim+Biopharm',
                    'Frontage',
                    'Illumina',
                    'Intarcia+Therapeutics',
                    'Mawi+DNA+Technologies',
                    'Meadowhawk+Biolabs',
                    'Multispan,Inc.',
                    'Nodexus',
                    'Novodiax',
                    'Paragon+Genomics',
                    'Pharmatech+Associates',
                    'Planet+Biotechnology',
                    'Potrero+Medical',
                    'Predicine',
                    'Pulse+Biosciences',
                    'Quartzy',
                    'Quintara+Bio',
                    'Quintara+Discovery',
                    'RefleXion+Medical',
                    'Spotlight+Therapeutics',
                    'Virovek',
                    'Bio-Rad',
                    'Pacific+BioLabs',
                    'Charles+River+Laboratories',
                    'Teknova',
                    'Aulos+Bioscience',
                    'Advanced+Bifurcation+Systems',
                    'Florica+Therapeutics',
                    'S2+Genomics',
                    'Alto+Neuroscience',
                    'Efemoral+Medical',
                    'Evommune',
                    'Fist+Assist+Devices',
                    'Globavir+Biosciences',
                    'LifeWave+Biomedical',
                    'Quadriga+BioSciences',
                    'QView+Medical',
                    'RenovoRx',
                    'Retrotope+Pharmaceuticals',
                    'Unicycive+Therapeutics',
                    'Univfy',
                    'UroViu',
                    'Advanced+NanoTherapies',
                    'Aridis+Pharmaceuticals',
                    'Cirtec+Medical',
                    'Livionex+Pharma',
                    'ProTrials+Research',
                    'Supira+Medical',
                    'Tenon+Medical',
                    'Tioga+Medical',
                    'Xoc+Pharmaceuticals',
                    'ExThera+Medical',
                    '180+Life+Sciences',
                    'Abbott',
                    'Abram+Scientific',
                    'Adicet+Bio',
                    'AEGEA+Medical',
                    'Aether+Biomachines',
                    'Akoya+Biosciences',
                    'Alion+Pharmaceuticals',
                    'Alladapt+Immunotherapeutics',
                    'Allay+Therapeutics',
                    'Aluda+Pharmaceuticals',
                    'AN2+Therapeutics',
                    'Antheia',
                    'Ariagen',
                    'Attune+Neurosciences',
                    'Augmenta+Bioworks',
                    'Avellino+Laboratories',
                    'BillionToOne',
                    'Biotrace+Medical',
                    'CelerisTx',
                    'Clinuvel+Pharmaceuticals',
                    'CohBar',
                    'Corcept+Therapeutics',
                    'Corium',
                    'Credence+MedSystems',
                    'CS+Bio',
                    'Doloromics',
                    'Drawbridge+Health',
                    'Eclipse+Regenesis',
                    'Edison+Oncology',
                    'Emmecell',
                    'Enable+Medicine',
                    'Endovascular+Engineering',
                    'Escend+Pharmaceuticals',
                    'Farapulse',
                    'Gamma+Biosciences',
                    'Grace+Science',
                    'GRAIL',
                    'Hexagon+Bio',
                    'iNanoBio',
                    'Intersect+ENT',
                    'Ionpath',
                    'iSchemaView',
                    'Kintara+Therapeutics',
                    'Levita+Magnetics',
                    'LevitasBio',
                    'Medikine',
                    'Octave+Bioscience',
                    'Olive+Diagnostics',
                    'Orca+Bio',
                    'Pacific+Biosciences',
                    'Personalis',
                    'PharmatrophiX',
                    'Phathom+Pharmaceuticals']
        for key_word in key_words:
            url = base_url + key_word + plus + 'Cellranger' + page_size
            urls.append(url)

        for url in urls:
            for i in range(1, 2):
                for j in range(2022, 2024):
                    url1 = url + "&filter=years."+str(j)+"-"+str(j)    
                    url2 = url1 + "&page=" + str(i)
                    yield scrapy.Request(url=url2, callback=self.parse)

    def parse(self, response):
        # href = response.xpath("//*[@id='search-results']/section/div[1]/div/article[2]/div[2]/div[1]/a/@href").extract()[0]
        href_list = response.xpath("//*[@id='search-results']/section/div[1]/div/article/div[2]/div[1]/a/@href")
        if len(href_list) > 0:
            for href_name in href_list:
                root = href_name.root
                href_link = "https://pubmed.ncbi.nlm.nih.gov" + root
                yield scrapy.Request(
                    url=href_link,
                    callback=self.parse_email,
                )
         
    
    def parse_email(self, response):
        email=re.compile(r'[a-z0-9\-\.]+@[0-9a-z\-\.]+')
        title = response.xpath("//*[@class='heading-title']/text()").extract()[0].rstrip().lstrip()
        affiliation_list = response.xpath("//*[@id='full-view-expanded-authors']/div/ul/li/text()")
        #affiliation_list_content = response.xpath("//*[@id='full-view-expanded-authors']/div/ul/li/text()").extract()
        # for affiliation in affiliation_list:
            # affiliation_content = affiliation.root
        # author_name = response.xpath("//*[@class='authors-list']/span/a/text()").extract()
        
        # yield {
        #     "title": title,
        #     "affiliation_list": affiliation_list_content
        # }
        author_email_map = dict()
        author_item = response.xpath("//*[@class='authors-list-item ']")
        for item in author_item:
            author = item.xpath("a/text()").extract()[0]
            affiliationSupList = item.xpath("sup/a/@title").extract()
            if len(affiliationSupList) > 0:
                affiliation = item.xpath("sup/a/@title").extract()[0]
                #emailSet=set()
                emailList = email.findall(affiliation)
                if len(emailList) > 0:
                    em = emailList[0]
                    char = em[-1]
                    if (char == "."):
                        em = em[0: -1]
                    author_email_map["author"] = author
                    author_email_map["email"] = em

        if len(author_email_map) > 0:
            yield {
                "title": title,
                "author": author_email_map,
                "url(Click url to access page)": response.url,
            }
        # else:
        #     author_email_map["author"] = ""
        #     author_email_map["email"] = "can't find any email in this page"
        #     yield {
        #         "title": title,
        #         "author": author_email_map,
        #         "url(Click url to access page)": response.url,
        #     }

    def emailre(testStr):
        email=re.compile(r'([a-zA-Z0-9_.+-]+@[a-pr-zA-PRZ0-9-]+\.[a-zA-Z0-9-.]+)')
        emailset=set()  #列表
        for em in email.findall(testStr):
            emailset.add(em)
        return emailset
    
    def removeDot(emailStr):
        char = emailStr[-1]
        if char == ".":
            return emailStr[0: -1]
        else:
            return emailStr
from io import StringIO
from unittest import TestCase

from abstract_extractor import AbstractExtractor


class TestAbstractExtractor(TestCase):
    def test___call__(self):
        # Arrange
        sut = AbstractExtractor()
        handle = StringIO(self.get_text_xml_data())
        expected = [
            {"pubmed_id": "30516273",
             "article_title": "Temporal clustering of extreme climate events drives a regime shift in rocky intertidal biofilms.",
             "article_abstract": "Research on regime shifts has focused primarily on how changes in the intensity and duration of press disturbances precipitate natural systems into undesirable, alternative states. By contrast, the role of recurrent pulse perturbations, such as extreme climatic events, has been largely neglected, hindering our understanding of how historical processes regulate the onset of a regime shift. We performed field manipulations to evaluate whether combinations of extreme events of temperature and sediment deposition that differed in their degree of temporal clustering generated alternative states in rocky intertidal epilithic microphytobenthos (biofilms) on rocky shores. The likelihood of biofilms to shift from a vegetated to a bare state depended on the degree of temporal clustering of events, with biofilm biomass showing both states under a regime of non-clustered (60 days apart) perturbations while collapsing in the clustered (15 days apart) scenario. Our results indicate that time since the last perturbation can be an important predictor of collapse in systems exhibiting alternative states and that consideration of historical effects in studies of regime shifts may largely improve our understanding of ecosystem dynamics under climate change. This article is protected by copyright. All rights reserved.",
             "pub_date": {
                 "year": "2018",
                 "month": "Dec",
                 "day": "05"
             }
             },
            {"pubmed_id": "30516274",
             "article_title": "Multiple drivers of contrasting diversity-invasibility relationships at fine spatial grains.",
             "article_abstract": "The diversity-invasibility hypothesis and ecological theory predict that high-diversity communities should be less easily invaded than species-poor communities, but empirical evidence does not consistently support this prediction. While fine-scale experiments tend to yield the predicted negative association between diversity and invasibility, broad-scale observational surveys generally report a positive correlation. This conflicting pattern between experiments and observational studies is referred to as the invasion paradox, and is thought to arise because different processes control species composition at different spatial scales. Here, we test empirically the extent to which the strength and direction of published diversity-invasibility relationships depend on spatial scale and on the metrics used to measure invasibility. Using a meta-analytic framework, we explicitly separate the two components of spatial scale: grain and extent, by focusing on fine-grain studies that vary in extent. We find evidence of multiple drivers of the paradox. When we consider only fine-grain studies, we still observe conflicting patterns between experiments and observational studies. In contrast, when we examine studies that are conducted at both a fine grain and fine extent, there is broad overlap in effect sizes between experiments and observation, suggesting that comparing studies with similar extents resolves the paradox at local scales. However, we uncover systematic differences in the metrics used to measure invasibility between experiments, which use predominantly invader performance, and observational studies, which use mainly invader richness. When we consider studies with the same metric (i.e., invader performance), the contrasting associations between study types also disappears. It is not possible, at present, to fully disentangle the effect of spatial extent and metric on the paradox because both variables are systematically associated in different directions with study type. There is therefore an urgent need to conduct experiments and observational studies that incorporate the full range of variability in spatial extent and invasibility metric. This article is protected by copyright. All rights reserved.",
             "pub_date": {
                 "year": "2018",
                 "month": "Dec",
                 "day": "05"
             }
             }
        ]

        # Act
        actual = sut(handle)

        # Assert
        self.assertEqual(actual, expected)

    def test_dump(self):
        # Arrange
        sut = AbstractExtractor()
        handle = StringIO(self.get_text_xml_data())
        out_handle = StringIO()

        # Act
        sut.dump(handle, out_handle)

        # Assert
        self.assertTrue(len(out_handle.getvalue()) > 100, "The output handle must have atleast some data written to it")

    def get_text_xml_data(self):
        xml_str = '''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE PubmedArticleSet SYSTEM "http://dtd.nlm.nih.gov/ncbi/pubmed/out/pubmed_190101.dtd">
       <PubmedArticleSet>
        <PubmedArticle>
    <MedlineCitation Status="Publisher" Owner="NLM">
      <PMID Version="1">30516273</PMID>
      <DateRevised>
        <Year>2018</Year>
        <Month>12</Month>
        <Day>05</Day>
      </DateRevised>
      <Article PubModel="Print-Electronic">
        <Journal>
          <ISSN IssnType="Print">0012-9658</ISSN>
          <JournalIssue CitedMedium="Print">
            <PubDate>
              <Year>2018</Year>
              <Month>Dec</Month>
              <Day>05</Day>
            </PubDate>
          </JournalIssue>
          <Title>Ecology</Title>
          <ISOAbbreviation>Ecology</ISOAbbreviation>
        </Journal>
        <ArticleTitle>Temporal clustering of extreme climate events drives a regime shift in rocky intertidal biofilms.</ArticleTitle>
        <ELocationID EIdType="doi" ValidYN="Y">10.1002/ecy.2578</ELocationID>
        <Abstract>
          <AbstractText>Research on regime shifts has focused primarily on how changes in the intensity and duration of press disturbances precipitate natural systems into undesirable, alternative states. By contrast, the role of recurrent pulse perturbations, such as extreme climatic events, has been largely neglected, hindering our understanding of how historical processes regulate the onset of a regime shift. We performed field manipulations to evaluate whether combinations of extreme events of temperature and sediment deposition that differed in their degree of temporal clustering generated alternative states in rocky intertidal epilithic microphytobenthos (biofilms) on rocky shores. The likelihood of biofilms to shift from a vegetated to a bare state depended on the degree of temporal clustering of events, with biofilm biomass showing both states under a regime of non-clustered (60 days apart) perturbations while collapsing in the clustered (15 days apart) scenario. Our results indicate that time since the last perturbation can be an important predictor of collapse in systems exhibiting alternative states and that consideration of historical effects in studies of regime shifts may largely improve our understanding of ecosystem dynamics under climate change. This article is protected by copyright. All rights reserved.</AbstractText>
          <CopyrightInformation>This article is protected by copyright. All rights reserved.</CopyrightInformation>
        </Abstract>
        <AuthorList CompleteYN="Y">
          <Author ValidYN="Y">
            <LastName>Dal Bello</LastName>
            <ForeName>Martina</ForeName>
            <Initials>M</Initials>
            <AffiliationInfo>
              <Affiliation>Department of Biology, University of Pisa, CoNISMa, Via Derna 1, Pisa, Italy.</Affiliation>
            </AffiliationInfo>
          </Author>
          <Author ValidYN="Y">
            <LastName>Rindi</LastName>
            <ForeName>Luca</ForeName>
            <Initials>L</Initials>
            <AffiliationInfo>
              <Affiliation>Department of Biology, University of Pisa, CoNISMa, Via Derna 1, Pisa, Italy.</Affiliation>
            </AffiliationInfo>
          </Author>
          <Author ValidYN="Y">
            <LastName>Benedetti-Cecchi</LastName>
            <ForeName>Lisandro</ForeName>
            <Initials>L</Initials>
            <AffiliationInfo>
              <Affiliation>Department of Biology, University of Pisa, CoNISMa, Via Derna 1, Pisa, Italy.</Affiliation>
            </AffiliationInfo>
          </Author>
        </AuthorList>
        <Language>eng</Language>
        <PublicationTypeList>
          <PublicationType UI="D016428">Journal Article</PublicationType>
        </PublicationTypeList>
        <ArticleDate DateType="Electronic">
          <Year>2018</Year>
          <Month>12</Month>
          <Day>05</Day>
        </ArticleDate>
      </Article>
      <MedlineJournalInfo>
        <Country>United States</Country>
        <MedlineTA>Ecology</MedlineTA>
        <NlmUniqueID>0043541</NlmUniqueID>
        <ISSNLinking>0012-9658</ISSNLinking>
      </MedlineJournalInfo>
      <KeywordList Owner="NOTNLM">
        <Keyword MajorTopicYN="N">abrupt changes</Keyword>
        <Keyword MajorTopicYN="N">alternative states</Keyword>
        <Keyword MajorTopicYN="N">biofilm</Keyword>
        <Keyword MajorTopicYN="N">climate change</Keyword>
        <Keyword MajorTopicYN="N">epilithic microphytobenthos</Keyword>
        <Keyword MajorTopicYN="N">extreme events</Keyword>
        <Keyword MajorTopicYN="N">regime shift</Keyword>
        <Keyword MajorTopicYN="N">temporal clustering</Keyword>
      </KeywordList>
    </MedlineCitation>
    <PubmedData>
      <History>
        <PubMedPubDate PubStatus="entrez">
          <Year>2018</Year>
          <Month>12</Month>
          <Day>6</Day>
          <Hour>6</Hour>
          <Minute>0</Minute>
        </PubMedPubDate>
        <PubMedPubDate PubStatus="pubmed">
          <Year>2018</Year>
          <Month>12</Month>
          <Day>6</Day>
          <Hour>6</Hour>
          <Minute>0</Minute>
        </PubMedPubDate>
        <PubMedPubDate PubStatus="medline">
          <Year>2018</Year>
          <Month>12</Month>
          <Day>6</Day>
          <Hour>6</Hour>
          <Minute>0</Minute>
        </PubMedPubDate>
      </History>
      <PublicationStatus>aheadofprint</PublicationStatus>
      <ArticleIdList>
        <ArticleId IdType="pubmed">30516273</ArticleId>
        <ArticleId IdType="doi">10.1002/ecy.2578</ArticleId>
      </ArticleIdList>
    </PubmedData>
  </PubmedArticle>
  <PubmedArticle>
    <MedlineCitation Status="Publisher" Owner="NLM">
      <PMID Version="1">30516274</PMID>
      <DateRevised>
        <Year>2018</Year>
        <Month>12</Month>
        <Day>05</Day>
      </DateRevised>
      <Article PubModel="Print-Electronic">
        <Journal>
          <ISSN IssnType="Print">0012-9658</ISSN>
          <JournalIssue CitedMedium="Print">
            <PubDate>
              <Year>2018</Year>
              <Month>Dec</Month>
              <Day>05</Day>
            </PubDate>
          </JournalIssue>
          <Title>Ecology</Title>
          <ISOAbbreviation>Ecology</ISOAbbreviation>
        </Journal>
        <ArticleTitle>Multiple drivers of contrasting diversity-invasibility relationships at fine spatial grains.</ArticleTitle>
        <ELocationID EIdType="doi" ValidYN="Y">10.1002/ecy.2573</ELocationID>
        <Abstract>
          <AbstractText>The diversity-invasibility hypothesis and ecological theory predict that high-diversity communities should be less easily invaded than species-poor communities, but empirical evidence does not consistently support this prediction. While fine-scale experiments tend to yield the predicted negative association between diversity and invasibility, broad-scale observational surveys generally report a positive correlation. This conflicting pattern between experiments and observational studies is referred to as the invasion paradox, and is thought to arise because different processes control species composition at different spatial scales. Here, we test empirically the extent to which the strength and direction of published diversity-invasibility relationships depend on spatial scale and on the metrics used to measure invasibility. Using a meta-analytic framework, we explicitly separate the two components of spatial scale: grain and extent, by focusing on fine-grain studies that vary in extent. We find evidence of multiple drivers of the paradox. When we consider only fine-grain studies, we still observe conflicting patterns between experiments and observational studies. In contrast, when we examine studies that are conducted at both a fine grain and fine extent, there is broad overlap in effect sizes between experiments and observation, suggesting that comparing studies with similar extents resolves the paradox at local scales. However, we uncover systematic differences in the metrics used to measure invasibility between experiments, which use predominantly invader performance, and observational studies, which use mainly invader richness. When we consider studies with the same metric (i.e., invader performance), the contrasting associations between study types also disappears. It is not possible, at present, to fully disentangle the effect of spatial extent and metric on the paradox because both variables are systematically associated in different directions with study type. There is therefore an urgent need to conduct experiments and observational studies that incorporate the full range of variability in spatial extent and invasibility metric. This article is protected by copyright. All rights reserved.</AbstractText>
          <CopyrightInformation>This article is protected by copyright. All rights reserved.</CopyrightInformation>
        </Abstract>
        <AuthorList CompleteYN="Y">
          <Author ValidYN="Y">
            <LastName>Smith</LastName>
            <ForeName>Nicola S</ForeName>
            <Initials>NS</Initials>
            <AffiliationInfo>
              <Affiliation>Earth to Oceans Research Group, Department of Biological Sciences, Simon Fraser University, Burnaby, BC, V5A 1S6, Canada.</Affiliation>
            </AffiliationInfo>
          </Author>
          <Author ValidYN="Y">
            <LastName>Côté</LastName>
            <ForeName>Isabelle M</ForeName>
            <Initials>IM</Initials>
            <AffiliationInfo>
              <Affiliation>Earth to Oceans Research Group, Department of Biological Sciences, Simon Fraser University, Burnaby, BC, V5A 1S6, Canada.</Affiliation>
            </AffiliationInfo>
          </Author>
        </AuthorList>
        <Language>eng</Language>
        <PublicationTypeList>
          <PublicationType UI="D016428">Journal Article</PublicationType>
        </PublicationTypeList>
        <ArticleDate DateType="Electronic">
          <Year>2018</Year>
          <Month>12</Month>
          <Day>05</Day>
        </ArticleDate>
      </Article>
      <MedlineJournalInfo>
        <Country>United States</Country>
        <MedlineTA>Ecology</MedlineTA>
        <NlmUniqueID>0043541</NlmUniqueID>
        <ISSNLinking>0012-9658</ISSNLinking>
      </MedlineJournalInfo>
      <KeywordList Owner="NOTNLM">
        <Keyword MajorTopicYN="N">biotic resistance</Keyword>
        <Keyword MajorTopicYN="N">diversity-invasibility hypothesis</Keyword>
        <Keyword MajorTopicYN="N">invasibility metrics</Keyword>
        <Keyword MajorTopicYN="N">invasion paradox</Keyword>
        <Keyword MajorTopicYN="N">invasion susceptibility</Keyword>
        <Keyword MajorTopicYN="N">meta-analysis</Keyword>
        <Keyword MajorTopicYN="N">spatial scale</Keyword>
        <Keyword MajorTopicYN="N">systematic review</Keyword>
      </KeywordList>
    </MedlineCitation>
    <PubmedData>
      <History>
        <PubMedPubDate PubStatus="entrez">
          <Year>2018</Year>
          <Month>12</Month>
          <Day>6</Day>
          <Hour>6</Hour>
          <Minute>0</Minute>
        </PubMedPubDate>
        <PubMedPubDate PubStatus="pubmed">
          <Year>2018</Year>
          <Month>12</Month>
          <Day>6</Day>
          <Hour>6</Hour>
          <Minute>0</Minute>
        </PubMedPubDate>
        <PubMedPubDate PubStatus="medline">
          <Year>2018</Year>
          <Month>12</Month>
          <Day>6</Day>
          <Hour>6</Hour>
          <Minute>0</Minute>
        </PubMedPubDate>
      </History>
      <PublicationStatus>aheadofprint</PublicationStatus>
      <ArticleIdList>
        <ArticleId IdType="pubmed">30516274</ArticleId>
        <ArticleId IdType="doi">10.1002/ecy.2573</ArticleId>
      </ArticleIdList>
    </PubmedData>
  </PubmedArticle>
  </PubmedArticleSet>'''
        return xml_str

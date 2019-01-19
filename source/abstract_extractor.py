import json
import logging
from xml.etree import ElementTree

"""
Extracts useful information from the Pubmed XML
"""


class AbstractExtractor:

    def __init__(self):
        self.namespaces = {}

    @property
    def logger(self):
        return logging.getLogger(__name__)

    def __call__(self, xml_handle):
        result = []
        for ele_article in self._iter_elements_by_name(xml_handle, "PubmedArticle", self.namespaces):
            title = ele_article.find("MedlineCitation/Article/ArticleTitle").text
            abstract = ele_article.find("MedlineCitation/Article/Abstract/AbstractText").text
            id = ele_article.find("MedlineCitation/PMID").text
            year = ele_article.find("MedlineCitation/Article/Journal/JournalIssue/PubDate/Year").text
            month = ele_article.find("MedlineCitation/Article/Journal/JournalIssue/PubDate/Month").text
            day = ele_article.find("MedlineCitation/Article/Journal/JournalIssue/PubDate/Day").text

            result.append({"pubmed_id": id,
                           "article_title": title,
                           "article_abstract": abstract,
                           "pub_date": {
                               "year": year,
                               "month": month,
                               "day": day
                           }})

        return result

    def dump(self, xml_handle, out_handle):
        result = self.__call__(xml_handle)
        out_handle.write(json.dumps(result))

    def dump_to_file(self, xml_handle, file_path):
        with open(file_path, "w") as handle:
            self.dump(xml_handle, handle)

    def _iter_elements_by_name(self, handle, name, namespace):
        events = ElementTree.iterparse(handle, events=("start", "end"))
        _, root = next(events)  # Grab the root element.

        expanded_name = name
        # If name has the namespace, expand it
        if name.find(":") >= 0:
            local_name = name[name.index(":") + 1:]
            namespace_short_name = name[:name.index(":")]
            expanded_name = "{{{}}}{}".format(namespace[namespace_short_name], local_name)

        for event, elem in events:

            if event == "end" and elem.tag == expanded_name:
                yield elem
                elem.clear()

"""Creates an arxiv document class and registers it as domain model

Returns:
    class: ArxivDocument class
"""

from webminer.interface_adapters.domain_model import DomainModel


class ArxivDocument(object):
    """Create an arxiv document

    Args:
        object (obj): Base object to be extended

    Returns:
        class: Transformed and extended document
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def from_dict(cls, feedparser_dict):
        """Checks the feedparser dictionary and returns it as a document

        Args:
            feedparser_dict (feedParserDict): Dictionary from parsing the feed

        Returns:
            class object: ArxivDocument object
        """

        pdf = ""
        for link in feedparser_dict["links"]:
            try:
                if link["title"] == "pdf":
                    pdf = link["href"]
            except AttributeError:
                pass

        document = ArxivDocument(
            doc_id=feedparser_dict["doc_id"],
            title=feedparser_dict["title"],
            abstract=feedparser_dict["summary"],
            authors=[auth["name"] for auth in feedparser_dict["authors"]],
            url=feedparser_dict["url"],
            publish_date=feedparser_dict["published"],
            pdf_url=pdf,
        )

        return document


DomainModel.register(ArxivDocument)

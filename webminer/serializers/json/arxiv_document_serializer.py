"""
Serializers allow complex data such as querysets and model instances to be converted
to native Python datatypes that can then be easily rendered into JSON
"""

import json


class ArxivDocEncoder(json.JSONEncoder):
    """Encodes the arxiv document

    Args:
        json (obj): The JSON encoded object

    Returns:
        dict: The serialized format
    """

    def default(self, o):  # pylint: disable=E0202
        try:
            to_serialize = {
                "id": o.doc_id,
                "url": o.url,
                "title": o.title,
                "abstract": o.abstract,
                "authors": ",".join(o.authors),
                "publish_date": o.publish_date,
                "pdf": o.pdf_url,
            }
            return to_serialize

        except AttributeError:
            return super().default(o)

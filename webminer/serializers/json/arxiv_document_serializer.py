import json

class ArxivDocEncoder(json.JSONEncoder):
    def default(self, o):
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

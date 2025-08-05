from langchain.text_splitter import MarkdownHeaderTextSplitter
import os


class TextSplitter():

    def __init__(self):
        print('TextSplitter => START')
        pass

    def resolve_path(self, path: str):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, path)
    
    def load_md_chunks(self, md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        lines = content.splitlines()
        splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "H1"), ("##", "H2"), ("###", "H3")])
        docs = [doc for doc in splitter.split_text(content) if doc.page_content.strip()]

        # 为每个块加上起始行号
        for doc in docs:
            chunk = doc.page_content.strip()
            start_line = None
            if chunk:
                for idx, line in enumerate(lines, 1):
                    if line.strip() and chunk.startswith(line.strip()):
                        start_line = idx
                        break
            doc.metadata["start_line"] = start_line
        return docs
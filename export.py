from io import BytesIO
from docx import Document

def save_markdown_report(report, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)

        from io import BytesIO
from docx import Document


def clean_markdown_formatting(text):
    return (
        text
        .replace("**", "")
        .replace("__", "")
        .replace("`", "")
    )

def convert_markdown_to_docx_bytes(markdown_text):
    doc = Document()

    for line in markdown_text.split("\n"):
        clean_line = clean_markdown_formatting(line.strip())

        if not clean_line:
            doc.add_paragraph()
            continue

        if clean_line.startswith("# "):
            doc.add_heading(clean_line.replace("# ", ""), level=1)

        elif clean_line.startswith("## "):
            doc.add_heading(clean_line.replace("## ", ""), level=2)

        elif clean_line.startswith("### "):
            doc.add_heading(clean_line.replace("### ", ""), level=3)

        elif clean_line.startswith("- "):
            doc.add_paragraph(clean_line.replace("- ", ""), style="List Bullet")

        elif clean_line.startswith("|"):
            doc.add_paragraph(clean_line)

        else:
            doc.add_paragraph(clean_line)

    file_stream = BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)

    return file_stream
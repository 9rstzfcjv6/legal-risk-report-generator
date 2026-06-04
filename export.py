def save_markdown_report(report, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(report)

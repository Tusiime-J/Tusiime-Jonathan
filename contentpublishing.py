# Main purpose: Demonstrates method overloading (Pythonic) and Method Resolution Order (MRO) in a content publishing system.

class BaseContent:
    def __init__(self, title):
        self.title = title

    def get_output_quality(self):
        return "Standard"

class TextFormatterMixin:
    def format_as_text(self, content_body):
        return f"--- {self.title.upper()} ---\n{content_body}\n--- End of Text ---"

    def get_output_quality(self):
        return "Basic"

class HTMLFormatterMixin:
    def format_as_html(self, content_body):
        return f"<h1>{self.title}</h1>\n<p>{content_body}</p>"

    def get_output_quality(self):
        return "WebOptimized"

class PDFFormatterMixin:
    def format_as_pdf(self, content_body):
        return f"%PDF-1.4\n<{self.title}>\n<body text='{content_body}'>\n"

    def get_output_quality(self):
        return "PrintReady"


class ContentPublisher:
    def publish(self, content_object, output_format="text", **options):
        print(f"\n--- Publishing '{content_object.title}' as {output_format.upper()} ---")
        if not isinstance(content_object, (TextFormatterMixin, HTMLFormatterMixin, PDFFormatterMixin)):
            print(f"Error: {type(content_object).__name__} does not support formatting.")
            return

        content_body = options.get('body', "No specific body provided.")

        if output_format == "text" and isinstance(content_object, TextFormatterMixin):
            print(content_object.format_as_text(content_body))
        elif output_format == "html" and isinstance(content_object, HTMLFormatterMixin):
            print(content_object.format_as_html(content_body))
        elif output_format == "pdf" and isinstance(content_object, PDFFormatterMixin):
            print(content_object.format_as_pdf(content_body))
        else:
            print(f"Unsupported format '{output_format}' or content type not suitable for this format.")

        print(f"Using output quality: {content_object.get_output_quality()}")

class BlogPost(HTMLFormatterMixin, TextFormatterMixin, BaseContent):
    pass

class PrintReport(PDFFormatterMixin, TextFormatterMixin, BaseContent):
    pass

article = BlogPost("My First Blog Post")
report = PrintReport("Quarterly Financial Report")

publisher = ContentPublisher()

publisher.publish(article, output_format="html", body="This is the article content for the web.")
publisher.publish(article, output_format="text", body="This is the article content for plain text.")

publisher.publish(report, output_format="pdf", body="Detailed financial data here.")
publisher.publish(report, output_format="text", body="Summary report for plain text.")

print("\n--- MRO for BlogPost ---")
print(BlogPost.__mro__)
print(f"Default quality for BlogPost: {article.get_output_quality()}")

print("\n--- MRO for PrintReport ---")
print(PrintReport.__mro__)
print(f"Default quality for PrintReport: {report.get_output_quality()}")
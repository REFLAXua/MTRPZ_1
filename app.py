import sys
import os
import markdown

def convert_markdown_to_html(input_path, output_path=None):
    if not os.path.isfile(input_path):
        print(f"error: file '{input_path}' does not exist", file=sys.stderr)
        sys.exit(1)

    try:
        with open(input_path, 'r') as file:
            markdown_content = file.read()
    except Exception as e:
        print(f"error with reading file '{input_path}': {e}", file=sys.stderr)
        sys.exit(1)

    try:
        html_content = markdown.markdown(markdown_content)
    except Exception as e:
        print(f"error: invalid markdown <{e}>", file=sys.stderr)
        sys.exit(1)

    if output_path:
        try:
            with open(output_path, 'w') as file:
                file.write(html_content)
        except Exception as e:
            print(f"Error writing to file '{output_path}': {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(html_content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Using: ./app /path/to/markdown [--out /path/to/output.html]", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = None

    if len(sys.argv) == 4 and sys.argv[2] == '--out':
        output_path = sys.argv[3]

    convert_markdown_to_html(input_path, output_path)

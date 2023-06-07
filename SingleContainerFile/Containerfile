FROM fedora:latest
RUN yum install python-pip -y
RUN pip3 install fpdf
RUN mkdir /temp

WORKDIR /app
RUN echo -e "from fpdf import FPDF\n\
import os\n\
import time\n\
import textwrap\n\
import filecmp\n\
\n\
INPUT_DIR = '/opt/incoming'\n\
OUTPUT_DIR = '/opt/outgoing'\n\
TEMP_DIR = '/temp'\n\
\n\
def text_to_pdf(in_file, out_file):\n\
    a4_width_mm = 210\n\
    pt_to_mm = 0.35\n\
    fontsize_pt = 10\n\
    fontsize_mm = fontsize_pt * pt_to_mm\n\
    margin_bottom_mm = 10\n\
    character_width_mm = 7 * pt_to_mm\n\
    width_text = a4_width_mm / character_width_mm\n\
\n\
    pdf = FPDF(orientation='P', unit='mm', format='A4')\n\
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)\n\
    pdf.add_page()\n\
    pdf.set_font(family='Courier', size=fontsize_pt)\n\
    with open(in_file) as file:\n\
        for line in file:\n\
            line = line[:-1]\n\
            lines = textwrap.wrap(line, width_text)\n\
            if len(lines) == 0:\n\
                pdf.ln()\n\
            for wrap in lines:\n\
                pdf.cell(0, fontsize_mm, wrap, ln=1)\n\
    pdf.output(out_file, 'F')\n\
\n\
while True:\n\
    try:\n\
        time.sleep(1)\n\
        input_files = os.listdir(INPUT_DIR)\n\
        output_files = [name.split('.')[0] for name in os.listdir(OUTPUT_DIR)]\n\
        for file in input_files:\n\
            if os.path.isfile(os.path.join(INPUT_DIR, file)):\n\
                in_file = file.split('.')[0]\n\
                in_path = os.path.join(INPUT_DIR, file)\n\
                out_path = os.path.join(OUTPUT_DIR, f'{in_file}.pdf')\n\
                if in_file not in output_files:\n\
                    os.system(f'cp -f {in_path} {TEMP_DIR}') \n\
                    text_to_pdf(in_path, out_path)\n\
                else:\n\
                    temp_path = os.path.join(TEMP_DIR, file)\n\
                    if not os.path.exists(temp_path):\n\
                        os.system(f'cp -f {in_path} {TEMP_DIR}')\n\
                    result = filecmp.cmp(in_path, temp_path)\n\
                    if result == False:\n\
                        os.system(f'cp -f {in_path} {TEMP_DIR}')\n\
                        text_to_pdf(in_path, out_path)\n\
    except Exception as error:\n\
        print(f'error: {error}')\n\
">> app.py


CMD ["python3", "app.py"]

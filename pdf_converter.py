from fpdf import FPDF
import os
import time 
import textwrap
import filecmp

INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/output"
TEMP_DIR = "/temp"

def text_to_pdf(in_file, out_file):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    with open(in_file) as file:
        for line in file:
            line = line.strip("\n")
            lines = textwrap.wrap(line, width_text)
            if len(lines) == 0:
                pdf.ln()
            for wrap in lines:
                pdf.cell(0, fontsize_mm, wrap, ln=1)
    pdf.output(out_file, 'F')

while True:
    try:
        time.sleep(1)
        input_files = os.listdir(INPUT_DIR)
        output_files = [name.split(".")[0] for name in os.listdir(OUTPUT_DIR)]
        for file in input_files:
            if os.path.isfile(os.path.join(INPUT_DIR, file)):
                in_file = file.split(".")[0]
                in_path = os.path.join(INPUT_DIR, file)
                out_path = os.path.join(OUTPUT_DIR, f"{in_file}.pdf")
                if in_file not in output_files:
                    os.system(f"cp -f {in_path} {TEMP_DIR}") 
                    text_to_pdf(in_path, out_path)
                else:
                    temp_path = os.path.join(TEMP_DIR, file)
                    if not os.path.exists(temp_path):
                        os.system(f"cp -f {in_path} {TEMP_DIR}")
                    result = filecmp.cmp(in_path, temp_path)
                    if result == False:
                        os.system(f"cp -f {in_path} {TEMP_DIR}")
                        text_to_pdf(in_path, out_path)
    except Exception as error:
        print(f"error: {error}")

FROM fedora:latest
RUN pip3 install fpdf
RUN mkdir /temp
COPY pdf_converter.py /app
WORKDIR /app
CMD ["python3", "pdf_converter.py"]
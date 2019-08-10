from textmining.model import SamsungReport
if __name__ == '__main__':
    texts=SamsungReport.read_file()
    print(SamsungReport.extract_hangul(texts))
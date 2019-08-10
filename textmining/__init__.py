from textmining.model import SamsungReport
if __name__ == '__main__':
    sr = SamsungReport()
    #sr.download()
    print(sr.extract_noun())

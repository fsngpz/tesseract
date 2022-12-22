import wave

# outfile = r"C:\Users\User\PycharmProjects\tesseract\tesseract\misc\sound\test.wav"

# infiles = [r"C:\Users\User\PycharmProjects\tesseract\piano\sound\1.wav",
#            r"C:\Users\User\PycharmProjects\tesseract\piano\sound\7U.wav"]
def compile(infiles, outfile):
    data = []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()

    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()

if __name__ == "__main__":
    compile(r"C:\Users\User\PycharmProjects\tesseract\piano\sound\1.wav")
import zipfile
import os

def compressFiles(filepaths=[], output="./lfiles_compressed.zip"):
    try:
        zfile = zipfile.ZipFile(output, 'w')
        for filepath in filepaths:
            print("Begin compressing file: {0}".format(filepath))
            zfile.write(filename=filepath, compress_type = zipfile.ZIP_DEFLATED)
        zfile.close()
        print("All file processed!")
        pass
    except Exception as e:
        print(e)
        pass

if __name__ == "__main__":
    compressFiles(filepaths=["./log.txt"])
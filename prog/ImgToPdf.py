import img2pdf
from pathlib import Path
import re
import sys
import os
from tqdm import tqdm

def extract_num(s, ret=0):
    p = re.compile(r'(\d+)')
    search = p.search(s)
    if search:
        return int(search.group()[-1])
    else:
        return ret

def ImageToPdf(outputpath, imagepath):
    lists = list(imagepath.glob('**/*'))
    imagepath_list = [str(i) for i in lists if i.match("*.jpg") or i.match("*.png") or i.match("*.jpeg")]
    imagepath_list.sort(key=lambda s: extract_num(s))

    with open(outputpath, "wb") as f:
        f.write(img2pdf.convert(imagepath_list))
    #print(f"{outputpath.name} :Done")

def main():
    args = sys.argv
    #base_path = input("PDFに変換したいフォルダが入った親フォルダをD&Pしてください")
    base_path = args[1]
    base_path = base_path.strip("\'")
    glob = Path(base_path).glob("*")
    comicfolderlist = list([item for item in list(glob) if item.is_dir()])
    #outputpathlist = list([item.with_name(f"{item.name}.pdf") for item in imagefolderlist])
    for comicpath in tqdm(comicfolderlist[1:]):
        basepathlist = list([item for item in list(comicpath.glob('*')) if item.is_dir()])
        for basepath in basepathlist:
            os.makedirs(f"E:/漫画/00_pdf/{comicpath}", exist_ok=True)
            ImageToPdf(Path(f"E:/漫画/00_pdf/{comicpath}/{basepath.name}.pdf"), basepath)
        #ImageToPdf(outputpath, imagepath)
        #except:
        #    import traceback
        #    traceback.print_exc()

if __name__=='__main__':
    main()

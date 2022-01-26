#author:shapemind
#dt: 2022/1/4 15:12

from typing import List
from PIL import Image
import os
import re
from fpdf import FPDF
import zipfile
import shutil

def read_file(dir_path):
  """
  获取需要转换的docx文件
  :param dir_path:
  :return:返回docx文件列表
  """
  docx_file_list = []
  for root,dirs,files in os.walk(dir_path):
    for file in files:
      if 'docx' in file:
        docx_file_list.append(file)
  return docx_file_list


def makir_tmp(dir_path, docx_file_list):
  """
  返回每个docx文件的tmp文件夹
  :param dir_path:
  :param docx_file_list:
  :return:
  """
  tmp_page_list = []
  for file in docx_file_list:
    abs_root_docx = dir_path+'\\'+file
    abs_root_zip = dir_path+'\\'+re.sub(r'docx','zip',file)
    abs_root_tmp = dir_path+'\\'+re.sub(r'\.docx','',file)+'_tmp'
    # 将docx文件重名为zip文件
    os.rename(abs_root_docx,abs_root_zip)
    # 进行解压
    f = zipfile.ZipFile(abs_root_zip, 'r')
    # 将图片提取并保存
    for ele in f.namelist():
      f.extract(ele, abs_root_tmp)
    # 释放该zip文件
    f.close()
    # 将docx文件从zip还原为docx
    os.rename(abs_root_zip,abs_root_docx)
    # 加临时文件夹内图片路径加入列表
    tmp_page_list.append(abs_root_tmp+'\word\media')
  
  #返回各个临时文件夹内图片路径
  return tmp_page_list

def sort_key(eles):
  '''
  排序用
  :param eles:
  :return:
  '''
  if eles:
    try:
      num = re.findall(r'\d+', eles)[0]
    except:
      num = -1
    return int(num)
  
def mk_pdf(tmp_page_list: List[str]) -> None:
  '''
  生成pdf
  :param tmp_page_list:
  :return:
  '''
  image_help_list = []
  image_list = []
  res_pdf = 'E:\word2page2pdf\PDF'
  for opt in tmp_page_list:
    # 获取pdf_name
    pdf_name_list = re.split(r'\\', opt)
    pdf_name = re.sub(r'_tmp','',pdf_name_list[2])
    
    # 获得该照片文件夹下所有图片，排序
    for path, dirs, files in os.walk(opt):
      for i in files:
        image_help_list.append(i)
    image_help_list.sort(key=sort_key)

    # 获得照片的绝对路径
    for name in image_help_list:
      image_list.append(opt + '\\' + name)

    # 获取照片尺寸，设置pdf尺寸
    im1 = Image.open(image_list[0])
    width, height = im1.size
    pdf = FPDF(unit="pt", format=[width, height])

    # 合并成pdf
    for page in image_list:
      pdf.add_page()
      pdf.image(page, 0, 0)
    pdf.output(res_pdf+"\\"+pdf_name+".pdf", "F")
    
    # 清空image_help_list和image_list
  image_help_list.clear()
  image_list.clear()

def clear_dir(dir_path, docx_file_list):
  '''
  删除文件夹
  :param dir_path:
  :param docx_file_list:
  :return:
  '''
  for file in docx_file_list:
    abs_root_tmp = dir_path+'\\'+re.sub(r'\.docx','',file)+'_tmp'
    if os.path.isdir(abs_root_tmp):
      shutil.rmtree(abs_root_tmp)
      
  
def extract_page(path, zip_path, tmp_path, store_path):
  '''
  :param path:源文件
  :param zip_path:docx重命名为zip
  :param tmp_path:中转图片文件夹
  :param store_path:最后保存结果的文件夹（需要手动创建）
  :return:
  '''
  # 将docx文件重命名为zip文件
  os.rename(path, zip_path)
  # 进行解压
  f = zipfile.ZipFile(zip_path, 'r')
  # 将图片提取并保存
  for file in f.namelist():
    f.extract(file, tmp_path)
  # 释放该zip文件
  f.close()
  # 将docx文件从zip还原为docx
  os.rename(zip_path, path)
  # 得到缓存文件夹中图片列表
  pic = os.listdir(os.path.join(tmp_path, 'word/media'))
  # 将图片复制到最终的文件夹中
  for i in pic:
    # 根据word的路径生成图片的名称
    new_name = path.replace('\\', '_')
    new_name = new_name.replace(':', '') + '_' + i
    shutil.copy(os.path.join(tmp_path + '/word/media', i), os.path.join(store_path, new_name))
  # 删除缓冲文件夹中的文件，用以存储下一次的文件
  for i in os.listdir(tmp_path):
    # 如果是文件夹则删除
    if os.path.isdir(os.path.join(tmp_path, i)):
      shutil.rmtree(os.path.join(tmp_path, i))



def page2pdf(pdf_name):
  # 先排序
  path = pdf_name
  image_help_list = []
  image_list = []
  for path,dirs,files in os.walk(pdf_name):
    for i in files:
      image_help_list.append(i)
  image_help_list.sort(key=sort_key)

  for name in image_help_list:
    image_list.append(pdf_name+'\\'+name)

  # 获取照片尺寸，设置pdf尺寸
  im1 = Image.open(image_list[0])
  width, height = im1.size
  pdf = FPDF(unit = "pt", format = [width, height])

  for page in image_list:
    pdf.add_page()
    pdf.image(page, 0, 0)
  pdf.output("test.pdf", "F")
    
if __name__ == '__main__':
  dir_path = 'E:\word2page2pdf'
  docx_file_list = read_file(dir_path)
  tmp_page_list = makir_tmp(dir_path,docx_file_list)
  mk_pdf(tmp_page_list)
  clear_dir(dir_path,docx_file_list)
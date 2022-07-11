import json

key_list = []
def get_dict_allkeys(dict_a):
    """
    遍历嵌套字典，获取json返回结果的所有key值
    :param dict_a:
    :return: key_list
    """
    if isinstance(dict_a, dict):  # 使用isinstance检测数据类型
        # 如果为字典类型，则提取key存放到key_list中
        for x in range(len(dict_a)):
            temp_key = list(dict_a.keys())[x]
            temp_value = dict_a[temp_key]
            if isinstance(temp_value, list) :
                temp_key=temp_key+"."
            key_list.append(temp_key)
            get_dict_allkeys(temp_value)
              # 自我调用实现无限遍历
    elif isinstance(dict_a, list):
        # 如果为列表类型，则遍历列表里的元素，将字典类型的按照上面的方法提取key
        for k in dict_a:
            if isinstance(k, dict):
                for x in range(len(k)):
                    temp_key = list(k.keys())[x]
                    temp_value = k[temp_key]
                    key_list.append(temp_key)
                    get_dict_allkeys(temp_value) # 自我调用实现无限遍历
    return key_list

if __name__ == '__main__':
    with open('E:\\Nutstore_file\\我的坚果云\\WorkFile\\招行项目\\特征\\实时特征\\行外非人行特征\\个人工商'
              '\\qjs_nls09_zx00904d\\qjs_nls09_zx00904d_jmespath.json','r',encoding='utf-8') as f:
        jmespath_json = json.load(f)
    
    get_keys = get_dict_allkeys(jmespath_json)
    print(get_keys)
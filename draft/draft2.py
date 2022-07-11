from pathlib import Path
import json
import os
analysis_root_dir = "E:\\Nutstore_file\\我的坚果云\\WorkFile\\招行项目\\特征\\zs_realtime_feature\\行外非人行\\工商(ic)_企业工商(qje)"
store_result="E:\\Nutstore_file\\我的坚果云\\WorkFile\\招行项目\\特征\\zs_realtime_feature\\dependency.csv"

def helper(res,result,tmp_list):
	#res为传入的json数据，循序找出每一个key
    for item in res:
        if type(res[str(item)]).__name__ == 'dict':
            helper(res[str(item)],result)
        elif type(res[str(item)]).__name__ == 'list':
            for i in range(len(res[str(item)])):
                helper(res[str(item)][i],result,tmp_list)
            for field in result:
                if '.' not in field:
                    tmp_list.append(str(item)+'.'+field)
            result.clear()
        else:
            result.append(item)
		
    return tmp_list


def parse_dir(root_dir):
    path = Path(root_dir)
    
    all_json_file = list(path.glob('**/*.json'))
    
    no_jmespath_json_file = []
    for json_file in all_json_file:
        if 'jme' not in str(json_file):
            no_jmespath_json_file.append(json_file)
    
    key_result = []
    res = []
    tmp_list = []
    final_key_result = []
    
    for i in no_jmespath_json_file:
        prefix = str(os.path.basename(i)).replace('.json','')
        # print(prefix)
        with i.open(encoding='utf8') as f:
            json_object = json.load(f)
            # print(type(json_object))
            # print(json_object)
            if type(json_object).__name__ == 'list':
                tmp_dict = {prefix:json_object}
                # print(type(tmp_dict))
                res = helper(tmp_dict, key_result,tmp_list)
            elif type(json_object).__name__ == 'dict':
                res = helper(json_object, key_result,tmp_list)
    tmp_set = set(i for i in res if '_cp.' not in i)
    print(tmp_set)

def write_result_in_file(write_path, write_content):
    with open(write_path, 'w') as f:
        f.writelines("service_name,action,method,url\n")
        for dict_content in write_content:
            url = dict_content['url']
            method = dict_content['method']
            action = dict_content['action']
            service_name = dict_content['service_name']
            f.writelines(service_name + "," + action + "," + method + "," + url + "\n")
    
if __name__ == '__main__':
    parse_dir(analysis_root_dir)
    # print("main begin...")
    # parse_result = parse_dir(analysis_root_dir)
    # print(parse_result)
    # write_result_in_file(store_result, parse_result)
    # print("main finished...")
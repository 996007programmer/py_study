#author:shapemind
#dt: 2022/6/10 15:02
import importlib
import json
from pyspark.sql import functions as F


domain = {}
content = {}
out_schema = {}
shuffle = 10

def main():
	featuremodel = {"prh_mla_dct": importlib.import_module("prh_mla_dct__14")}
	print(featuremodel)
	config = list(featuremodel.keys())
	print(config)
	inputSchema_map = {}
	for d, mod in featuremodel.items():
		# domain 存储schema
		# content 存储init_features
		inputSchema = json.loads(mod.features.get("inputSchema"))
		sMap = {i['name']: i for i in inputSchema}
		inputSchema = list(sMap.values())
		inputSchema_map[d] = inputSchema
		domain[d] = json.dumps(inputSchema, ensure_ascii=False)
		feat = {}
		for i in ["fql", "schema", "schemaExpression", "query"]:
			feat[i] = mod.features[i]
		content[d] = json.dumps(feat, ensure_ascii=False)
		out_schema[d] = mod.features["schema"]
	
	load = {
		"content": [json.dumps(content, ensure_ascii=False)],
		"domain": [json.dumps(domain, ensure_ascii=False)],
		"config": [",".join(config)]
	}
	
	ldd = [
		      (
			      json.dumps({"content": load["content"][0],
			                  "domain": load["domain"][0],
			                  "config": load["config"][0]}))
	      ] * shuffle * 200
	
	# print(inputSchema_map)


if __name__ == '__main__':
    main()
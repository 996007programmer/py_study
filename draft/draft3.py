#author:shapemind
#dt: 2021/12/6 11:06

import json
import pandas as pd

def main():
	features = {
		"fql": """expand
	    coalesce(bus_typ_cd,'0') as bus_typ_cd_n,
	    cast(bus_typ_cd_n,'int') as bus_typ,
	    (act_nbr*100+bus_typ) as act_bus_type,
	from t41_pbc2_crd_trx_sgs_inf;

	-- 最大贷款账户个数对应的业务大类
	-- 最大贷款账户个数对应的业务类型
	-- 贷款业务类型去重个数
	select
	    max_index(act_bus_type,bus_big_cls,bus_typ_cd) as m_i,
	    count(distinct bus_typ_cd) as bus_typ_cnt
	from t41_pbc2_crd_trx_sgs_inf;""",
		"schema": {"bus_big_cls_m_i_act_bus_type": "string", "bus_typ_cd_m_i_act_bus_type": "string",
		           "bus_typ_cnt": "int"},
		"inputSchema": "[{\"name\":\"crd_qry_tm\",\"type\":\"date\",\"required\":false,\"desc\":\"资信查询时间\",\"missing\":{\"value\":[\"\",\"\\\\N\",\"1900-01-01\"],\"min\":\"1900-01-01\"}},{\"name\":\"frs_strk_bus_dtrb_mon\",\"type\":\"date\",\"required\":false,\"desc\":\"首笔业务发放月份\"},{\"name\":\"act_nbr\",\"type\":\"int\",\"required\":true,\"desc\":\"账户数\"},{\"name\":\"bus_typ_cd\",\"type\":\"string\",\"required\":true,\"desc\":\"业务类型代码\"},{\"name\":\"bus_big_cls\",\"type\":\"string\",\"required\":true,\"desc\":\"业务大类\"}]",
		"schemaExpression": [],
		"query": "rO0ABXNyABNqYXZhLnV0aWwuQXJyYXlMaXN0eIHSHZnHYZ0DAAFJAARzaXpleHAAAAACdwQAAAACc3IAH2NvbS5jcmVkaXR4LnhmZWF0dXJlLmNvcmUuUXVlcnkAAAAAAAAAAQIAC1oACmV4cGFuZEZsYWdMAARhZ2dzdAAQTGphdmEvdXRpbC9MaXN0O0wADmFyaXRobWV0aWNBZ2dzcQB+AANMAAljb21wb3VuZHNxAH4AA0wABGRlcHNxAH4AA0wAB2V4cGFuZHNxAH4AA0wABmZpZWxkc3EAfgADTAAEZnJvbXQAEkxqYXZhL2xhbmcvU3RyaW5nO0wABWxpbWl0dAAQTGphdmEvbGFuZy9Mb25nO0wAB29wZXJhbmR0AChMY29tL2NyZWRpdHgveGZlYXR1cmUvY29yZS9pbmYvSU9wZXJhbmQ7TAAGc2NoZW1hdAAPTGphdmEvdXRpbC9NYXA7eHABc3EAfgAAAAAAAHcEAAAAAHhzcQB+AAAAAAAAdwQAAAAAeHNxAH4AAAAAAAB3BAAAAAB4c3EAfgAAAAAAAHcEAAAAAHhzcQB+AAAAAAADdwQAAAADc3IAJ2NvbS5jcmVkaXR4LnhmZWF0dXJlLmV4ZC5FeHBhbmRDb2FsZXNjZQAAAAAAAAABAgACTAAEY29sc3EAfgADTAAIZGF0YVR5cGV0AC1MY29tL2NyZWRpdHgveGZlYXR1cmUvY29tbW9uL3NjaGVtYS9EYXRhVHlwZTt4cgAkY29tLmNyZWRpdHgueGZlYXR1cmUuZnVuYy5CYXNlRXhwYW5kAAAAAAAAAAECAAJMAAVhbGlhc3EAfgAETAAJY29uc3RMaXN0cQB+AAN4cHQADGJ1c190eXBfY2RfbnNxAH4AAAAAAAJ3BAAAAAJzcgArY29tLmNyZWRpdHgueGZlYXR1cmUuY29tbW9uLnZhbHVlcy5Db25zdGFudAAAAAAAAAABAgAGTAAJYm9vbFZhbHVldAATTGphdmEvbGFuZy9Cb29sZWFuO0wACWNvbnN0VHlwZXQALkxjb20vY3JlZGl0eC94ZmVhdHVyZS9jb21tb24vdmFsdWVzL0NvbnN0VHlwZTtMAAtkb3VibGVWYWx1ZXQAEkxqYXZhL2xhbmcvRG91YmxlO0wACGludFZhbHVldAATTGphdmEvbGFuZy9JbnRlZ2VyO0wAC3F1ZXJ5UmVzdWx0cQB+AANMAAtzdHJpbmdWYWx1ZXEAfgAEeHBwfnIALGNvbS5jcmVkaXR4LnhmZWF0dXJlLmNvbW1vbi52YWx1ZXMuQ29uc3RUeXBlAAAAAAAAAAASAAB4cgAOamF2YS5sYW5nLkVudW0AAAAAAAAAABIAAHhwdAAKQ29uc3RGaWVsZHBwcHQACmJ1c190eXBfY2RzcQB+ABRwfnEAfgAadAALQ29uc3RTdHJpbmdwcHB0AAEweHNxAH4AAAAAAAJ3BAAAAAJxAH4AHnEAfgAieH5yACtjb20uY3JlZGl0eC54ZmVhdHVyZS5jb21tb24uc2NoZW1hLkRhdGFUeXBlAAAAAAAAAAASAAB4cQB+ABt0AApUeXBlU3RyaW5nc3IAI2NvbS5jcmVkaXR4LnhmZWF0dXJlLmV4ZC5FeHBhbmRDYXN0AAAAAAAAAAECAAJMAANjb2xxAH4ABEwABnRvVHlwZXEAfgAPeHEAfgAQdAAHYnVzX3R5cHNxAH4AAAAAAAJ3BAAAAAJzcQB+ABRwcQB+ABxwcHB0AAxidXNfdHlwX2NkX25zcQB+ABRwcQB+ACBwcHB0AANpbnR4cQB+ACx+cQB+ACR0AAdUeXBlSW50c3IAKWNvbS5jcmVkaXR4LnhmZWF0dXJlLmV4ZC5FeHBhbmRBcml0aG1ldGljAAAAAAAAAAECAAB4cgAvY29tLmNyZWRpdHgueGZlYXR1cmUuZnVuYy5BYnN0cmFjdEFyaXRobWV0aWNFeHAAAAAAAAAAAQIABEwABWFsaWFzcQB+AARMAARsZWZ0dAAtTGNvbS9jcmVkaXR4L3hmZWF0dXJlL2NvbW1vbi92YWx1ZXMvQ29uc3RhbnQ7TAAMb3BlcmF0b3JUeXBldAA2TGNvbS9jcmVkaXR4L3hmZWF0dXJlL2Z1bmMvZW51bXR5cGUvQXJpdGhPcGVyYXRvclR5cGU7TAAFcmlnaHRxAH4AM3hxAH4AFHBwcHBwcHQADGFjdF9idXNfdHlwZXNxAH4AMXBwcHBwcHBzcQB+ABRwcQB+ABxwcHB0AAdhY3RfbmJyfnIANGNvbS5jcmVkaXR4LnhmZWF0dXJlLmZ1bmMuZW51bXR5cGUuQXJpdGhPcGVyYXRvclR5cGUAAAAAAAAAABIAAHhxAH4AG3QAFUFyaXRoT3BlcmF0b3JNdWx0aXBseXNxAH4AFHB+cQB+ABp0AAhDb25zdEludHBzcgARamF2YS5sYW5nLkludGVnZXIS4qCk94GHOAIAAUkABXZhbHVleHIAEGphdmEubGFuZy5OdW1iZXKGrJUdC5TgiwIAAHhwAAAAZHBwfnEAfgA6dAAQQXJpdGhPcGVyYXRvckFkZHNxAH4AFHBxAH4AHHBwcHQAB2J1c190eXB4c3EAfgAAAAAAAncEAAAAAnNyAB9jb20uY3JlZGl0eC54ZmVhdHVyZS5jb3JlLkZpZWxkAAAAAAAAAAECAAJMAAVhbGlhc3EAfgAETAAEbmFtZXEAfgAEeHBwcQB+AB5zcQB+AEhwcQB+ACx4dAAYdDQxX3BiYzJfY3JkX3RyeF9zZ3NfaW5mcHBwc3EAfgACAHNxAH4AAAAAAAJ3BAAAAAJzcgArY29tLmNyZWRpdHgueGZlYXR1cmUuYWdnLkFnZ3JlZ2F0b3JNYXhJbmRleAAAAAAAAAABAgACTAALZXh0cmFjdE5hbWVxAH4AA0wAB21heE5hbWVxAH4ABHhyAChjb20uY3JlZGl0eC54ZmVhdHVyZS5mdW5jLkJhc2VBZ2dyZWdhdG9yAAAAAAAAAAECAANaAANleGRMAAVhbGlhc3EAfgAETAAJY29uc3RMaXN0cQB+AAN4cAB0AANtX2lzcQB+AAAAAAADdwQAAAADc3EAfgAUcHEAfgAccHBwdAAMYWN0X2J1c190eXBlc3EAfgAUcHEAfgAccHBwdAALYnVzX2JpZ19jbHNzcQB+ABRwcQB+ABxwcHB0AApidXNfdHlwX2NkeHNxAH4AAAAAAAJ3BAAAAAJxAH4AVnEAfgBYeHEAfgBUc3IAKGNvbS5jcmVkaXR4LnhmZWF0dXJlLmFnZy5BZ2dyZWdhdG9yQ291bnQAAAAAAAAAAQIAAloACGRpc3RpbmN0TAADY29scQB+AAR4cQB+AE8AdAALYnVzX3R5cF9jbnRzcQB+AAAAAAACdwQAAAACc3EAfgAUcHEAfgAccHBwdAAIZGlzdGluY3RzcQB+ABRwcQB+ABxwcHB0AApidXNfdHlwX2NkeAFxAH4AYXhzcQB+AAAAAAAAdwQAAAAAeHNxAH4AAAAAAAB3BAAAAAB4c3EAfgAAAAAAAHcEAAAAAHhzcQB+AAAAAAAAdwQAAAAAeHNxAH4AAAAAAAB3BAAAAAB4dAAYdDQxX3BiYzJfY3JkX3RyeF9zZ3NfaW5mcHBzcgARamF2YS51dGlsLkhhc2hNYXAFB9rBwxZg0QMAAkYACmxvYWRGYWN0b3JJAAl0aHJlc2hvbGR4cD9AAAAAAAAGdwgAAAAIAAAABXQACmNyZF9xcnlfdG1zcgApY29tLmNyZWRpdHgueGZlYXR1cmUuY29tbW9uLnNjaGVtYS5TY2hlbWEAAAAAAAAAAQIACFoACW5ld1NjaGVtYVoACHJlcXVpcmVkTAAFYWxpYXNxAH4ABEwABGRlc2NxAH4ABEwAB21pc3Npbmd0ACxMY29tL2NyZWRpdHgveGZlYXR1cmUvY29tbW9uL3NjaGVtYS9NaXNzaW5nO0wABG5hbWVxAH4ABEwABXNjb3BldAAqTGNvbS9jcmVkaXR4L3hmZWF0dXJlL2NvbW1vbi9zY2hlbWEvU2NvcGU7TAAEdHlwZXEAfgAPeHAAAHB0ABLotYTkv6Hmn6Xor6Lml7bpl7RzcgAqY29tLmNyZWRpdHgueGZlYXR1cmUuY29tbW9uLnNjaGVtYS5NaXNzaW5nAAAAAAAAAAECAApaAAhjaGVja01heFoACGNoZWNrTWluTAACY210AA9MamF2YS91dGlsL1NldDtMAANtYXh0ABJMamF2YS9sYW5nL09iamVjdDtMAAdtYXhEYXRldAAZTGphdmEvdGltZS9Mb2NhbERhdGVUaW1lO0wACW1heERvdWJsZXEAfgAXTAADbWlucQB+AHJMAAdtaW5EYXRlcQB+AHNMAAltaW5Eb3VibGVxAH4AF0wABXZhbHVlcQB+AAN4cAABc3IAEWphdmEudXRpbC5IYXNoU2V0ukSFlZa4tzQDAAB4cHcMAAAABD9AAAAAAAADdAAAdAAKMTkwMC0wMS0wMXQAAlxOeHBwcHQACjE5MDAtMDEtMDFzcgANamF2YS50aW1lLlNlcpVdhLobIkiyDAAAeHB3CAUAAAdsAQH/eHBzcQB+AAAAAAADdwQAAAADcQB+AHdxAH4AeXEAfgB4eHEAfgBqcH5xAH4AJHQACFR5cGVEYXRldAAHYWN0X25icnNxAH4AawABcHQACei0puaIt+aVsHBxAH4AgHBxAH4AL3QAFWZyc19zdHJrX2J1c19kdHJiX21vbnNxAH4AawAAcHQAGOmmlueslOS4muWKoeWPkeaUvuaciOS7vXBxAH4Ag3BxAH4AfnQACmJ1c190eXBfY2RzcQB+AGsAAXB0ABLkuJrliqHnsbvlnovku6PnoIFwcQB+AIZwcQB+ACV0AAtidXNfYmlnX2Nsc3NxAH4AawABcHQADOS4muWKoeWkp+exu3BxAH4AiXBxAH4AJXh4"
	}
	features_dumps = json.dumps(features)
	features_json = json.loads(features_dumps)
	
	config = list(features_json.keys())
	# print(features_json.get('inputSchema'))
	
	inputSchema = json.loads(features_json.get('inputSchema'))
	sMap = {i['name']: i for i in inputSchema}
	inputSchema = list(sMap.values())
	feat = {}
	for i in ["fql", "schema", "schemaExpression", "query"]:
		feat[i] = features_json.get(i)
	content = json.dumps(feat, ensure_ascii=False)
	out_schema = features_json.get('schema')
	# print(out_schema)

	load = {
		"content": [json.dumps(content, ensure_ascii=False)],
		"domain": [json.dumps(inputSchema, ensure_ascii=False)],
		"config": [",".join(config)],
	}
	print([",".join(config)])
	ldd = {"content": [str(load["content"][0])],
			"domain": [str(load["domain"][0])],
			"config": [str(load["config"][0])]}
	df = pd.DataFrame(ldd)
	xfconfig_df = spark.createDataFrame(df)
	xfconfig_df.createOrReplaceTempView('xfconfig')
	confres = spark.sql('''select default.xfeature13(content, domain, config) as loaded from xfconfig''').toJSON().first()
	res = json.loads(confres).get("loaded")
	
	data_dict = {"msg_id":['ATREWT213','fusah10'],
	             "cert_no":['440123193021','231514123'],
	             "rn":['1','1'],
	             "act_nbr":[1,2],
	             "bus_typ_cd":['19','18'],
	             "bus_big_cls":['1','2'],
	             "prh_mla_dct":['{"act_nbr":1,"bus_typ_cd":"19","bus_big_cls":"1"}',
	                            '{"act_nbr":2,"bus_typ_cd":"18","bus_big_cls":"2"}',
	                            ]
	             }
	data_df = pd.DataFrame(data_dict)
	prh_mla_dct = spark.createDataFrame(df)
	xf_df = spark.sql('''select default.xfeature13(from prt_mla_dct, 'from prt_mla_dct','') as xf_field from prt_mla_dct''')

if __name__ == '__main__':
	main()
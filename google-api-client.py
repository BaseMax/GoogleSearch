from googleapiclient.discovery import build

api_key = "**************************************"
cse_id = "***************"

def google_search(search_term, api_key, cse_id, **kwargs):
	service = build("customsearch", "v1", developerKey=api_key)
	res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
	return res

result = google_search("Github", api_key, cse_id)
print(result)

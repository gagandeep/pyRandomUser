import urllib
import urllib2
import json

class Randomuser(object):
	@classmethod
	def _make_request(self, params=None):
		url = 'http://api.randomuser.me/'
		if params:
			query_params = urllib.urlencode(params)
			url += "?"+query_params
		fp = urllib2.urlopen(url)
		response = json.load(fp)
		results = response['results'] if 'results' in response else None
		if results and len(results) == 1:
			return results[0]
		else:
			return results

	@classmethod
	def generate(self, num=1):
		return Randomuser._make_request({"results":num})

	@classmethod
	def generate_female(self, num=1):
		return Randomuser._make_request({"gender":"female","results":num})

	@classmethod
	def generate_male(self, num=1):
		return Randomuser._make_request({"gender":"male","results":num})

	@classmethod
	def generate_seed(self, seed):
		return Randomuser._make_request({"seed":seed})

if __name__ == '__main__':
	print Randomuser.generate(2)
	print Randomuser.generate_male(2)
	print Randomuser.generate_female(2)
	print Randomuser.generate_seed("7b9a05bd69c99c04")
	
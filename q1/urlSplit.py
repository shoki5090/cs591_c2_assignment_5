class urlSplit:

	def __init__(self,url):
		self.url = url
		self.protocol = ""
		self.domain = ""
		self.path = ""

	def urlSplitting(self):

		#split for protocol

		components = self.url.split("://")
		self.protocol = components[0]
		
		# split for domain
		more_components = components[1].split("/")
		if len(more_components) > 2:
			self.domain = more_components[0]
			self.path = more_components[1:]
		else:
			self.domain = more_components[0]	

			self.path = more_components[1]


		return [self.protocol, self.domain, self.path]

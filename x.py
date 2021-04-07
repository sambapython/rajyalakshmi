class RegionOut(BaseModel):
	def __init__(self, *args, **kwargs):
		print(args)
		print(kwargs)
		import pdb;pdb.set_trace()
		super(RegionOut, self.).__init__(*args, **kwargs)
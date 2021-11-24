class BaseError(Exception):
	"""
	The base error for the module.
	"""
	
	pass

class ColorUtilitiesError(BaseError):
	"""
	Error for color utilities.
	"""

	pass

class ColorNotFoundError(BaseError):
	"""
	This error raises when a color is not found!
	"""

	pass

class HexNotFoundError(BaseError):
	"""
	This error raises when a hex is not found!
	"""

	pass
def grep(pattern, lines, ignore_case=False):
	for line in lines:
		if ~ignore_case and pattern in line:
			yield line
		elif ignore_case and pattern.lower() in line.lower():
			yield line


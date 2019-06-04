rule api:
    input:
        chr = os.environ.get("chr")
	pos = os.environ.get("pos")
	alt = os.environ.get("alt")
    output:
        "variant.txt"
    run:
	shell("curl 'http://0.0.0.0:5000/api?chr={chr}&pos={pos}&alt={alt}'")

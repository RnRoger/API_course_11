<<<<<<< HEAD
rule api:
    params:
        chr = os.environ.get("chr"),
        pos = os.environ.get("pos"),
        alt = os.environ.get("alt")
    output:
        "variant.txt"
    run:
        shell("wget 'http://0.0.0.0:5000/api?chr={params.chr}&pos={params.pos}&alt={params.alt}' --output-document {output}")

=======
rule api:
    params:
        chr = os.environ.get("chr"),
        pos = os.environ.get("pos"),
        alt = os.environ.get("alt")
    output:
        "variant_data.txt"
    run:
        shell("wget 'http://0.0.0.0:5000/api?chr={params.chr}&pos={params.pos}&alt={params.alt}' --output-document {output}")


with open('variant_data.txt') as f:
    first_line = f.readline()
    if first_line != "Not Malignant" or "Unknown":
        rule fake:
            params:
                chr = os.environ.get("chr")
                pos = os.environ.get("pos"),
                alt = os.environ.get("alt")
            output:
                "test.txt"
            run:
                shell("wget 'http://0.0.0.0:5000/api?chr={params.chr}&pos={params.pos}&alt={params.alt}' --output-document {output}")
>>>>>>> ec85ff5b46e9fce771787880e92d6fe596ae9de0

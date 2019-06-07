rule variant_api:
    params:
        chr = os.environ.get("chr"),
        pos = os.environ.get("pos"),
        alt = os.environ.get("alt")
    output:
        "variant_info.txt"
    run:
        shell("wget 'http://0.0.0.0:5000/api?chr={params.chr}&pos={params.pos}&alt={params.alt}' --output-document {output}")

rule ensembl_api:
    input:
        "variant_info.txt"
    output:
        "ensembl_application.json"
    run:
        with open(input[0]) as file:
            for line in file:
                rsID = line[2] 
        shell("wget -q --header='Content-type:application/json' 'https://rest.ensembl.org/variation/human/{rsID}?genotyping_chips=1'  --output-document {output}")

rule all:
    input:
        "report.html"

# Call local API to retrieve variant data based on chromosome (chr), position (pos) and alternative allele (alt)
rule variant_api:
    params:
        chr = os.environ.get("chr"),
        pos = os.environ.get("pos"),
        alt = os.environ.get("alt")
    output:
        "variant_info.txt"
    run:
        shell("wget 'http://0.0.0.0:5000/api?chr={params.chr}&pos={params.pos}&alt={params.alt}' --output-document {output}")

# Call ensembl API to retrieve additional information about variant
rule ensembl_api:
    input:
        "variant_info.txt"
    output:
        "ensembl_application.json"
    run:
        with open(input[0]) as file:
            line = file.readline()
            print(line)
            rsID = str(line.split(",")[2])
            rsID = rsID.replace("'", "")
	    rsID = rsID.replace(" ", "")
            shell("wget -q --header='Content-type:application/json' 'https://rest.ensembl.org/variation/human/{rsID}?genotyping_chips=1'  --output-document {output}")
    onerror:
        print("Snakemake stopped, this could be due to a Non Malignant or Unknown variant")
        print("Variant = " + str(line))


# Create workflow
rule workflow:
	output:
		"workflow.svg"
	shell:
		"snakemake --dag all | dot -Tsvg > {output}"

# Create HTML report
rule report:
	input:
		VariantInfo = "variant_info.txt",
        Ensembl = "ensembl_application.json",
		Workflow = "workflow.svg"
	output:
		"report.html"
	run:
		from snakemake.utils import report
		report("""API Course 11 (version 1.0)""", output[0], metadata="Authors: Awan & Melanie", **input)

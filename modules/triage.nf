process TRIAGE {
    tag "$meta.id"
    label 'process_single'

    container 'python:3.11-slim'

    input:
    tuple val(meta), path(vcf)

    output:
    tuple val(meta), path("${meta.id}.triage.jsonl"), emit: triage_jsonl
    path "versions.yml",                                  emit: versions

    script:
    """
    triage.py ${vcf} ${meta.id}.triage.jsonl

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        python: \$(python3 --version | sed 's/Python //')
        triage_rule_version: v1.0.0
    END_VERSIONS
    """
}
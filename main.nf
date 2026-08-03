#!/usr/bin/env nextflow
nextflow.enable.dsl = 2
include { GLASSBOX_TRIAGE } from './subworkflow/glassbox_triage.nf'
params.input         = "${projectDir}/tests/sample.vcf"
params.schema        = "${projectDir}/docs/schema.json"
params.sarek_version = "sarek-3.9.0"
workflow {
    ch_vcf = Channel
        .fromPath(params.input, checkIfExists: true)
        .map { vcf -> [ [id: 'sample'], vcf ] }
    ch_schema = Channel.fromPath(params.schema, checkIfExists: true)
    GLASSBOX_TRIAGE(ch_vcf, ch_schema, params.sarek_version)
    GLASSBOX_TRIAGE.out.audit_bundle.view { meta, bundle ->
        "Audit bundle for ${meta.id}: ${bundle}"
    }
}

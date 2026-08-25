from client import CloudDspmSensitiveDataDiscoveryRiskClassifierClient

def main():
    client = CloudDspmSensitiveDataDiscoveryRiskClassifierClient()
    res = client.audit_cloud_data_security_posture('arn:aws:s3:::analytics-raw-bucket')
    print('DSPM Audit: ' + res['dspm_audit_id'] + ' | Storage: ' + res['storage_uri'])
    print('Sensitive Entities Classified: ' + str(res['pii_financial_phi_entities_classified']) + ' | Risk: ' + res['contextual_data_risk_score'])
    print('Compliance Score: ' + str(res['gdpr_hipaa_pci_dss_compliance_score_pct']) + '% | Policy Generated: ' + str(res['automated_least_privilege_iam_policy_generated']))

if __name__ == '__main__':
    main()

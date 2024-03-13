## About the connector
The Cymulate Web Application Firewall will validate the configuration, implementation, and efficacy, to ensure that the Web Application Firewall blocks malicious payloads before they get to your Web Application. Technical reports provide analysis of the attacks and actionable mitigation guidance that help security teams to shore up their defenses against web application attacks.
<p>This document provides information about the Cymulate Web Application Firewall - BAS Connector, which facilitates automated interactions, with a Cymulate Web Application Firewall - BAS server using FortiSOAR&trade; playbooks. Add the Cymulate Web Application Firewall - BAS Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Cymulate Web Application Firewall - BAS.</p>

### Version information

Connector Version: 1.0.0


Authored By: Fortinet

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-cymulate-web-application-firewall</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Cymulate Web Application Firewall - BAS server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Cymulate Web Application Firewall - BAS server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Cymulate Web Application Firewall - BAS</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the server URL to connect and perform the automated operations.
</td>
</tr><tr><td>API Key</td><td>API key to access the endpoint to connect and perform the automated operations
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get WAF Report Results</td><td>Retrieves the latest Web Application Firewall report results by the environment ID.</td><td>get_waf_report_results <br/>Investigation</td></tr>
<tr><td>Get WAF Site Results</td><td>Retrieves detailed list of the latest Web Application Firewall site results and their IDs.</td><td>get_waf_site_results <br/>Investigation</td></tr>
<tr><td>Get WAF Payload Response</td><td>Retrieves the Web Application Firewall response data based on the payload ID that you have specified.</td><td>get_waf_payload_response <br/>Investigation</td></tr>
<tr><td>Get Technical Report Results</td><td>Retrieves the latest technical report results based on the site ID that you have specified.</td><td>get_technical_report_results <br/>Investigation</td></tr>
<tr><td>Launch WAF Assessment</td><td>Launch a Web Application Firewall assessment based on the parameters that you have specified.</td><td>launch_waf_assessment <br/>Investigation</td></tr>
<tr><td>Stop WAF Assessment</td><td>Stop a Web Application Firewall assessment that is running.</td><td>stop_waf_assessment <br/>Investigation</td></tr>
<tr><td>Get WAF Assessment History</td><td>Retrieves the Web Application Firewall assessment history within the date range provided in the query parameters. If a date range is not provided, the response will retrieve the history from the last 30 days.</td><td>get_waf_assessment_history <br/>Investigation</td></tr>
<tr><td>Get Technical Report Results By Assessment ID</td><td>Retrieves the Web Application Firewall technical report results for a specific assessment.</td><td>get_technical_report_results_by_id <br/>Investigation</td></tr>
<tr><td>Get Executive Report Results By Assessment ID</td><td>Retrieves the Web Application Firewall executive report results for a specific assessment.</td><td>get_executive_report_results_by_id <br/>Investigation</td></tr>
<tr><td>Get WAF Site IDs</td><td>Retrieves the detailed list of site IDs for sites tested in Web Application Firewall assessments.</td><td>get_waf_site_ids <br/>Investigation</td></tr>
<tr><td>Get WAF Sites</td><td>Retrieves the detailed list of sites tested in Web Application Firewall assessments.</td><td>get_waf_sites <br/>Investigation</td></tr>
<tr><td>Get WAF Templates</td><td>Retrieves the detailed list of available Web Application Firewall templates.</td><td>get_waf_templates <br/>Investigation</td></tr>
<tr><td>Get WAF Template By ID</td><td>Retrieves the specific Web Application Firewall template by its ID.</td><td>get_waf_template_by_id <br/>Investigation</td></tr>
<tr><td>Get WAF Assessment Status</td><td>Retrieves the Web Application Firewall assessment status by the assessment ID.</td><td>get_waf_assessment_status <br/>Investigation</td></tr>
</tbody></table>

### operation: Get WAF Report Results
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>Specify the environment ID. If an ID is not provided, the request will return latest report results for the default environment.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get WAF Site Results
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>Specify the environment ID. If an ID is not provided, the request will return latest results for the default environment.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get WAF Payload Response
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Payload ID</td><td>Specify the payload ID whose Web Application Firewall response data is to be retrieved.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Technical Report Results
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Site ID</td><td>Specify the site ID whose technical report results is to be retrieved.
</td></tr><tr><td>Offset</td><td>Specify the index of the first item to be returned by this operation. This parameter is useful if you want to get a subset of records, say records starting from the 10th index.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of results that this operation should return. The minimum supported value is 1000 and the maximum supported value is 10000.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Launch WAF Assessment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Sites</td><td>Specify the comma separated values of urls. eg: https://example1.com,https://example2.com
</td></tr><tr><td>Template ID</td><td>Specify the template ID to launch a Web Application Firewall assessment.
</td></tr><tr><td>Schedule</td><td>Specify the datetime of the schedule.
</td></tr><tr><td>Schedule Loop</td><td>Specify the schedule loop. eg: one-time
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Stop WAF Assessment
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Environment ID</td><td>Specify the environment ID. If an ID is not provided, the most recently launched assessment will be stopped.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get WAF Assessment History
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>From Date</td><td>Specify the start date to fetch the Web Application Firewall assessments.
</td></tr><tr><td>To Date</td><td>Specify the end date to fetch the Web Application Firewall assessments.
</td></tr><tr><td>Environment ID</td><td>Specify the environment ID. If an ID is not provided, the results will show data from the Default environment.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Technical Report Results By Assessment ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Assessment ID</td><td>Specify the assessment ID whose Web Application Firewall technical report results is to be retrieved.
</td></tr><tr><td>Offset</td><td>Specify the index of the first item to be returned by this operation. This parameter is useful if you want to get a subset of records, say records starting from the 10th index.
</td></tr><tr><td>Limit</td><td>Specify the maximum number of records that this operation should return. By default it will return all records.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get Executive Report Results By Assessment ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Assessment ID</td><td>Specify the assessment ID whose Web Application Firewall executive report results is to be retrieved.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get WAF Site IDs
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get WAF Sites
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get WAF Templates
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get WAF Template By ID
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Template ID</td><td>Specify the template ID whose Web Application Firewall template is to be retrieved.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
### operation: Get WAF Assessment Status
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Assessment ID</td><td>Specify the assessment ID. If an ID is not provided, the request will return the latest run assessment.
</td></tr></tbody></table>

#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - cymulate-web-application-firewall - 1.0.0` playbook collection comes bundled with the Cymulate Web Application Firewall - BAS connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Cymulate Web Application Firewall - BAS connector.

- Get WAF Report Results
- Get WAF Site Results
- Get WAF Payload Response
- Get Technical Report Results
- Launch WAF Assessment
- Stop WAF Assessment
- Get WAF Assessment History
- Get Technical Report Results By Assessment ID
- Get Executive Report Results By Assessment ID
- Get WAF Site IDs
- Get WAF Sites
- Get WAF Templates
- Get WAF Template By ID
- Get WAF Assessment Status

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.

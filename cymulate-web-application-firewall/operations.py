"""
Copyright start
Copyright (C) 2008 - 2024 FortinetInc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end
"""

from requests import request, exceptions as req_exceptions
from connectors.core.connector import get_logger, ConnectorError
from datetime import datetime


logger = get_logger("cymulate-web-application-firewall")


class CymulateWebApplicationFirewall:
    def __init__(self, config, *args, **kwargs):
        server_url = config.get("server_url").strip('/')
        if not server_url.startswith('https://') and not server_url.startswith('http://'):
            server_url = "https://" + server_url
        self.url = server_url + "/v1"
        self.api_key = config.get("api_key")
        self.verify_ssl = config.get("verify_ssl")

    def api_request(self, endpoint, method="GET", params={}, data={}):
        try:
            endpoint = self.url + endpoint
            headers = {"x-token": self.api_key}
            response = request(method, endpoint, headers=headers, params=params, data=data, verify=self.verify_ssl)

            if response.ok:
                return response.json()
            else:
                if response.text != "":
                    err_resp = response.text
                    error_msg = 'Response [{0}:{1}]'.format(response.status_code, err_resp)
                else:
                    error_msg = 'Response [{0}:{1}]'.format(response.status_code, response.content)
                logger.error(error_msg)
                raise ConnectorError(error_msg)
        except req_exceptions.SSLError:
            logger.error('An SSL error occurred')
            raise ConnectorError('An SSL error occurred')
        except req_exceptions.ConnectionError:
            logger.error('A connection error occurred')
            raise ConnectorError('A connection error occurred')
        except req_exceptions.Timeout:
            logger.error('The request timed out')
            raise ConnectorError('The request timed out')
        except req_exceptions.RequestException:
            logger.error('There was an error while handling the request')
            raise ConnectorError('There was an error while handling the request')
        except Exception as err:
            raise ConnectorError(str(err))


def get_params(params):
    new_params = {}
    for k, v in params.items():
        if v is None or v == "":
            continue
        if k == "schedule":
            v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")
        if k in {"fromDate", "toDate"}:
            v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
        elif k == "sites":
            v = [x.strip() for x in str(v).split(",")]
        new_params[k] = v
    return new_params


def get_waf_report_results(config, params):
    ob = CymulateWebApplicationFirewall(config)
    params = get_params(params)
    return ob.api_request("/waf/attacks", params=params)


def get_waf_site_results(config, params):
    ob = CymulateWebApplicationFirewall(config)
    params = get_params(params)
    return ob.api_request("/waf/ids", params=params)


def get_waf_payload_response(config, params):
    ob = CymulateWebApplicationFirewall(config)
    params = get_params(params)
    return ob.api_request(f"/waf/payload-response/{params['id']}")


def get_technical_report_results(config, params):
    ob = CymulateWebApplicationFirewall(config)
    params = get_params(params)
    site_id = params.pop("SiteID")
    return ob.api_request(f"/waf/attack/technical/{site_id}", params=params)


def launch_waf_assessment(config, params):
    ob = CymulateWebApplicationFirewall(config)
    data = get_params(params)
    return ob.api_request(f"/waf/start/", method="POST", data=data)


def stop_waf_assessment(config, params):
    ob = CymulateWebApplicationFirewall(config)
    params = get_params(params)
    return ob.api_request(f"/waf/stop/", method="POST", params=params)


def get_waf_assessment_history(config, params):
    ob = CymulateWebApplicationFirewall(config)
    params = get_params(params)
    return ob.api_request("/waf/history/get-ids/", params=params)


def get_technical_report_results_by_id(config, params):
    ob = CymulateWebApplicationFirewall(config)
    params = get_params(params)
    assessment_id = params.pop("id")
    return ob.api_request(f"/waf/history/technical/{assessment_id}", params=params)


def get_executive_report_results_by_id(config, params):
    ob = CymulateWebApplicationFirewall(config)
    params = get_params(params)
    assessment_id = params.pop("id")
    return ob.api_request(f"/waf/history/executive/{assessment_id}")


def get_waf_site_ids(config, params):
    ob = CymulateWebApplicationFirewall(config)
    return ob.api_request(f"/waf/site-ids/")


def get_waf_sites(config, params):
    ob = CymulateWebApplicationFirewall(config)
    return ob.api_request(f"/waf/waf-sites/")


def get_waf_templates(config, params):
    ob = CymulateWebApplicationFirewall(config)
    return ob.api_request(f"/waf/templates/")


def get_waf_template_by_id(config, params):
    ob = CymulateWebApplicationFirewall(config)
    params = get_params(params)
    template_id = params.pop("id")
    return ob.api_request(f"/waf/template/{template_id}")


def get_waf_assessment_status(config, params):
    ob = CymulateWebApplicationFirewall(config)
    params = get_params(params)
    return ob.api_request(f"/waf/status/", params=params)


def check_health_ex(config):
    get_waf_report_results(config, {})
    return True


operations = {
    "get_waf_report_results": get_waf_report_results,
    "get_waf_site_results": get_waf_site_results,
    "get_waf_payload_response": get_waf_payload_response,
    "get_technical_report_results": get_technical_report_results,
    "launch_waf_assessment": launch_waf_assessment,
    "stop_waf_assessment": stop_waf_assessment,
    "get_waf_assessment_history": get_waf_assessment_history,
    "get_technical_report_results_by_id": get_technical_report_results_by_id,
    "get_executive_report_results_by_id": get_executive_report_results_by_id,
    "get_waf_site_ids": get_waf_site_ids,
    "get_waf_sites": get_waf_sites,
    "get_waf_templates": get_waf_templates,
    "get_waf_template_by_id": get_waf_template_by_id,
    "get_waf_assessment_status": get_waf_assessment_status
}

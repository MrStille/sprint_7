
SHOULD_LOG = True

class ApiLog:

    @staticmethod
    def log_req(request_url, response):
        if SHOULD_LOG:
            req = "Request:\n"
            req += f"[{response.request.method}] url: {request_url}\n"
            request_body = "---"
            if  response.request is not None and response.request.body is not None:
                   request_body = response.request.body
            req += "payload: "+ request_body +"\n"
            req += "Response:\n"
            req += "Status code: " + str(response.status_code) +"\n"
            req += "Body: "+ response.text +"\n"
            print("\n"+ req)

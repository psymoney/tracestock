from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import requests
import json


class CompanyLookupView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):

        # TODO(SY): implement get_corporate_code method
        def get_corporate_code(name):
            return "00126380"

        def get_financials():
            URI = "https://opendart.fss.or.kr/api/fnlttSinglAcntAll.json"
            API_KEY = "d3f02b844b4afaa11b10e188bc7a092fc1a63f25"
            business_year = 2019
            report_code = 11011

            # Request financial data from external API
            data_response = requests.get(URI, params={
                'crtfc_key': API_KEY,
                'corp_code': corporate_code,
                'bsns_year': business_year,
                'reprt_code': report_code,
                'fs_div': consolidation_key})

            # TODO(SY): add status checking function
            financial_data = json.loads(data_response.text)

            print(json.dumps(financial_data, indent="\t"))

            return financial_data

        # TODO(SY): implement get_financial_reports method
        def get_financial_reports(financials):
            return "abc"

        corporate_name = request.query_params["corporateName"]
        consolidation_key = request.query_params["consolidationKey"]
        if consolidation_key == "True":
            consolidation_key = "CFS"
        else:
            consolidation_key = "OFS"

        # TODO(SY): delete below print code after test
        print(
            f"corporate_name = {corporate_name} \nconsolidation_key = {consolidation_key}")

        corporate_code = get_corporate_code(corporate_name)
        financials = get_financials()

        # TODO(SY): fix Response after implementing get method
        return Response(data={"corporate_name": corporate_name, "consolidation_key": consolidation_key}, status=status.HTTP_200_OK)

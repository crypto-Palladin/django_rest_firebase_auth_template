from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict

from core.models import CustomUser
from core import services


class Initial(APIView):

    def get(self, request, format=None):
        """
        ####*Requires Firebase idToken authentication by using Header:
        <code>'Authorization' : "JWT '<idToken>'"</code>
        """
        response_data = {
            'user': model_to_dict(request.user),
            'firebase_user': request.auth
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request):
        """
        <table class="parameters table table-bordered table-striped">
            <thead>
                <tr>
                    <th>Parameter</th>
                    <th>Value example</th>
                </tr>
            </thead>
            <tbody>
              <tr>
                  <td>"email" </td>
                  <td>"example@gmail.com"</td>
              </tr>
              <tr>
                  <td>"first_name" </td>
                  <td> "Ex" </td>
              </tr>
              <tr>
                  <td>"last_name" </td>
                  <td> "Ample" </td>
              </tr>
              <tr>
                  <td>"zip_code" </td>
                  <td> "01001" </td>
              </tr>
              <tr>
                  <td>"country_of_residence" </td>
                  <td> "Ukraine" </td>
              </tr>
              <tr>
                  <td>"mobile_number" </td>
                  <td> "+380971112233" </td>
              </tr>
            </tbody>
        </table>
        
        ####*Requires Firebase idToken authentication by using Header:
        <code>'Authorization' : "JWT '<idToken>'"</code>
        """
        result = services.put_info_to_user_profile(
            user_id=model_to_dict(request.user)['id'],
            data=request.data
        )

        if result[0]:
            return Response(result[1])
        return Response(result[1], status=status.HTTP_400_BAD_REQUEST)

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import openai
from .models import Chats
from .serializers import ChatsSerializer
import os
from dotenv import load_dotenv
load_dotenv()

@csrf_exempt
@api_view(['POST'])
def getResponse(request):
    postdata = request.POST
    serializer = ChatsSerializer(data=postdata)
    if serializer.is_valid():
        try:
            answer = OpenAI(postdata['question'])
        except Exception as e:
            error = e
            answer = None
        if answer:
            Chats.objects.create(question=postdata['question'],answer=answer)
            status_code = status.HTTP_201_CREATED
            message = "Successful"
            data = {'answer': answer}
        else:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            message = f"Internal servel error {error}"
    else:
        status_code = status.HTTP_400_BAD_REQUEST
        field_names = []

        for field_name, field_errors in serializer.errors.items():
            print(field_name, field_errors)
            field_names.append(field_name)
        message = f'Invalid data in {message}'
        
    return Response({'message':message,'data':data},status=status_code)


def OpenAI(question):
    api_key = os.environ.get("OPENAI_API_KEY")
    openai.api_key = api_key

    # Get the user input from the command line
    user_input = question
    # Send the request to the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"{user_input}"),
        temperature=0.5,
        max_tokens=4000
    )

    # Print the response
    response_string = response["choices"][0]["text"][2:]
    return response_string
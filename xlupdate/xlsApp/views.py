from rest_framework import viewsets
from .models import StudDetail
from .serializers import StudDetailSerializer
from rest_framework.decorators import api_view

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

class StudDetailViewSet(viewsets.ModelViewSet):
    queryset = StudDetail.objects.all()
    serializer_class = StudDetailSerializer

# myapp/views.py


@api_view(['POST'])
def update_database(request):
    # Check if a file is provided in the request
    print(request.FILES)
    if 'file.xlsx' not in request.FILES:
        return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

    # Get the uploaded file
    # print the excel_file
    excel_file = request.FILES['file.xlsx']
    print(excel_file)
    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(excel_file)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Convert DataFrame to a list of dictionaries
    data = df.to_dict(orient='records')


    # Update or create database entries
    for record in data:
        students = StudDetail.objects.filter(roll=record.get("roll"))
        print(students)
        
        if students.exists():
            students.update(
            roll=record.get('roll'),
            sname=record.get('sname'),
            sclass= record.get('sclass'),
            saddress= record.get('saddress'),
            tamil= record.get('tamil'),
            english= record.get('english'),
            maths= record.get('maths'),
            science= record.get('science'),
            socialscience= record.get('socialscience'),
            )
        else:
            StudDetail.objects.create(
            roll=record.get('roll'),
            sname=record.get('sname'),
            sclass= record.get('sclass'),
            saddress= record.get('saddress'),
            tamil= record.get('tamil'),
            english= record.get('english'),
            maths= record.get('maths'),
            science= record.get('science'),
            socialscience= record.get('socialscience'),
            )

    return Response({"status": "success"}, status=status.HTTP_200_OK)

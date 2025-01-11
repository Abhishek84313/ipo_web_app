from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IPOInfo
from .serializers import IPOInfoSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from .forms import IPOInfoForm
from django.contrib import messages
# from django.contrib.auth import logout

class IPOInfoAPI(APIView):

    def get(self, request):
        ipo_info = IPOInfo.objects.all()
        serializer = IPOInfoSerializer(ipo_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = IPOInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def ipo_list_page(request):
        """
        Render the HTML page to display IPOs.
        """
        return render(request, 'ipo_web/ipo_list.html')

    def ipo_list_data(request):
        """
        Return IPO data as JSON (for dynamic updates).
        """
        ipo_info = IPOInfo.objects.all()
        serializer = IPOInfoSerializer(ipo_info, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    @login_required
    def admin_dashboard(request):
        if request.method == 'POST':
            form = IPOInfoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "IPO added successfully!")
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Failed to add IPO. Please check the form.")
        else:
            form = IPOInfoForm()
        return render(request, 'ipo_web/admin_dashboard.html', {'form': form})
    def home_page(request):
        return render(request, 'ipo_web/home_page.html')

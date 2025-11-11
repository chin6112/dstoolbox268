from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token
import json

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

@require_http_methods(["POST"])
def contact(request):
    """Handle contact form submissions"""
    try:
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        
        if not all([name, email, message]):
            return HttpResponse(
                '<div class="p-4 bg-red-900 border border-red-500 rounded-lg text-red-100"><strong>Error:</strong> All fields are required.</div>',
                status=400
            )
        
        # Basic email validation
        if '@' not in email:
            return HttpResponse(
                '<div class="p-4 bg-red-900 border border-red-500 rounded-lg text-red-100"><strong>Error:</strong> Please enter a valid email address.</div>',
                status=400
            )
        
        # Here you can add email sending logic or save to database
        # For now, we'll just return a success message
        
        success_html = f'''
        <div class="p-4 bg-green-900 border border-green-500 rounded-lg text-green-100 animate__animated animate__fadeIn">
            <strong>✓ Message Sent!</strong>
            <p class="mt-2">Thanks {name}! I received your message and will get back to you soon at {email}.</p>
        </div>
        '''
        return HttpResponse(success_html)
        
    except Exception as e:
        return HttpResponse(
            f'<div class="p-4 bg-red-900 border border-red-500 rounded-lg text-red-100"><strong>Error:</strong> {str(e)}</div>',
            status=500
        )
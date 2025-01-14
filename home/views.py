from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode
import json
import datetime
from .models import QRCodeData 

@csrf_exempt
def scan_qr_code(request):
    if request.method == 'POST':
        # Extract PNG image data from request
        image_data = request.FILES.get('image_data')
        
        if not image_data:
            return JsonResponse({'error': 'No image data found in the request'})

        try:
            # Read image data from request
            with Image.open(image_data) as image:
                # Decode QR code using pyzbar
                decoded_objects = decode(image)
                
                if decoded_objects:
                    qr_data = decoded_objects[0].data.decode('utf-8')
                    # Process the QR code data as needed
                    # For example, save to database or return directly
                    json_data = json.loads(qr_data)

                    # Convert the Python object back to a formatted JSON string
                    formatted_json_data = json.dumps(json_data, indent=4)
                    # print(formatted_json_data)


                    qr_code_obj = QRCodeData.objects.create(
                    product_id=formatted_json_data['PRODUCT ID'],
                    product_name=formatted_json_data['PRODUCT NAME'],
                    product_type=formatted_json_data['PRODUCT TYPE'],
                    weight=formatted_json_data['WEIGHT OF THE PRODUCT'],
                    manufacturing_date=datetime.datetime.strptime(formatted_json_data['MANUFACTURING DATE'], '%d/%m/%Y').date(),
                    prize=formatted_json_data['PRICE']
        )
                    print("QR data: ", qr_code_obj)
                    return JsonResponse({'qr_data': formatted_json_data})
                else:
                    return JsonResponse({'error': 'QR code not found or could not be decoded'})
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while processing the image: {}'.format(str(e))})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

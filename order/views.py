from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import OrderSerializer, Order_detailSerializer
from .models import Order, Order_detail
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from user.authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token, access_token_exp
# Create your views here.

class OrderAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            order = Order.objects.filter(o_user=id)
            serializer = OrderSerializer(order, many=True, context={"request": request})
        
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message' : "no auth token"})

    def post(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            
            order_data = {
                "o_user": id, 
                "o_add": request.data["address"], 
                "o_num": request.data["number"], 
                "o_name": request.data["name"], 
                "o_pay": request.data["payment"], 
                "o_total_price": request.data["totalPrice"]
            }
            serializer = OrderSerializer(data=order_data)
            if serializer.is_valid():
                current_order = serializer.save()

                current_order_id = current_order.id

                for item in request.data["items"]:
                    print(item)
                    od_detail_data = {
                        "od_id": current_order_id,
                        "od_pd": item["kitItem"]["pd_id"],
                        "od_quantity": item["count"],
                        "od_price": item["count"] * item["kitItem"]["pd_price"]
                    }
                    detail_serializer = Order_detailSerializer(data=od_detail_data)
                    if detail_serializer.is_valid():
                        detail_serializer.save()
                    else:
                        return Response({'message' : "Error product id: " + str(item["kitItem"]["pd_id"])})
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message' : "no valid order"})
        
        else:
            return Response({'message' : "no auth token"})

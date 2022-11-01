from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import OrderSerializer, Order_detailSerializer
from main.serializer import HobbySerializer
from user.serializer import SubSerializer, Sub_pdSerializer
from .models import Order, Order_detail, Hobby
from user.models import Subscription, Sub_pd
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from user.authentication import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token, access_token_exp
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
# Create your views here.

class OrderAPIView(APIView):
    def get(self, request):
        # 해당 유저 토큰으로 주문정보 필터링 & json직렬화
        order_condition = request.GET.get('type', None)

        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            order_obj = Order.objects.filter(o_user=id)
            serializer = OrderSerializer(order_obj, many=True, context={"request": request})
            order_data = []
            # 반복할 숫자 선언(num) & 직렬화된 데이터에서 주문id 추출 --> 해당 주문 id의 주문 디테일 id 필터링 & json직렬화 
            if order_condition == 'item':
                
                for order in serializer.data:
                    order_pd = Order_detail.objects.filter(od_id=order['id'])
                    detail_serializer = Order_detailSerializer(order_pd, many=True, context={"request": request})
                    detail_serializer = detail_serializer.data
                    
                    detail_order_data = []
                    order_data_obj = {
                        "o_id" : order['id'],
                        "o_add" : order['o_add'],
                        "o_num" : order['o_num'],
                        "o_name" : order['o_name'],
                        "o_pay" : order['o_pay'],
                        "o_total_price" : order['o_total_price'],
                        "o_create" : order['o_create'],
                        "o_items" : detail_order_data
                    }
                    # 반복할 숫자 선언(dict_od_id_num) & 주문 디테일에서 주문한 상품정보 id추출 --> 해당 상품정보 id의 상품 필터링 & json직렬화
                    
                    for order_pd in detail_serializer:
                        
                        order_hobby = Hobby.objects.filter(pd_id=order_pd['od_pd'])
                        hobby_serializer = HobbySerializer(order_hobby, many=True, context={"request": request})
                        hobby_serializer = hobby_serializer.data[0]

                        
                        detail_order_data_obj= {
                            "p_id" : order_pd["od_pd"],
                            "p_quantity" : order_pd['od_quantity'],
                            "p_total_price" : order_pd['od_price'],
                            "p_title" : hobby_serializer['pd_title'],
                            "p_description" : hobby_serializer['pd_descrition'],
                            "p_info" : hobby_serializer['pd_info'],
                            "p_price" : hobby_serializer['pd_price'],
                            "p_sell" : hobby_serializer['pd_sell'],
                            "p_create" : hobby_serializer['pd_create'],
                            "p_image" : hobby_serializer['images']
                        }

                        detail_order_data.append(detail_order_data_obj)
                    if len(detail_serializer) != 0:
                        order_data.append(order_data_obj)
                    
            
            elif order_condition == 'sub':
                
                for order in serializer.data:
                    
                    order_pd = Subscription.objects.filter(order_id=order['id'])
                    sub_serializer = SubSerializer(order_pd, many=True, context={"request": request})
                
                    if len(sub_serializer.data) == 0:
                        continue
                    sub_serializer = sub_serializer.data[0]
    
                    subpd = Sub_pd.objects.filter(id=sub_serializer['subpd_id'])
                    subpd_serializer = Sub_pdSerializer(subpd, many=True, context={"request": request})
                    subpd_serializer = subpd_serializer.data[0]
                    
                    sub_order_data = []
                    order_data_obj = {
                        "o_id" : order['id'],
                        "o_add" : order['o_add'],
                        "o_num" : order['o_num'],
                        "o_name" : order['o_name'],
                        "o_pay" : order['o_pay'],
                        "o_total_price" : order['o_total_price'],
                        "o_create" : order['o_create'],
                        "o_items" : sub_order_data
                    }
                    detail_order_data_obj = {
                        "sub_id" : sub_serializer['id'],
                        "s_id" : subpd_serializer['id'],
                        "s_title" : subpd_serializer['title'],
                        "s_body" : subpd_serializer['body'],
                        "s_price" : subpd_serializer['price'],
                        "s_sub_image" : subpd_serializer['sub_image'],
                        "s_create" : sub_serializer['create_time'],
                        "s_delete" : sub_serializer['delete_time']
                    }
                    sub_order_data.append(detail_order_data_obj)
                    order_data.append(order_data_obj)
                
            return Response({
                        "order" : order_data,
                    }, status=status.HTTP_200_OK)

        else:
            return Response({'message' : "no auth token, order_condition: " + order_condition})

    def post(self, request):
        paginator = PageNumberPagination()
        order_condition = request.GET.get('type', None)

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
                "o_total_price": request.data["totalPrice"],
            }
            serializer = OrderSerializer(data=order_data)
            if serializer.is_valid():
                current_order = serializer.save()

                current_order_id = current_order.id
                
                if order_condition == 'item': #상품 주문시 order post

                    for item in request.data["items"]:
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
                
                elif order_condition == 'sub':
                    
                    for sub in request.data["items"]:
                        
                        od_sub_data = {
                            "order_id": current_order_id,
                            "subpd_id": sub["id"],
                            "user_id": id
                        }
                        subSerializer = SubSerializer(data=od_sub_data)
                        
                        if subSerializer.is_valid():
                            subSerializer.save()
                        else:
                            return Response({'message' : "Error subpd_id: " + str(sub["id"])})
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message' : "no valid order"})
        
        else:
            return Response({'message' : "no auth token"})


            

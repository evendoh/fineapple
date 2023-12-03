from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserProfileEditSerializer, UserFinancialEditSerializer, UserFinancialMBTIEditSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status

### USER 정보 수정 하는 함수 만들기

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_profile_edit(request):
    user_profile = get_object_or_404(User, username=request.user.username)

    if request.method == 'PUT':
        serializer = UserProfileEditSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_profile.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user_profile.delete()
        return Response({'detail': '사용자 프로필이 성공적으로 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)

    return Response({'detail': '허용되지 않은 메서드입니다.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_financial_edit(request):
    user = get_object_or_404(User, username=request.user.username)
    print(user.financial_products)
    new_financial_product = request.data.get('financial_product')
    print(request.data.get('financial_product'))
    
    # financial_products 필드가 문자열이므로 직접 추가 또는 제거
    if user.financial_products:
        # 기존 항목이 존재하면 쉼표로 구분된 문자열을 리스트로 변환
        existing_products = user.financial_products.split(',')
        
        if new_financial_product in existing_products:
            # 이미 있는 경우 제거
            existing_products.remove(new_financial_product)
            print(1)
        else:
            # 없는 경우 추가
            print(2)
            existing_products.append(new_financial_product)
        
        # 리스트를 다시 쉼표로 구분된 문자열로 변환하여 저장
        user.financial_products = ','.join(existing_products)
    else:
        user.financial_products = new_financial_product
    
    print(user.financial_products)

    # 위에서 financial_products를 직접 조작했기 때문에 따로 저장해야 함
    user.save()
    print(3)

    serializer = UserFinancialEditSerializer(instance=user, data={'financial_products': user.financial_products}, partial=True)

    if request.method == 'PUT':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_mbti_edit(request):
    user = get_object_or_404(User, username=request.user.username)
    if request.method == 'PUT':
        if user.mbti != []:
            user.mbti = ''
            user.save()
        print(request.data)
        serializer = UserFinancialMBTIEditSerializer(instance=user, data=request.data)
        # serializer = UserFinancialMBTIEditSerializer(instance=user, data={'mbti': user.mbti}, partial=True)
        if serializer.is_valid():
            serializer.save()
            # print('2', serializer.data.mbti)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_mbti(request):
    if request.method == 'GET':
        # 현재 요청한 유저의 mbti 정보 가져오기
        requesting_user = request.user
        requesting_user_mbti = requesting_user.mbti

        # mbti가 같은 다른 유저들 필터링
        users_with_same_mbti = User.objects.filter(mbti=requesting_user_mbti)
        # 빈 딕셔너리 초기화
        result_dict = {}

        # 각 유저들의 financial_products 리스트를 분석하여 딕셔너리에 저장
        for user in users_with_same_mbti:
            print(user)
            if not user.financial_products:

                continue
            financial_products_list = user.financial_products.split(',')
            print('?', financial_products_list)
            for product in financial_products_list:
                product = product.strip()  # 앞뒤 공백 제거
                print('!', product)
                # 딕셔너리에 이미 키가 존재하는지 확인하고 없으면 추가, 있으면 값을 증가
                if product in result_dict:
                    result_dict[product] += 1
                else:
                    result_dict[product] = 1
            print(result_dict)
        # 딕셔너리를 값에 따라 내림차순으로 정렬
        sorted_result = dict(sorted(result_dict.items(), key=lambda item: item[1], reverse=True))
        top_10_keys = list(sorted_result.keys())[:10]


        return Response(top_10_keys)
    else:
        return Response({'error': 'Only GET requests are allowed.'})



# # profile 조회
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_profile_detail(request):
#     user = request.user
#     serializer = UserProfileSerializer(user)
#     return Response(serializer.data)



# def profile(request, user_pk):
#     User = get_user_model()
#     person = User.objects.get(pk=user_pk)
#     # user = request.user
#     context = {
#         'person' : person
#     }
#     return render(request, 'accounts/profile.html', context)


# # # @login_required
# # def follow(request, user_pk):
# #     if request.user.is_authenticated:
# #         User = get_user_model()
# #         you = User.objects.get(pk=user_pk)
# #         me = request.user
# #         if you != me:
# #             if you.followers.filter(pk=request.user.pk).exists():
# #                 you.followers.remove(me)
# #             else:
# #                 you.followers.add(me)
# #         return redirect("accounts:profile", you.pk)
# #     return redirect("accounts:login")


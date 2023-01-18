# from django.http import JsonResponse
# from django.core import serializers
from .models import Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CategorySerializer


# @api_view()
# def categories(request):
#     all_categories = Category.objects.all()
#     serializer = CategorySerializer(all_categories, many=True)

#     return Response({
#         "ok": True,
#         # "cateogories": serializers.serialize("json", all_categories)
#         "categories": serializer.data,
#     })

@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)

    # elif request.method == "POST":
    #     print("post를 위한 요청 데이터 : ", request.data)
    #     serailizer = CategorySerializer(data=request.data)
    #     print(serailizer.is_valid())
    #     print(serailizer.errors)
    #     return Response({"created": True})
    elif request.method == "POST":
        print(request.data)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            # return Response({"created": True})
            new_category = serializer.save()
            return Response(
                CategorySerializer(new_category).data,
            )            
        else:
            return Response(serializer.errors)


# pk 로 카테고리 조회 for url pk
@api_view()
def category(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

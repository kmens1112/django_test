from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator

# Create your views here.

class books_list(View):
    context = {}
    template_name = 'books_list.html' #기본 템플릿 이름 설정

    #GET 통신
    def get(self,request):    
        books = Book.objects.all()
        page = int(request.GET.get('page', 1)) #페이지값을 전달받지 못하면 1로 설정
        # 해당 통신이 Ajax인지 확인 -> 페이지네이션 요청인지 확인하는 방법
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        	# Ajax라면 표현할 페이지 템플릿을 변경
            self.template_name = 'books_table.html'
        # 페이지네이터로 구분 -> 5개 아이템을 표시
        paginator = Paginator(books, 5)
        # 페이지 선택
        books_list = paginator.get_page(page)
        #도서 리스트를 저장
        self.context = {"books_list":books_list}
        return render(request, self.template_name, self.context) 
       
    #POST 통신
    def post(self,request):
        return render(request, self.template_name, self.context)
    
class books_detail(View):
    context = {}
    template_name = 'books_detail.html'

    def get(self, request):
        return render(request, self.template_name, self.context)
    def post(self, request):
        
        return render(request, self.template_name, self.context)
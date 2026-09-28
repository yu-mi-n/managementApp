from django.shortcuts import render
from .models import Worker

def dashboard(request):
    context = {'name': 'Juan', 'balance': '350.00', 'target': '500.00', 'progress': 70}
    return render(request, 'dashboard.html', context)

def learning(request):
    return render(request, 'learning.html')

def call_screen(request):
    return render(request, 'call.html')

def learning(request):
    # 学習リスト画面（スクリーンショットのデザインを反映）
    return render(request, 'learning.html')

def lesson_detail(request, lesson_id):
    # リストを押した先の動画プレイヤー画面
    return render(request, 'lesson_detail.html', {'lesson_id': lesson_id})

def standby(request):
    return render(request, 'standby.html')

from .models import TodoItem, TodoHistory
from django.shortcuts import render
from django.http import HttpResponseRedirect


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
                  {'all_items': all_todo_items})


def todoHistory(request):
    all_todo_items = TodoHistory.objects.all()
    return render(request, 'history.html',
                  {'all_hist_items': all_todo_items})


def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    hist_item = TodoHistory(hist_content = request.POST['content'])
    hist_item.save()
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')





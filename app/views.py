from django.shortcuts import render
from .forms import SampleForm


def top(request):
    form = SampleForm(request.POST or None)
    # 采用保留form里面所有值的方法，保留checkbox的状态
    context = {'form': form}
    print("qiulongquan_form={}".format(form))
    if form.is_valid():
        tags = form.cleaned_data.get('tags')
        if tags:
            print("qiulongquan_tags={}".format(tags))
    return render(request, 'app/top.html', context)

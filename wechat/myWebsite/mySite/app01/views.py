#coding=utf-8
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
import subprocess
from django.shortcuts import HttpResponse
# Create your views here.
def home(request):
    return render(request,'22.html')
class Home(View):
    def get(self,request):
        def run_code(code):
            try:
                output = subprocess.check_output(['python', '-c', code],
                                                 universal_newlines=True,
                                                 stderr=subprocess.STDOUT,
                                                 timeout=5)
            except subprocess.CalledProcessError as e:
                output = e.output
            except subprocess.TimeoutExpired as e:
                output = '\r\n'.join(['Time Out!!!', e.output])
            return output
       
        code = "import numpy\nimport numpy.linalg as ng\n"
        m1 = request.GET.get('m1')
        m2 = request.GET.get("m2")
        m3 = request.GET.get("m3")
        m4 = request.GET.get("m4")
        m5 = request.GET.get("m5")
        data = request.GET.get("command")
        result = "result="
        data = result+data+"\n"+"print(result)"
        if m1:
            code = code + "m1=" + m1 + "\n" + "m1=numpy.mat(m1)\n"
        if m2:
            code = code + "m2=" + m2 + "\n" + "m2=numpy.mat(m2)\n"
        if m3:
            code = code + "m3=" + m3 + "\n" + "m3=numpy.mat(m3)\n"
        if m4:
            code = code + "m4=" + m4 + "\n" + "m4=numpy.mat(m4)\n"
        if m5:
            code = code + "m5=" + m5 + "\n" + "m5=numpy.mat(m5)\n"
        code = code + data
        output = run_code(code)
        # m1 = m1+data
        return JsonResponse(data={'data':output})

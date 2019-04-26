from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class VerifycodeMiddleware(MiddlewareMixin):
   def process_request(self, request):
       print("***************", request.path)
       if request.path == "/useradd/" and request.method == "POST":
           # 判断验证码
           verifycode = request.POST.get("verifycode")
           if not verifycode.upper() == request.session.get("verifycode").upper():
               return redirect("/useradd/")
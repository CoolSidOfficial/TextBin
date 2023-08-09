from django.shortcuts import render

def index(request):
    return render(request, 'index.html')    


def text_to_binary(request):
   dtext=request.GET.get('data','default')
   final_text="".join(format(ord (bits),"08b")for bits in dtext)

   # final_text=bin(int.from_bytes(dtext.encode(), 'big'))
   conv={"ttb":str(final_text)}
   return  render(request, 'index.html',conv)
def binary_to_text(request):
   dtext=request.GET.get('data','default')

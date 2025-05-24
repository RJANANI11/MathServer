from django.shortcuts import render

def powercalc(request):
    context = {}
    context['P'] = "0"
    context['I'] = "0"
    context['R'] = "0"

    if request.method == "POST":
        print("POST method is used")
        I = request.POST.get('current', '0')
        R = request.POST.get('resistance', '0')
        print("Current =", I)
        print("Resistance =", R)

        try:
            power = int(float(I)) ** 2 * int(float(R))
            context['P'] = power
        except ValueError:
            context['P'] = "Invalid input"
        
        context['I'] = I
        context['R'] = R
        print("Power =", context['P'])

    return render(request, 'mathapp/math.html', context)
from django.shortcuts import render
from .forms import ValuationForm

def calculate_exit_multiple(ebitda):
    # Example: Exit multiple based on EBITDA
    industry_multiple = 10  # This can be dynamic or retrieved from Excel
    return ebitda * industry_multiple

def calculate_target(revenue, growth_rate):
    # Example: Target price based on revenue and growth rate
    return revenue * (1 + growth_rate)

def calculate_up_down(current_price, target_price):
    # Example: Up/(Down) percentage
    return ((target_price - current_price) / current_price) * 100

def valuation_view(request):
    if request.method == 'POST':
        form = ValuationForm(request.POST)
        if form.is_valid():
            revenue = form.cleaned_data['revenue']
            ebitda = form.cleaned_data['ebitda']
            growth_rate = form.cleaned_data['growth_rate']
            current_price = form.cleaned_data['current_price']

            # Perform calculations
            exit_multiple = calculate_exit_multiple(ebitda)
            target_price = calculate_target(revenue, growth_rate)
            up_down = calculate_up_down(current_price, target_price)

            return render(request, 'valuations/result.html', {
                'exit_multiple': exit_multiple,
                'target_price': target_price,
                'up_down': up_down
            })
    else:
        form = ValuationForm()
    
    return render(request, 'valuations/valuation.html', {'form': form})

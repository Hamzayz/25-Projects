from flask import Flask, render_template, request
import func


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            # Get form data
            value = float(request.form['value'])
            category = request.form['category']
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            
            # Perform conversion based on category
            if category == 'length':
                result = func.convert_length(value, from_unit, to_unit)
            elif category == 'weight':
                result = func.convert_weight(value, from_unit, to_unit)
            elif category == 'temperature':
                result = func.convert_temperature(value, from_unit, to_unit)
            
            # Format result
            result = f"{value} {from_unit} = {result:.4f} {to_unit}"
            
        except ValueError:
            error = "Please enter a valid number"
        except KeyError:
            error = "Invalid unit selection"
        except Exception as e:
            error = f"Error: {str(e)}"
    
    return render_template('main.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
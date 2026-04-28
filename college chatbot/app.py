
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def process_query(user_input, is_first=False):
    """
    Enhanced query processor with dynamic buttons for step-by-step flow.
    Returns dict: {'response': str, 'buttons': list of {'label':str, 'value':str} or None}
    """
    user_input = user_input.lower().strip() if user_input else ''
    
    # Welcome for first interaction
    if is_first or not user_input:
        main_buttons = [
            {'label': 'Courses', 'value': 'courses'},
            {'label': 'Fees', 'value': 'fees'},
            {'label': 'Admission', 'value': 'admission'},
            {'label': 'Hostel', 'value': 'hostel'},
            {'label': 'Placement', 'value': 'placement'}
        ]
        return {
            'response': 'Welcome to College Enquiry Bot 🤖\nHow can I help you today?',
            'buttons': main_buttons
        }
    
    # Back to main menu
    if user_input in ['back', 'main', 'menu']:
        main_buttons = [
            {'label': 'Courses', 'value': 'courses'},
            {'label': 'Fees', 'value': 'fees'},
            {'label': 'Admission', 'value': 'admission'},
            {'label': 'Hostel', 'value': 'hostel'},
            {'label': 'Placement', 'value': 'placement'}
        ]
        return {
            'response': 'Back to main menu. Choose an option:',
            'buttons': main_buttons
        }
    
    # COURSES flow
    if any(word in user_input for word in ['course', 'courses', '1', 'courses']):
        sub_buttons = [
            {'label': 'B.Tech CS', 'value': 'btech_cs'},
            {'label': 'BCA', 'value': 'bca'},
            {'label': 'Back to Main', 'value': 'main'}
        ]
        return {
            'response': 'Available Courses:\n• B.Tech Computer Science (4 yrs)\n• B.Tech Mechanical (4 yrs)\n• BCA (3 yrs)\n• MBA (2 yrs)',
            'buttons': sub_buttons
        }
    elif 'btech_cs' in user_input:
        return {
            'response': 'B.Tech CS Details:\n• Seats: 120\n• Eligibility: 12th PCM 60%\n• Sem Fees: ₹60,000\n• Labs: AI, Cloud, Cybersecurity',
            'buttons': [{'label': 'More Info / Back', 'value': 'main'}]
        }
    elif 'bca' in user_input:
        return {
            'response': 'BCA Details:\n• Seats: 60\n• Eligibility: 12th any stream 50%\n• Sem Fees: ₹40,000\n• Focus: Programming, Web Dev',
            'buttons': [{'label': 'More Info / Back', 'value': 'main'}]
        }
    
    # FEES flow
    elif any(word in user_input for word in ['fee', 'fees', 'cost', '2', 'fees']):
        sub_buttons = [
            {'label': 'B.Tech Fees', 'value': 'btech_fees'},
            {'label': 'BCA/MBA Fees', 'value': 'bca_mba_fees'},
            {'label': 'Back to Main', 'value': 'main'}
        ]
        return {
            'response': 'Annual Fee Structure:\n• B.Tech: ₹1,20,000\n• BCA: ₹80,000\n• MBA: ₹2,50,000\n(Scholarships available)',
            'buttons': sub_buttons
        }
    elif 'btech_fees' in user_input:
        return {
            'response': 'B.Tech Fees Breakdown:\n• Tuition: ₹90,000\n• Hostel+Mess: ₹30,000\n• Total: ₹1,20,000/year',
            'buttons': [{'label': 'Back to Main', 'value': 'main'}]
        }
    # ... similar for other subs
    
    # ADMISSION
    elif any(word in user_input for word in ['admission', 'apply', 'enroll', '3']):
        sub_buttons = [
            {'label': 'B.Tech Process', 'value': 'btech_admit'},
            {'label': 'Documents Needed', 'value': 'docs'},
            {'label': 'Back to Main', 'value': 'main'}
        ]
        return {
            'response': 'Admission Steps:\n1. Online Form\n2. Entrance Test\n3. Counseling\n4. Documents & Fees',
            'buttons': sub_buttons
        }
    
    # HOSTEL
    elif any(word in user_input for word in ['hostel', 'dorm', '4']):
        sub_buttons = [
            {'label': 'Boys Hostel', 'value': 'boys_hostel'},
            {'label': 'Girls Hostel', 'value': 'girls_hostel'},
            {'label': 'Back to Main', 'value': 'main'}
        ]
        return {
            'response': 'Hostel Info:\n• Capacity: 500+ students\n• Cost: ₹60,000/year (mess incl.)\n• WiFi, Laundry, Gym',
            'buttons': sub_buttons
        }
    
    # PLACEMENT
    elif any(word in user_input for word in ['placement', 'job', '5']):
        sub_buttons = [
            {'label': '2023 Stats', 'value': '2023_stats'},
            {'label': 'Top Companies', 'value': 'companies'},
            {'label': 'Back to Main', 'value': 'main'}
        ]
        return {
            'response': 'Placement Highlights:\n• Rate: 85%\n• Avg Package: ₹5.5 LPA\n• Highest: ₹32 LPA',
            'buttons': sub_buttons
        }
    
    # Default
    default_buttons = [
        {'label': 'Courses', 'value': 'courses'},
        {'label': 'Fees', 'value': 'fees'},
        {'label': 'Admission', 'value': 'admission'},
        {'label': 'Hostel', 'value': 'hostel'},
        {'label': 'Placement', 'value': 'placement'}
    ]
    return {
        'response': 'Please choose an option above or ask about courses, fees, admission, hostel, or placement.',
        'buttons': default_buttons
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    # First chat: is_first=True
    bot_data = process_query(user_message, is_first=(not user_message))
    return jsonify(bot_data)

if __name__ == '__main__':
    app.run(debug=True)


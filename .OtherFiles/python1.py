from flask import Flask, send_file, flash, redirect, render_template
import pandas as pd
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Sample dataframe
df = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 22]
})

# Route to download the Excel file and show a flash message
@app.route('/download_excel')
def download_excel():
    try:
        # Create an in-memory Excel file
        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Sheet1', index=False)

        excel_buffer.seek(0)

        # Send the Excel file as a downloadable attachment
        send_file(
            excel_buffer,
            download_name='sample_dataframe.xlsx',
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True
        )

        # Flash a success message
        flash("File download successful!", 'success')

        # Redirect to the home page or any other route
        return redirect('/')

    except Exception as e:
        # Flash an error message
        flash(f"An error occurred: {str(e)}", 'error')

        # Redirect to the home page or any other route
        return redirect('/')

# Route to display flash messages (optional)
@app.route('/')
def index():
    # Retrieve and display flash messages
    success_messages = [message[1] for message in flashes() if 'success' in message[1]]
    error_messages = [message[1] for message in flashes() if 'error' in message[1]]
    return render_template('index.html', success_messages=success_messages, error_messages=error_messages)

if __name__ == '__main__':
    app.run(debug=True)

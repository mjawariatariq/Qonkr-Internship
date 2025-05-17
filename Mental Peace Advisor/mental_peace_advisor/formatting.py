import re

def format_bot_message_html(message: str) -> str:
    # Yeh function bot ke text ko HTML format mein convert karta hai
    # Taake message Streamlit mein achi tarah style ho kar dikhai de

    lines = message.split('\n')  # Message ko lines mein split karna
    ul_open = False              # Track karta hai ke <ul> tag khula hai ya nahi (list ka start)
    html = ""                    # HTML output store karne ke liye variable
    previous_line_empty = False  # Empty line track karne ke liye, takay multiple <br> na lage

    for line in lines:
        stripped_line = line.strip()  # Har line se extra spaces hata dena

        # Agar line bullet point jaisi ho (* ya - se start ho)
        if stripped_line.startswith(('* ', '- ')):
            if not ul_open:
                # Agar list start nahi hui to <ul> tag open karo
                html += '<ul style="margin:10px 0; padding-left:20px; line-height:1.6;">'
                ul_open = True
            # Bullet point ka actual content nikaalna
            content = stripped_line[2:].strip()
            # Content mein agar **bold** likha ho to usko <b> tag mein convert karna
            content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', content)
            # Har bullet point ko <li> tag mein wrap karna
            html += f"<li>{content}</li>"
            previous_line_empty = False

        # Agar line blank hai (empty line)
        elif stripped_line == "":
            if ul_open:
                # Agar list chal rahi hai to close kar dena
                html += "</ul>"
                ul_open = False
            # Agar pehle bhi empty line nahi thi to ek <br> tag add karo
            if not previous_line_empty:
                html += "<br>"
                previous_line_empty = True  # Mark karna ke abhi <br> add hua hai

        else:
            # Agar ye normal paragraph wali line hai
            if ul_open:
                # Agar list open hai to pehle usko close karo
                html += "</ul>"
                ul_open = False
            # Paragraph mein **bold** text ko <b> tag mein convert karo
            content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', stripped_line)
            # Paragraph ko <p> tag mein style karke add karo
            html += f'<p style="margin:10px 0; line-height:1.5;">{content}</p>'
            previous_line_empty = False

    # Agar loop ke end tak list open hai to usko close karna
    if ul_open:
        html += "</ul>"

    # Final formatted HTML return karna
    return html

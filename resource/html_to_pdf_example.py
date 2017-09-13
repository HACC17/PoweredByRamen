import pdfkit	# installed via pip

options = {
            'quiet': '',
            'page-size': 'B4',
            'margin-top': '0.45in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '2.00in',
            'disable-smart-shrinking': ''
        }
		
#pdfkit.from_url('http://google.com', 'out.pdf')
pdfkit.from_file('demo.html', 'out.pdf', 'options'=options)
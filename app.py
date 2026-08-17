import os
import re
from contextlib import contextmanager
from nicegui import app, ui

# Serve current directory files under the '/static' route
app.add_static_files('/static', '.')

# --- SHARED LAYOUT FRAME (Header & Footer) ---
@contextmanager
def page_layout():
    # --- HEADER WITH DARK BLUE BACKGROUND ---
    with ui.header().classes('bg-slate-900 text-white p-4 row items-center justify-between'):
        
        # --- FIXED LOGO DISPLAY ---
        # Using ui.element('img') keeps the native aspect ratio and respects h-10 w-auto
        with ui.row().classes('items-center gap-3'):
            ui.element('img').props('src="/static/logo.png"').classes('h-18 w-auto cursor-pointer') \
                .on('click', lambda: ui.navigate.to('/'))
            
          
        # --- NAVIGATION LINKS ---
        with ui.row().classes('items-center gap-4'):
            ui.link('Home', '/').classes('text-white no-underline hover:underline')
            ui.link('About Us', '/about-us').classes('text-white no-underline hover:underline')
            ui.link('Services', '/services').classes('text-white no-underline hover:underline')
            ui.link('Industries', '/industries').classes('text-white no-underline hover:underline')
            ui.link('TexSource', '/texsource').classes('text-white no-underline hover:underline')
            ui.link('Advance EMI Calculator', '/advance-emi-calculator').classes('text-white no-underline hover:underline')
            ui.link('Contact', '/contact').classes('text-white no-underline hover:underline')
            
            # CTA BUTTON
            ui.button('Free Consultation', icon='mail', on_click=lambda: ui.navigate.to('/contact')) \
                .props('color=blue-6 rounded')

    # Main content container
    with ui.column().classes('w-full max-w-6xl mx-auto p-6 min-h-screen'):
        yield
      
    # Standard HTML <footer> container that scrolls naturally
    with ui.element('footer').classes('bg-slate-900 text-slate-300 p-8 flex-col items-center gap-6 w-full mt-auto'):
        
        # 1. OFFICE ADDRESSES GRID (2 Columns on Desktop)
        with ui.row().classes('w-full max-w-5xl justify-between gap-8 text-sm'):
            # 0. BRAND HEADER / COMPANY NAME (Top Left alignment above columns)
            with ui.row().classes('w-full max-w-5xl justify-start'):
                ui.label('Pro Fincap Services LLP').classes('text-xl font-extrabold text-blue-400 tracking-wide mb-2')
            # --- BHILWARA OFFICE ---
            with ui.column().classes('flex-1 min-w-[280px] gap-2'):
                with ui.row().classes('items-center gap-2 text-white font-bold text-base'):
                    ui.icon('location_on', size='sm').classes('text-blue-400')
                    ui.label('Bhilwara Office')
                
                ui.label('34, Ground Floor, New Cloth Market, Pur Road, Bhilwara, PIN-311001 (Raj)').classes('text-slate-400')
                
                with ui.row().classes('items-center gap-2 mt-1'):
                    ui.icon('phone', size='xs').classes('text-blue-400')
                    ui.link('+91 8107299881', 'tel:+918107299881').classes('text-slate-300 no-underline hover:text-white')
                
                with ui.row().classes('items-center gap-2'):
                    ui.icon('email', size='xs').classes('text-blue-400')
                    ui.link('info@thefincap.com', 'mailto:info@thefincap.com').classes('text-slate-300 no-underline hover:text-white')
                    ui.label('|')
                    ui.icon('language', size='xs').classes('text-blue-400')
                    ui.link('www.thefincap.com', 'https://www.thefincap.com', new_tab=True).classes('text-slate-300 no-underline hover:text-white')

            # --- UDAIPUR OFFICE ---
            with ui.column().classes('flex-1 min-w-[280px] gap-2'):
                with ui.row().classes('items-center gap-2 text-white font-bold text-base'):
                    ui.icon('location_on', size='sm').classes('text-blue-400')
                    ui.label('Udaipur Office')
                
                ui.label('Plot No. 5, First Floor, Mayank Colony, Near State Bank of India, 100 feet road Shobhagpura, Near Zudio Chouraha, Udaipur, Rajasthan - 313001 (Raj)').classes('text-slate-400')
                
                with ui.row().classes('items-center gap-2 mt-1'):
                    ui.icon('phone', size='xs').classes('text-blue-400')
                    ui.link('+91 9920218033', 'tel:+919920218033').classes('text-slate-300 no-underline hover:text-white')

        # DIVIDER LINE
        ui.element('div').classes('w-full max-w-5xl h-px bg-slate-800 my-2')

        # 2. LOCATIONS BAR & SOCIAL MEDIA ICONS
        with ui.row().classes('w-full max-w-5xl justify-between items-center flex-wrap gap-4'):
            
            # Global Presence Tagline
            with ui.row().classes('items-center gap-2 text-xs font-semibold text-slate-400 tracking-wider'):
                ui.label('BHILWARA').classes('text-blue-400')
                ui.label('|')
                ui.label('UDAIPUR').classes('text-blue-400')
                ui.label('|')
                ui.label('DUBAI').classes('text-blue-400')

            # Social Media Icon Links
            with ui.row().classes('items-center gap-1'):
                # Facebook
                ui.button(icon='facebook', on_click=lambda: ui.navigate.to('https://www.facebook.com/thefincapservices/', new_tab=True)) \
                    .props('flat round color=white size=sm').tooltip('Facebook')
                
                # Instagram (using photo icon)
                ui.button(icon='photo_camera', on_click=lambda: ui.navigate.to('https://www.instagram.com/thefincapservices/', new_tab=True)) \
                    .props('flat round color=white size=sm').tooltip('Instagram')
                
                # LinkedIn (using work/business icon)
                ui.button(icon='business', on_click=lambda: ui.navigate.to('https://in.linkedin.com/company/the-fincap-services', new_tab=True)) \
                    .props('flat round color=white size=sm').tooltip('LinkedIn')
                
                # YouTube
                ui.button(icon='play_circle_filled', on_click=lambda: ui.navigate.to('https://www.youtube.com/channel/UCMZGsjiyrWANUWpOeBJXBdQ', new_tab=True)) \
                    .props('flat round color=white size=sm').tooltip('YouTube')
                
                # WhatsApp (Direct Chat Link)
                ui.button(icon='chat', on_click=lambda: ui.navigate.to('https://wa.me/918107299881', new_tab=True)) \
                    .props('flat round color=green-5 size=sm').tooltip('WhatsApp')

        # 3. COPYRIGHT
        ui.label('© 2026 The Fincap Services. All rights reserved.').classes('text-xs text-slate-500 mt-2')
    pass
# --- PAGE 1: HOME PAGE ---
@ui.page('/')
def home_page():
    with page_layout():
        
        # --- HERO & INTRO BANNER ---
        with ui.card().classes('w-full p-8 bg-slate-800 text-white rounded-xl shadow-lg my-4'):
            ui.label('Strategic & Financial Advisory').classes('text-sm font-bold tracking-widest text-blue-400 uppercase mb-1')
            ui.label('Empowering Enterprise Growth').classes('text-3xl font-extrabold text-white mb-4')
            
            ui.label(
                'At FinCap we provide Strategic and Financial Advisory Services, Fund Raising, Banking, '
                'Project Finance, M&A, Valuation, GST, FPO solutions to enterprises. We provide competitive advantage, '
                'centre of expertise, improved processes and cost effectiveness.'
            ).classes('text-slate-300 text-base leading-relaxed mb-3')
            
            ui.label(
                'It’s our preferred model for companies to add more value by moving up in the value chain and focus on core '
                'activities of the operations. We see CFO shared services as a niche segment and in the near future will continue '
                'to mature with advancement of technology and secure business environment.'
            ).classes('text-slate-300 text-base leading-relaxed')

        # --- MD LEADERSHIP & PHILOSOPHY STATEMENT WITH PHOTO ---
        with ui.card().classes('w-full p-6 bg-slate-100 border-l-8 border-blue-600 rounded-r-xl my-6 shadow-sm'):
            with ui.row().classes('items-center gap-6 w-full flex-col sm:flex-row'):
                
                # Circular Headshot Photo
                ui.element('img').props('src="/static/md.png"') \
                    .classes('w-32 h-32 rounded-full object-cover border-4 border-white shadow-md shrink-0')
                
                # Quote & Designation
                with ui.column().classes('flex-1 gap-2'):
                    ui.icon('format_quote', size='md').classes('text-blue-600')
                    ui.label(
                        '“FinCap operates on the principle of sustainable excellence. We empower organizations to convert core competencies into agile, high-strength business models—ensuring strategic direction aligns with sustained growth.”'
                    ).classes('text-slate-800 text-base sm:text-lg italic leading-relaxed font-medium')
                    
                    with ui.row().classes('items-center gap-2 mt-2'):
                        ui.label('Praveen Chandalia').classes('text-base font-bold text-slate-900')
                        ui.label('Managing Director').classes('text-xs font-bold text-blue-700 bg-blue-100 px-2.5 py-0.5 rounded-full')

        # --- BUSINESS VERTICALS SECTION ---
        ui.label('Business Verticals').classes('text-2xl font-bold text-slate-800 mt-6 mb-4')
        
        verticals = [
            {
                'title': 'Corporate & Trade Finance', 
                'icon': 'account_balance', 
                'desc': 'Structured trade credit, working capital, and corporate finance solutions.'
            },
            {
                'title': 'FPO Solutions', 
                'icon': 'groups', 
                'desc': 'Comprehensive Farmer Producer Organization advisory and structural support.'
            },
            {
                'title': 'Project Financing', 
                'icon': 'trending_up', 
                'desc': 'End-to-end debt syndication and project funding assistance.'
            },
            {
                'title': 'Merger & Acquisition', 
                'icon': 'handshake', 
                'desc': 'Strategic M&A advisory, valuations, and deal structuring.'
            },
            {
                'title': 'Sector Advisory', 
                'subtitle': 'Renewable, Healthcare, Textile, Real Estate', 
                'icon': 'domain', 
                'desc': 'Deep domain expertise across key industrial sectors.'
            },
            {
                'title': 'Listing, Compliance & Taxation', 
                'icon': 'verified_user', 
                'desc': 'SME listing, regulatory compliance, GST, and corporate taxation.'
            },
            {
                'title': 'CFO Shared Services', 
                'icon': 'analytics', 
                'desc': 'Niche fractional CFO advisory for tech-driven operational scaling.'
            },
        ]
        
        # Responsive 3-Column Card Grid
        with ui.grid().classes('grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 w-full mb-8'):
            for item in verticals:
                with ui.card().classes('p-6 w-full hover:shadow-xl transition-all duration-300 bg-white border-t-4 border-blue-600 flex flex-col justify-between'):
                    with ui.column().classes('gap-2 w-full'):
                        with ui.row().classes('items-center gap-3 mb-1'):
                            ui.icon(item['icon'], size='md').classes('text-blue-600')
                            ui.label(item['title']).classes('text-lg font-bold text-slate-800 leading-tight')
                        
                        if 'subtitle' in item:
                            ui.label(item['subtitle']).classes('text-xs font-semibold text-cyan-700 bg-cyan-50 px-2 py-1 rounded w-fit')
                            
                        ui.label(item['desc']).classes('text-slate-600 text-sm mt-1')
                    
                    with ui.row().classes('w-full justify-end mt-4'):
                        ui.button('Explore', icon='arrow_forward', on_click=lambda t=item['title']: ui.navigate.to('/services')) \
                            .props('flat dense color=primary')
            # --- OPTIONAL: DISPLAY DIAGRAM IMAGE DIRECTLY ---
        # Save your diagram image as 'verticals.png' in project folder to enable this box:
        with ui.card().classes('w-full p-6 my-6 flex-col items-center bg-slate-50 border border-slate-200'):
            ui.label('Vertical Architecture Diagram').classes('text-xl font-bold text-slate-800 mb-4')
            ui.element('img').props('src="/static/verticals.png"').classes('max-w-md w-full h-auto')
# --- PAGE 2: Advance EMI Calculator PAGE ---
@ui.page('/advance-emi-calculator')
def advanceemicalculator_page():
    with page_layout():
        ui.label('My Projects').classes('text-3xl font-extrabold text-slate-800 mt-4 mb-4')
        
        # Grid Row containing Project Cards & the Interactive EMI Tool
        with ui.row().classes('w-full gap-6 items-start'):
            
            # --- CARD 1: Automated Data Processing Engine ---
            with ui.card().classes('flex-1 p-6 shadow-md border border-slate-200 rounded-xl bg-white'):
                ui.label('Automated Data Processing Engine').classes('text-xl font-bold text-slate-800 mb-2')
                ui.label('Built backend workflows to parse and process custom client datasets efficiently.').classes('text-slate-600 text-sm')
            
            # --- CARD 2: Custom Analytics Dashboard ---
            with ui.card().classes('flex-1 p-6 shadow-md border border-slate-200 rounded-xl bg-white'):
                ui.label('Custom Analytics Dashboard').classes('text-xl font-bold text-slate-800 mb-2')
                ui.label('Developed interactive visualization dashboards using pure Python and modern frontend components.').classes('text-slate-600 text-sm')

            # --- CARD 3: Advance EMI Calculator Tool ---
            with ui.card().classes('flex-1 p-6 shadow-md border border-slate-200 rounded-xl bg-slate-900 text-white'):
                ui.label('Advance EMI Calculator').classes('text-xl font-bold text-emerald-400 mb-1')
                ui.label('Interactive tool to calculate loan amortizations with upfront advance EMI payments.').classes('text-slate-300 text-xs mb-4')

                # Calculation Engine Logic
                def calculate():
                    P = float(loan_amount.value or 0)
                    r = (float(interest_rate.value or 0) / 12) / 100
                    n = int((tenure_years.value or 0) * 12)
                    adv_count = int(advance_emis.value or 0)

                    if P > 0 and r > 0 and n > 0:
                        emi = (P * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
                        upfront = emi * adv_count
                        total_payable = (emi * (n - adv_count)) + upfront
                        total_interest = total_payable - P

                        lbl_emi.set_text(f'${emi:,.2f}')
                        lbl_upfront.set_text(f'${upfront:,.2f}')
                        lbl_interest.set_text(f'${total_interest:,.2f}')

                # Interactive Form Inputs
                loan_amount = ui.number('Loan Principal ($)', value=300000, step=5000, on_change=calculate).classes('w-full').props('dark color=emerald')
                interest_rate = ui.number('Annual Interest Rate (%)', value=7.5, step=0.1, on_change=calculate).classes('w-full').props('dark color=emerald')
                tenure_years = ui.number('Tenure (Years)', value=15, step=1, on_change=calculate).classes('w-full').props('dark color=emerald')
                advance_emis = ui.number('Upfront Advance EMIs', value=1, min=0, step=1, on_change=calculate).classes('w-full').props('dark color=emerald')

                # Live Results Summary
                ui.separator().classes('my-3 bg-slate-700')
                with ui.column().classes('w-full gap-2 text-sm'):
                    with ui.row().classes('justify-between w-full'):
                        ui.label('Monthly EMI:').classes('text-slate-400')
                        lbl_emi = ui.label('$0.00').classes('font-bold text-emerald-400')
                    
                    with ui.row().classes('justify-between w-full'):
                        ui.label('Upfront Paid:').classes('text-slate-400')
                        lbl_upfront = ui.label('$0.00').classes('font-bold text-slate-200')

                    with ui.row().classes('justify-between w-full'):
                        ui.label('Total Interest:').classes('text-slate-400')
                        lbl_interest = ui.label('$0.00').classes('font-bold text-rose-400')

                # Run baseline calculation when page renders
                calculate()
# --- PAGE 3: CONTACT FORM PAGE ---
@ui.page('/contact')
def contact_page():
    with page_layout():  # Preserves your shared Header and Footer
        
        # Centered container: Prevents full-screen stretching & creates margin above footer
        with ui.column().classes('w-full max-w-lg mx-auto items-center justify-center my-8 pb-16'):
            
            ui.label('Get In Touch').classes('text-3xl font-extrabold text-slate-800 mb-4 text-center')

            # Form Card
            with ui.card().classes('w-full p-6 flex flex-col gap-4 shadow-lg rounded-xl bg-white border border-slate-200'):
                
                name_input = ui.input(label='Your Name').classes('w-full')
                
                mobile_input = ui.input(
                    label='Mobile Number',
                    placeholder='10-digit mobile number',
                    validation={'Must be 10 digits': lambda v: bool(re.match(r'^\d{10}$', v or ''))}
                ).classes('w-full').props('maxlength=10 type=tel')
                
                email_input = ui.input(
                    label='Your Email',
                    validation={'Invalid email': lambda v: '@' in (v or '') and '.' in (v or '')}
                ).classes('w-full')
                
                message_input = ui.textarea(label='Your Message').classes('w-full').props('rows=3')

                def handle_submit():
                    name = (name_input.value or '').strip()
                    mobile = (mobile_input.value or '').strip()
                    email = (email_input.value or '').strip()
                    message = (message_input.value or '').strip()

                    if not name or not mobile or not email or not message:
                        ui.notify('Please fill out all required fields!', color='negative')
                        return

                    if not re.match(r'^\d{10}$', mobile):
                        ui.notify('Mobile number must be 10 numeric digits!', color='warning')
                        return

                    ui.notify(f'Thank you {name}, message sent!', color='positive')
                    name_input.value = ''
                    mobile_input.value = ''
                    email_input.value = ''
                    message_input.value = ''

                ui.button('Send Message', on_click=handle_submit).classes('w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2.5 rounded-lg mt-2')
        # --- NEW PAGE: About Us ---
# --- PAGE: ABOUT US ---
@ui.page('/about-us')
def about_us_page():
    with page_layout():
        
        # --- HERO BANNER ---
        with ui.card().classes('w-full p-8 bg-slate-800 text-white rounded-xl shadow-lg my-4'):
            ui.label('ABOUT THE FINCAP').classes('text-sm font-bold tracking-widest text-blue-400 uppercase mb-1')
            ui.label('Empowering Growth Through Financial Excellence').classes('text-3xl font-extrabold text-white mb-2')
            ui.label(
                'We understand "finance" as the lifeblood of any business organization. '
                'Our expertise helps enterprises navigate complex economic landscapes with resilience and agility.'
            ).classes('text-slate-300 text-base leading-relaxed')

        # --- 4 CORE PILLARS GRID ---
        ui.label('Our Core Pillars').classes('text-2xl font-bold text-slate-800 mt-6 mb-4')
        
        pillars = [
            {
                'title': 'Our Objective',
                'icon': 'ads_click',
                'color': 'border-blue-600',
                'desc': 'At The FinCap we understand "finance" as the lifeblood of business organization, every business and activity as development projects require adequate finance to meet their requirements in this economic world. Whether the business concerns are big or small, without proper financing solutions, it is very difficult to start or run the business activities efficiently.'
            },
            {
                'title': 'Our Mission',
                'icon': 'health_and_safety',
                'color': 'border-teal-500',
                'desc': 'We believe physical health is of utmost importance to everyone, be it an individual or an organization. We do a proper financial and operational analysis so prophylactic measures can be instituted in recessionary economic environment to excel when there is an opportunity or tide turns.'
            },
            {
                'title': 'Our Strength',
                'icon': 'bolt',
                'color': 'border-indigo-600',
                'desc': 'The FinCap financial expertise and quick turnaround time helps you to setup and kick start your business activities without any delay. We provide existing businesses significant cost reduction measures and centre of expertise which helps you leap forward over your competitors.'
            },
            {
                'title': 'Our Goal',
                'icon': 'emoji_events',
                'color': 'border-amber-500',
                'desc': 'FinCap prepare you for the short and long term prospective with our expertise in FPO, Banking, Private Equity, Project Finance and M&A Services.'
            },
        ]
        
        with ui.grid().classes('grid-cols-1 md:grid-cols-2 gap-6 w-full mb-8'):
            for p in pillars:
                with ui.card().classes(f'p-6 w-full bg-white shadow-md rounded-lg border-t-4 {p["color"]} hover:shadow-lg transition-all'):
                    with ui.row().classes('items-center gap-3 mb-2'):
                        ui.icon(p['icon'], size='md').classes('text-slate-700')
                        ui.label(p['title']).classes('text-xl font-bold text-slate-800')
                    ui.label(p['desc']).classes('text-slate-600 text-sm leading-relaxed')

        # --- FINCAP VALUE PYRAMID ---
        with ui.card().classes('w-full p-8 bg-slate-50 border border-slate-200 rounded-xl my-6'):
            ui.label('The FinCap Value Pyramid').classes('text-2xl font-bold text-slate-800 mb-1')
            ui.label('Our foundational hierarchy for corporate growth, sustainability, and value creation:').classes('text-slate-600 mb-6')
            
            pyramid_levels = [
                {'level': '6', 'title': 'Profit & Wealth Maximization', 'bg': 'bg-red-600', 'width': 'w-1/2'},
                {'level': '5', 'title': 'Longevity & Sustainability', 'bg': 'bg-lime-600', 'width': 'w-2/3'},
                {'level': '4', 'title': 'Growth & Brand Building', 'bg': 'bg-amber-500', 'width': 'w-3/4'},
                {'level': '3', 'title': 'Corporate Governance', 'bg': 'bg-cyan-600', 'width': 'w-4/5'},
                {'level': '2', 'title': 'Integrity & Ethics', 'bg': 'bg-sky-600', 'width': 'w-11/12'},
                {'level': '1', 'title': 'Professional & Technical Skills', 'bg': 'bg-slate-800', 'width': 'w-full'},
            ]
            
            with ui.column().classes('w-full max-w-2xl mx-auto gap-2 items-center'):
                for item in pyramid_levels:
                    with ui.row().classes(f'{item["width"]} {item["bg"]} text-white p-3 rounded shadow-md items-center justify-between transition-all duration-300 hover:scale-[1.02]'):
                        with ui.row().classes('items-center gap-3'):
                            ui.label(item['level']).classes('font-black text-lg bg-white/20 px-2.5 py-0.5 rounded')
                            ui.label(item['title']).classes('font-bold text-sm sm:text-base')
                        ui.icon('check_circle', size='xs').classes('opacity-80')

        # --- LEADERSHIP & TEAM SECTION ---
        ui.label('FinCap Team').classes('text-2xl font-bold text-slate-800 mt-8 mb-2')
        ui.label('At the FinCap we are team of professionals who came together to deliver quality and value added services to corporates in this fast changing world.').classes('text-slate-600 mb-6')
        
        # Profile Card
        with ui.card().classes('w-full p-8 bg-white border border-slate-200 shadow-md rounded-xl'):
            with ui.row().classes('gap-8 items-start flex-col md:flex-row w-full'):
                
                # Photo & Stats Badge
                with ui.column().classes('items-center gap-3 shrink-0 mx-auto md:mx-0'):
                    ui.element('img').props('src="/static/md.png"') \
                        .classes('w-44 h-44 rounded-full object-cover border-4 border-slate-100 shadow-lg')
                    
                    ui.label('Praveen Chandalia').classes('text-xl font-bold text-slate-900 text-center')
                    ui.label('Managing Director & Financial Expert').classes('text-xs font-bold text-blue-700 bg-blue-50 px-3 py-1 rounded-full text-center')

                    with ui.column().classes('w-full bg-slate-50 p-3 rounded-lg border border-slate-100 mt-2 gap-1 text-center'):
                        ui.label('Over Two Decades of Global Experience').classes('text-xs font-bold text-slate-700')
                        ui.label('USD 1.0B+ Capital Raised').classes('text-xs font-bold text-emerald-700')
                        ui.label('Chartered Accountant (ICAI)').classes('text-xs font-semibold text-slate-500')

                # Profile Bio
                with ui.column().classes('flex-1 gap-4'):
                    ui.label(
                        'Praveen is a science graduate and qualified chartered accountant from Institute of '
                        'Chartered Accountants of India. He is a financial expert with over two decades of global experience across the Middle East, Europe, and India. Throughout his career, he has gained deep insight into a broad spectrum of financial products while delivering innovative financial solutions. He brings extensive domain expertise across key sectors, including the polyester and textile value chain, industrial solar, and real estate.'
                    ).classes('text-slate-700 leading-relaxed text-base')
                    
                    ui.label(
                        'He worked on various greenfield & expansion projects, built complex financial models & feasibilities. '
                        'He was instrumental in raising more than USD 1.0 billions of fund through commercial lending '
                        'syndication and private equity investments.'
                    ).classes('text-slate-700 leading-relaxed text-base')

                    # Capability Tags
                    with ui.row().classes('gap-2 flex-wrap pt-2'):
                        for tag in ['Project Financing', 'Private Equity', 'Financial Modeling', 'M&A Advisory', 'Commercial Syndication']:
                            ui.label(tag).classes('text-xs font-semibold text-slate-600 bg-slate-100 px-3 py-1.5 rounded-md')
        # --- NEW PAGE: SERVICES ---
# --- PAGE: OUR SERVICES ---
@ui.page('/services')
def services_page():
    with page_layout():
        
        # --- HERO BANNER ---
        with ui.card().classes('w-full p-8 bg-slate-800 text-white rounded-xl shadow-lg my-4'):
            ui.label('OUR SERVICES').classes('text-sm font-bold tracking-widest text-blue-400 uppercase mb-1')
            ui.label('Comprehensive Financial & Strategic Solutions').classes('text-3xl font-extrabold text-white mb-2')
            ui.label(
                'At The FinCap, we deliver tailored financial structures, transaction advisory, and compliance frameworks '
                'to drive capital efficiency and long-term business sustainability.'
            ).classes('text-slate-300 text-base leading-relaxed')

        # --- SERVICE 1: CORPORATE & TRADE FINANCE ---
        with ui.card().classes('w-full p-8 bg-white border border-slate-200 shadow-md rounded-xl my-4'):
            ui.label('CORPORATE & TRADE FINANCE').classes('text-2xl font-bold text-slate-800 mb-2')
            ui.label(
                'At The FinCap we help our clients to secure their financial needs: quick turnaround time, '
                'reduction in finance cost and increase the working capital cycles through smart & innovative financing solutions.'
            ).classes('text-slate-600 mb-6 leading-relaxed')

            with ui.grid().classes('grid-cols-1 md:grid-cols-2 gap-6 w-full'):
                
                # Long term Financing
                with ui.card().classes('p-6 bg-slate-50 border-l-4 border-blue-600 rounded-lg'):
                    ui.label('Long Term Financing Solutions').classes('text-lg font-bold text-slate-800 mb-3')
                    with ui.column().classes('gap-2 text-slate-600 text-sm'):
                        for item in [
                            'Project Finance, ECA', 
                            'Asset-based Loans', 
                            'Equipment Finance', 
                            'Real Estate Finance', 
                            'Mezzanine Finance (subordinated debt finance)', 
                            'Private Equity'
                        ]:
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('check_circle', size='xs').classes('text-blue-600')
                                ui.label(item)

                # Trade Finance Solutions
                with ui.card().classes('p-6 bg-slate-50 border-l-4 border-cyan-600 rounded-lg'):
                    ui.label('Trade Finance Solutions').classes('text-lg font-bold text-slate-800 mb-3')
                    
                    ui.label('Fund Based Facilities').classes('text-xs font-bold text-slate-500 uppercase tracking-wider mb-1')
                    with ui.column().classes('gap-1 text-slate-600 text-sm mb-4 pl-2'):
                        for item in [
                            'Suppliers Financing, Buyers Credit, Dealer Financing',
                            'Trust Receipts, Overdraft',
                            'Invoice Factoring',
                            'Packing Credit Finance (PCFC, EPC)',
                            'International Trade Finance, ECB'
                        ]:
                            ui.label(f'• {item}')
                    
                    ui.label('Non Fund Based Facilities').classes('text-xs font-bold text-slate-500 uppercase tracking-wider mb-1')
                    with ui.column().classes('gap-1 text-slate-600 text-sm pl-2'):
                        for item in [
                            'Letter of Credit, SBLC, Avalization BoE',
                            'Bank Guarantee (BB, APG, PG & FG)'
                        ]:
                            ui.label(f'• {item}')

        # --- SERVICE 2: TAXATION & COMPLIANCE ---
        with ui.card().classes('w-full p-8 bg-white border border-slate-200 shadow-md rounded-xl my-4'):
            ui.label('TAXATION & COMPLIANCE').classes('text-2xl font-bold text-slate-800 mb-2')
            ui.label('Corporate Responsibility & Strategic Structuring').classes('text-slate-600 mb-6')

            tax_items = [
                ('GST', 'Tax registration, reporting & filing, payments & refund'),
                ('Corporate Taxation Planning', 'Strategic structuring of business operations in order to minimize tax liability.'),
                ('Property & Credit Risk Insurance', 'Industrial All Risk Policy (IAR), & Credit Risk Insurance, etc, to cover all major risk in business.'),
                ('Credit Rating', "We help to evaluate & determine borrower's creditworthiness & raise funds"),
                ('Listing & SEBI Compliance', 'Assisting in SME & mainboard listing, to comply with the provisions of the Companies Act, 2013 and SEBI Regulations, 2015'),
                ('BRSR & ESG', 'BRSR & ESG reporting is the disclosure of environmental, social and corporate governance data.'),
                ('EPR', "Extended Producer Responsibility (EPR) as an environmental policy approach in which a producer's responsibility for proper disposal of plastic waste."),
                ('Anti Dumping Duty', 'Antidumping (AD) Law – remedies unfairly priced imports that injure or threaten to injure domestic industry.')
            ]

            with ui.grid().classes('grid-cols-1 md:grid-cols-2 gap-4 w-full'):
                for title, desc in tax_items:
                    with ui.card().classes('p-4 bg-slate-50 border-t-2 border-slate-300 rounded-lg hover:border-blue-600 transition-all'):
                        ui.label(title).classes('font-bold text-slate-800 text-base mb-1')
                        ui.label(desc).classes('text-slate-600 text-sm leading-relaxed')

        # --- SERVICE 3: FINANCIAL PROCESS OUTSOURCING (FPO) ---
        with ui.card().classes('w-full p-8 bg-white border border-slate-200 shadow-md rounded-xl my-4'):
            ui.label('FINANCIAL PROCESS OUTSOURCING "FPO"').classes('text-2xl font-bold text-slate-800 mb-2')
            ui.label(
                'Many companies either already outsourced or in process of outsourcing their back-office functions of major business processes. '
                'The underlying principle for outsourcing is not just as a cost-cutting measure, but also for strategic advantages.'
            ).classes('text-slate-600 mb-6 leading-relaxed')

            with ui.grid().classes('grid-cols-1 md:grid-cols-2 gap-6 w-full'):
                # Key Principles
                with ui.column().classes('gap-3 bg-slate-50 p-6 rounded-xl border border-slate-200'):
                    ui.label('Strategic Advantages').classes('text-lg font-bold text-slate-800 mb-2')
                    for idx, principle in enumerate([
                        'Centralizing non-core functions to achieve economies of scale',
                        'Harmonizing processes to create standardized procedures',
                        'Access to global talent & centre of expertise. Easy & effective human resource management in core areas of business.',
                        'Significant reduction in internal ongoing operating costs.',
                        'Leverage on latest technology investments & updates.'
                    ], 1):
                        with ui.row().classes('items-start gap-3'):
                            ui.label(f'{idx}.').classes('font-bold text-blue-600')
                            ui.label(principle).classes('text-slate-700 text-sm flex-1')

                # Scope of Services
                with ui.column().classes('gap-4'):
                    with ui.card().classes('p-5 bg-slate-50 border-l-4 border-blue-600 w-full'):
                        ui.label('Transactions Outsourcing').classes('font-bold text-slate-800 mb-2')
                        ui.label('• Company Formation  • Invoicing  • Purchase Order  • Banking Transactions  • Process Standardization').classes('text-xs text-slate-600 leading-relaxed')

                    with ui.card().classes('p-5 bg-slate-50 border-l-4 border-cyan-600 w-full'):
                        ui.label('Accounting & Book Keeping').classes('font-bold text-slate-800 mb-2')
                        ui.label('• Accounts Payables  • Trade Receivables  • Financial Statements  • Payroll Processing  • Process Manuals').classes('text-xs text-slate-600 leading-relaxed')

                    with ui.card().classes('p-5 bg-slate-50 border-l-4 border-indigo-600 w-full'):
                        ui.label('Task Outsourcing').classes('font-bold text-slate-800 mb-2')
                        ui.label('• Setting up SOPs  • Transaction Outsourcing  • Accounting & Reporting  • FPnA  • Strategic Advisory').classes('text-xs text-slate-600 leading-relaxed')

        # --- SERVICE 4: CFO SHARED SERVICES ---
        with ui.card().classes('w-full p-8 bg-white border border-slate-200 shadow-md rounded-xl my-4'):
            ui.label('CFO SHARED SERVICES').classes('text-2xl font-bold text-slate-800 mb-2')
            ui.label('Knowledge Process Outsourcing & Virtual CFO Governance').classes('text-slate-600 mb-6')

            with ui.grid().classes('grid-cols-1 md:grid-cols-2 gap-6 w-full'):
                with ui.column().classes('gap-3 bg-slate-50 p-6 rounded-xl border border-slate-200'):
                    ui.label('Execution Roadmap').classes('text-lg font-bold text-slate-800 mb-2')
                    for step in [
                        'Identify activities to outsource',
                        'Do cost benefit analysis',
                        'Shared infrastructure & capabilities',
                        'Provide expert advice and suggest improved measures',
                        'Draft, negotiate & signed service contract',
                        'And deliver performance.'
                    ]:
                        with ui.row().classes('items-center gap-3'):
                            ui.icon('arrow_right_alt', size='sm').classes('text-blue-600')
                            ui.label(step).classes('text-slate-700 text-sm')

                with ui.column().classes('gap-3 bg-blue-50 p-6 rounded-xl border border-blue-100'):
                    ui.label('CFO Dashboard Modules').classes('text-lg font-bold text-blue-900 mb-2')
                    modules = [
                        ('Financial Reporting', 'Financial Statements, Consolidations'),
                        ('Risk and Compliance', 'Tax payment & return filing, Risk Management'),
                        ('Financial Management', 'FP&A, Budgeting'),
                        ('Strategic Planning', 'Expansion & Growth / Merger & Acquisition')
                    ]
                    for title, desc in modules:
                        with ui.column().classes('bg-white p-3 rounded-lg shadow-sm border border-blue-100 w-full'):
                            ui.label(title).classes('font-bold text-slate-800 text-sm')
                            ui.label(desc).classes('text-xs text-slate-500')

        # --- SERVICE 5: PROJECT FINANCE ---
        with ui.card().classes('w-full p-8 bg-white border border-slate-200 shadow-md rounded-xl my-4'):
            ui.label('PROJECT FINANCE').classes('text-2xl font-bold text-slate-800 mb-2')
            ui.label(
                'We at The FinCap provide project financing services that includes preparation of project feasibility report, '
                'financial modelling, and structure project funding solutions. We identify risk areas and address ways to mitigate them.'
            ).classes('text-slate-600 mb-6 leading-relaxed')

            with ui.grid().classes('grid-cols-1 md:grid-cols-2 gap-6 w-full'):
                with ui.column().classes('gap-3 bg-slate-50 p-6 rounded-xl border border-slate-200'):
                    ui.label('Risk Mitigation Areas').classes('text-lg font-bold text-slate-800 mb-2')
                    for risk in [
                        'Country & Political Risk',
                        'Industry & Sectors Analysis',
                        'Market & Competition',
                        'Project Execution',
                        'Supply Side',
                        'Project Funding',
                        'Currency & Interest'
                    ]:
                        with ui.row().classes('items-center gap-3'):
                            ui.icon('shield', size='xs').classes('text-blue-600')
                            ui.label(risk).classes('text-slate-700 text-sm font-medium')

                with ui.column().classes('gap-3 bg-slate-50 p-6 rounded-xl border border-slate-200'):
                    ui.label('Project Lifecycle Model').classes('text-lg font-bold text-slate-800 mb-2')
                    lifecycle = [
                        'Project Company & Objective',
                        'Project Ownership & Management Team',
                        'Business Strategy & Market Opportunity',
                        'Project Investments & Operating Assumptions',
                        'Project Financing & SWOT Analysis',
                        'Project Return & Sensitivity Analysis'
                    ]
                    for idx, step in enumerate(lifecycle, 1):
                        with ui.row().classes('items-center gap-3'):
                            ui.label(f'0{idx}').classes('text-xs font-bold bg-blue-100 text-blue-800 px-2 py-0.5 rounded')
                            ui.label(step).classes('text-slate-700 text-sm')

        # --- SERVICE 6: MERGER & ACQUISITIONS ---
        with ui.card().classes('w-full p-8 bg-white border border-slate-200 shadow-md rounded-xl my-4'):
            ui.label('MERGER & ACQUISITIONS').classes('text-2xl font-bold text-slate-800 mb-2')
            
            ui.label(
                'In the Global market, companies are facing tough competition from its peers, as the rapid change in technology & '
                'improved logistics has brought competition to centre stage. Now organizations focus more on expanding globally and '
                'managing operations from centralized locations. M&A activities provide opportunity to create synergy by economy of scale and increasing market share.'
            ).classes('text-slate-600 mb-6 leading-relaxed')

            ui.label('M&A Lifecycle Framework').classes('text-base font-bold text-slate-800 mb-3')
            
            ma_steps = [
                'M&A Strategy', 'Acquisition Target', 'Target Valuation', 
                'Synergy Analysis', 'Due Diligence', 'Integration Planning', 'Integration Execution'
            ]
            
            with ui.row().classes('gap-3 flex-wrap w-full'):
                for step in ma_steps:
                    with ui.card().classes('p-4 bg-slate-50 border-b-4 border-blue-600 flex-1 min-w-[150px] items-center text-center shadow-sm'):
                        ui.icon('hub', size='sm').classes('text-blue-600 mb-1')
                        ui.label(step).classes('font-bold text-xs text-slate-800')
# --- NEW PAGE: INDUSTRIES ---
@ui.page('/industries')
def industries_page():
    with page_layout():

        # ==========================================
        # HERO BANNER
        # ==========================================
        with ui.card().classes('w-full p-8 bg-slate-900 text-white rounded-xl shadow-lg'):
            ui.label('INDUSTRIES WE SERVE').classes('text-xs font-bold tracking-widest text-sky-400 uppercase mb-1')
            ui.label('Sector-Specific Solutions & Strategic Growth').classes('text-3xl font-black text-white mb-2')
            ui.label(
                'Comprehensive breakdown of our operations across Real Estate, Renewable Energy, '
                'Polyester & Textile Value Chain, and Healthcare infrastructure.'
            ).classes('text-slate-300 text-sm leading-relaxed')

        # ==========================================
        # 1. REAL ESTATE PROJECTS
        # ==========================================
        with ui.card().classes('w-full p-6 md:p-8 bg-white border border-slate-200 shadow-md rounded-xl'):
            ui.label('REAL ESTATE PROJECTS').classes('text-3xl font-black text-slate-900 mb-6 tracking-wide')

            with ui.grid().classes('grid-cols-1 lg:grid-cols-12 gap-8 w-full'):
                
                # Left Column: Development Models & Feasibilities
                with ui.column().classes('lg:col-span-5 gap-6'):
                    
                    # Project Development Model
                    with ui.card().classes('w-full p-5 bg-sky-50/50 border border-sky-200 rounded-lg'):
                        ui.label('Project development model').classes('text-lg font-bold text-slate-800 mb-3')
                        dev_models = [
                            'Residential & Services Apartments',
                            'Commercial & Office Space',
                            'Shopping Mall',
                            'Hotel & Leisure Activities',
                            'Community Development',
                            'Warehousing'
                        ]
                        with ui.column().classes('gap-2 text-slate-700 text-sm font-medium'):
                            for item in dev_models:
                                with ui.row().classes('items-center gap-2'):
                                    ui.icon('square', size='8px').classes('text-sky-600')
                                    ui.label(item)

                    # Project Feasibilities & Financing
                    with ui.card().classes('w-full p-5 bg-sky-50/50 border border-sky-200 rounded-lg'):
                        ui.label('Project Feasibilities & Financing').classes('text-lg font-bold text-slate-800 mb-3')
                        feasibilities = [
                            'Financial Model',
                            'Planning & Development Construction',
                            'Project Costs',
                            'Funding (Debt, Equity, Pre Sale Contributions)',
                            'Operations',
                            'Financial Projections (profitability, cash flow and returns)'
                        ]
                        with ui.column().classes('gap-2 text-slate-700 text-sm font-medium'):
                            for item in feasibilities:
                                with ui.row().classes('items-center gap-2'):
                                    ui.icon('square', size='8px').classes('text-sky-600')
                                    ui.label(item)

                # Right Column: Diamond Ecosystem Center Diagram
                with ui.column().classes('lg:col-span-7 flex flex-col items-center justify-center bg-slate-50 p-6 rounded-xl border border-slate-200'):
                    ui.label('Ecosystem Stakeholder Governance').classes('text-xs font-bold text-slate-500 uppercase tracking-wider mb-4')
                    
                    # Center Core
                    with ui.card().classes('p-4 bg-sky-800 text-white rounded-lg shadow-md text-center w-64 mb-6'):
                        ui.label('PROJECT DEVELOPMENT COMPANY').classes('font-black text-sm tracking-wide')

                    # Stakeholder Node Mapping
                    with ui.grid().classes('grid-cols-1 sm:grid-cols-2 gap-4 w-full'):
                        nodes = [
                            ('PROJECT OWNERS & LENDERS', 'Shareholders Agreement / Facility & Security Agreements'),
                            ('DESIGN & ENGG. COMPANY', 'Facility And Security Agreements'),
                            ('GOVERNMENT & OWNERS', 'Facility And Security Agreements'),
                            ('HOTEL CONSTRUCTION CONTRACTOR', 'Facility And Security Agreements'),
                            ('APARTMENT CONSTRUCTION CONTRACTOR', 'Facility And Security Agreements'),
                            ('APARTMENT MARKETING COMPANY', 'Apartment Marketing Agreements'),
                            ('HOTEL MANAGEMENT COMPANY', 'Hotel Management Contract')
                        ]
                        for title, agreement in nodes:
                            with ui.card().classes('p-3 bg-white border-l-4 border-sky-600 rounded shadow-sm'):
                                ui.label(title).classes('font-bold text-xs text-slate-800')
                                ui.label(agreement).classes('text-[11px] text-slate-500 mt-1')

        # ==========================================
        # 2. RENEWABLE ENERGY
        # ==========================================
        with ui.card().classes('w-full p-6 md:p-8 bg-white border border-slate-200 shadow-md rounded-xl'):
            ui.label('RENEWABLE ENERGY – SOLAR & WIND POWER, CARBON CREDIT').classes('text-2xl md:text-3xl font-black text-slate-900 mb-6 tracking-wide')

            with ui.grid().classes('grid-cols-1 lg:grid-cols-12 gap-6 w-full mb-6'):
                
                # PPA Box
                with ui.column().classes('lg:col-span-4 bg-sky-100/60 p-6 rounded-xl border border-sky-200 gap-3'):
                    ui.label('PPA Zero Investments').classes('text-xl font-bold text-slate-800 text-center w-full mb-2')
                    ppa_points = [
                        'No Power Generation Risk',
                        'Power Cost Cheaper than Grid (30%-40%)',
                        'No Operation & Maintenance costs',
                        'Convert your ideal rooftop into a money saver'
                    ]
                    for pt in ppa_points:
                        with ui.card().classes('w-full p-3 bg-sky-500 text-white rounded-md font-semibold text-xs text-center shadow-sm'):
                            ui.label(pt)

                # CAPEX Model Box
                with ui.column().classes('lg:col-span-4 bg-sky-100/60 p-6 rounded-xl border border-sky-200 gap-3'):
                    ui.label('CAPEX MODEL\n(Owned Solar Plant)').classes('text-xl font-bold text-slate-800 text-center w-full mb-2 whitespace-pre-line')
                    capex_points = [
                        'Company ownership of Solar Assets',
                        'One time capital investment',
                        'No running costs except regular maintenance',
                        'Accelerated depreciation claim in Income Tax'
                    ]
                    for pt in capex_points:
                        with ui.card().classes('w-full p-3 bg-sky-500 text-white rounded-md font-semibold text-xs text-center shadow-sm'):
                            ui.label(pt)

                # Savings & Lifecycle Box
                with ui.column().classes('lg:col-span-4 bg-sky-50 border border-slate-200 p-6 rounded-xl items-center justify-between text-center gap-4'):
                    ui.label('Lifecycle Optimization').classes('text-xs font-bold text-slate-400 uppercase tracking-widest')
                    
                    with ui.grid().classes('grid-cols-2 gap-2 w-full'):
                        with ui.card().classes('p-3 bg-white border border-slate-200 rounded text-center'):
                            ui.icon('account_balance', size='sm').classes('text-sky-600 mb-1')
                            ui.label('Project Finance').classes('text-xs font-bold text-slate-700')
                        with ui.card().classes('p-3 bg-white border border-slate-200 rounded text-center'):
                            ui.icon('solar_power', size='sm').classes('text-sky-600 mb-1')
                            ui.label('Solar Plant Installation').classes('text-xs font-bold text-slate-700')
                        with ui.card().classes('p-3 bg-white border border-slate-200 rounded text-center'):
                            ui.icon('build', size='sm').classes('text-sky-600 mb-1')
                            ui.label('Operation & Maintenance').classes('text-xs font-bold text-slate-700')
                        with ui.card().classes('p-3 bg-white border border-slate-200 rounded text-center'):
                            ui.icon('trending_up', size='sm').classes('text-sky-600 mb-1')
                            ui.label('Saving on Energy Bills').classes('text-xs font-bold text-slate-700')

                    ui.label('Adding green energy to your business....').classes('text-emerald-600 font-extrabold text-base italic mt-2')

            # Carbon Credit CC Box
            with ui.card().classes('w-full p-5 bg-sky-50 border border-sky-300 rounded-xl'):
                ui.label('Carbon Credit “CC”').classes('text-base font-bold text-sky-900 mb-2')
                ui.label(
                    '• We help you take CC that pull Greenhouse Gases (GHGs) out of the atmosphere or keep emissions from being released in environment, '
                    'through renewable energy, methane abatement, energy efficiency, reforestation and fuel switching (i.e. to carbon-neutral fuels and carbon-negative fuels)'
                ).classes('text-slate-700 text-xs md:text-sm leading-relaxed')

        # ==========================================
        # 3. POLYESTER & TEXTILE VALUE CHAIN
        # ==========================================
        with ui.card().classes('w-full p-6 md:p-8 bg-white border border-slate-200 shadow-md rounded-xl'):
            ui.label('POLYESTER & TEXTILE VALUE CHAIN').classes('text-3xl font-black text-slate-900 mb-6 tracking-wide')

            with ui.grid().classes('grid-cols-1 lg:grid-cols-12 gap-8 w-full'):
                
                # Objectives Flow (Left)
                with ui.column().classes('lg:col-span-4 gap-4 justify-between'):
                    objs = [
                        'Widen your product range &\nincrease market share',
                        'Create Value',
                        'Provide Customer Satisfaction'
                    ]
                    for obj in objs:
                        with ui.card().classes('w-full p-5 bg-sky-600 text-white rounded-lg shadow text-center font-bold text-sm whitespace-pre-line'):
                            ui.label(obj)

                # Gear Branding Center Flow
                with ui.column().classes('lg:col-span-4 bg-slate-50 p-6 rounded-xl border border-slate-200 items-center justify-center text-center gap-4'):
                    ui.label('Manufacturing & Branding Hub').classes('text-xs font-bold text-slate-400 uppercase tracking-wider')
                    
                    with ui.card().classes('w-full p-4 bg-slate-800 text-white rounded-lg shadow'):
                        ui.label('Garment Manufacturer').classes('font-bold text-sm')
                    
                    ui.icon('autorenew', size='md').classes('text-sky-600 my-1')

                    with ui.card().classes('w-full p-4 bg-sky-800 text-white rounded-lg shadow'):
                        ui.label('Create your own Brand & Logo').classes('font-bold text-sm')

                    ui.icon('arrow_downward', size='sm').classes('text-slate-400 my-1')

                    with ui.card().classes('w-full p-4 bg-slate-700 text-white rounded-lg shadow'):
                        ui.label('Uniforms').classes('font-bold text-sm')

                # Material Flow Blocks (Right)
                with ui.column().classes('lg:col-span-4 gap-3'):
                    materials = [
                        'PET Resin & PET Scrap',
                        'Recycle Polyester Fiber & Virgin Fiber',
                        'Spun & OE Yarn, Knitted Yarn, PV blended &',
                        '100% Poly, PV, Denim Fabric & Knitted Fabric'
                    ]
                    for mat in materials:
                        with ui.card().classes('w-full p-4 bg-sky-600 text-white rounded-lg shadow font-semibold text-xs flex items-center justify-center text-center'):
                            ui.label(mat)

        # ==========================================
        # 4. SMWD HEALTHCARE
        # ==========================================
        with ui.card().classes('w-full p-6 md:p-8 bg-white border border-slate-200 shadow-md rounded-xl'):
            ui.label('SMWD HEALTHCARE').classes('text-3xl font-black text-slate-900 mb-6 tracking-wide')

            with ui.grid().classes('grid-cols-1 lg:grid-cols-12 gap-6 w-full'):
                
                # Summary Bullet Column
                with ui.column().classes('lg:col-span-4 bg-slate-50 p-6 rounded-xl border border-slate-200 gap-4 justify-between'):
                    summary_bullets = [
                        "Can grow your business with the established SMWD Company's Global Sales Network & Infrastructure.",
                        "Take over major functions and associated costs related to Sales, Marketing, Warehousing and Distribution Activities.",
                        "Companies can focus more on research, product development, and production activities.",
                        "Established global sales force will be deployed for the company with no extra direct costs."
                    ]
                    for bullet in summary_bullets:
                        with ui.row().classes('items-start gap-2'):
                            ui.icon('check_circle', size='xs').classes('text-sky-600 mt-1')
                            ui.label(bullet).classes('text-xs md:text-sm text-slate-700 font-medium leading-relaxed')

                # Operational Pillars Grid
                with ui.column().classes('lg:col-span-8'):
                    with ui.grid().classes('grid-cols-1 sm:grid-cols-2 gap-4 w-full'):
                        
                        # Sales
                        with ui.card().classes('p-5 bg-sky-50/60 border border-sky-200 rounded-lg flex flex-col justify-start'):
                            ui.label('Sales:').classes('text-base font-bold text-slate-900 mb-2')
                            ui.label('• SMWD Company at its own cost, shall actively market and promote the sale and use of Products.').classes('text-xs text-slate-600 leading-relaxed')

                        # Marketing
                        with ui.card().classes('p-5 bg-sky-50/60 border border-sky-200 rounded-lg flex flex-col justify-start'):
                            ui.label('Marketing:').classes('text-base font-bold text-slate-900 mb-2')
                            ui.label('• SMWD Company shall utilize such advertising, marketing, promotional materials, and literature relative to the sale and use of the Products as may be necessary or appropriate.').classes('text-xs text-slate-600 leading-relaxed mb-2')
                            ui.label('• SMWD Company shall participate in trade shows and exhibitions in the Territory where such participation will promote the Products').classes('text-xs text-slate-600 leading-relaxed')

                        # Warehousing
                        with ui.card().classes('p-5 bg-sky-50/60 border border-sky-200 rounded-lg flex flex-col justify-start'):
                            ui.label('Warehousing:').classes('text-base font-bold text-slate-900 mb-2')
                            ui.label('• SMWD Company shall establish and maintain such places of business and shall maintain and properly train a sales force and other personnel, at its own cost and expense, as shall be necessary to provide good customer service and support, marketing coverage, and promotion for the Products.').classes('text-xs text-slate-600 leading-relaxed')

                        # Distribution
                        with ui.card().classes('p-5 bg-sky-50/60 border border-sky-200 rounded-lg flex flex-col justify-start'):
                            ui.label('Distribution:').classes('text-base font-bold text-slate-900 mb-2')
                            ui.label('• SMWD Company will established supply chain & distribution in local and international market for supply of goods in a very efficient way to optimize the resources thus reduce the overall costs').classes('text-xs text-slate-600 leading-relaxed')
# --- NEW PAGE: TEXSOURCE ---
@ui.page('/texsource')
def texsource_page():
    with page_layout():

        # ==========================================
        # HEADER BANNER & BRANDING
        # ==========================================
        with ui.card().classes('w-full p-6 md:p-8 bg-gradient-to-r from-sky-900 via-blue-900 to-cyan-900 text-white rounded-xl shadow-lg'):
            with ui.row().classes('w-full items-center justify-between gap-6'):
                with ui.column().classes('gap-2 flex-1'):
                    ui.label('TEXSOURCE CORPORATION').classes('text-2xl md:text-4xl font-black tracking-wider text-white')
                    ui.label('"Powering Circular Textiles"').classes('text-lg md:text-xl font-serif italic text-cyan-300')
                    ui.label('Strategic RM Sourcing & Distribution Network  ·  Polymer Value Chain  ·  Financial & Industrial Solar Advisory').classes('text-xs md:text-sm text-sky-100 font-medium mt-1')
                
                # TexSourceLogo Display
                ui.image('Texsourcelogo.jpeg').classes('w-28 md:w-36 h-auto rounded-lg shadow-md border-2 border-cyan-400/30 bg-white p-1')

        # ==========================================
        # VALUE PROPOSITION BANNER
        # ==========================================
        with ui.card().classes('w-full p-6 bg-sky-50 border border-sky-200 text-center rounded-xl shadow-sm'):
            ui.label('Premier supply chain partner for the global polymer, recycling & textile industries').classes('text-lg md:text-xl font-extrabold text-sky-950 mb-1')
            ui.label('Bridging global raw material networks with domestic production hubs — structural savings, quality assurance & working capital optimization').classes('text-xs md:text-sm text-slate-600 font-medium')

        # ==========================================
        # WHO WE SERVE
        # ==========================================
        with ui.card().classes('w-full p-6 bg-white border border-slate-200 shadow-md rounded-xl'):
            ui.label('WHO WE SERVE').classes('text-xs font-bold tracking-widest text-sky-600 uppercase mb-4 text-center w-full')
            
            sectors = [
                ('Spinning Mills', 'autorenew'),
                ('Fiber Recyclers', 'recycling'),
                ('Industrial Processors', 'precision_manufacturing'),
                ('Weaving Units', 'grid_view'),
                ('Non-Woven Manufacturers', 'layers')
            ]
            
            with ui.grid().classes('grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-4 w-full'):
                for name, icon in sectors:
                    with ui.card().classes('p-4 bg-slate-50 border border-slate-200 rounded-lg text-center items-center hover:bg-sky-50 transition-all'):
                        ui.icon(icon, size='md').classes('text-sky-700 mb-2')
                        ui.label(name).classes('font-bold text-xs md:text-sm text-slate-800')

        # ==========================================
        # BRAND CONCEPT & VALUE PROPOSITION
        # ==========================================
        with ui.grid().classes('grid-cols-1 md:grid-cols-2 gap-6 w-full'):
            
            # Brand Concept Block
            with ui.card().classes('p-6 bg-white border border-slate-200 shadow-md rounded-xl text-center'):
                ui.label('BRAND CONCEPT').classes('text-base font-extrabold text-sky-900 tracking-wider mb-6 w-full')
                with ui.row().classes('items-center justify-center gap-2 md:gap-4 w-full'):
                    
                    # Recycle
                    with ui.column().classes('items-center'):
                        ui.icon('recycling', size='lg').classes('text-cyan-600')
                        ui.label('Recycle').classes('text-xs font-bold text-slate-700 mt-1')
                    
                    ui.label('+').classes('text-xl font-bold text-slate-400')
                    
                    # Fibre
                    with ui.column().classes('items-center'):
                        ui.icon('grain', size='lg').classes('text-cyan-600')
                        ui.label('Fibre').classes('text-xs font-bold text-slate-700 mt-1')
                    
                    ui.label('+').classes('text-xl font-bold text-slate-400')
                    
                    # Yarn
                    with ui.column().classes('items-center'):
                        ui.icon('texture', size='lg').classes('text-cyan-600')
                        ui.label('Yarn').classes('text-xs font-bold text-slate-700 mt-1')
                    
                    ui.label('=').classes('text-xl font-bold text-slate-400')
                    
                    # TexSource
                    with ui.column().classes('items-center'):
                        ui.image('Texsourcelogo.jpeg').classes('w-12 h-12 rounded-full border border-sky-300')
                        ui.label('TexSource').classes('text-xs font-extrabold text-sky-900 mt-1')

            # Value Proposition Block
            with ui.card().classes('p-6 bg-white border border-slate-200 shadow-md rounded-xl text-center'):
                ui.label('VALUE PROPOSITION').classes('text-base font-extrabold text-sky-900 tracking-wider mb-6 w-full')
                with ui.row().classes('items-center justify-center gap-3 md:gap-6 w-full'):
                    
                    with ui.column().classes('items-center max-w-[100px]'):
                        ui.icon('sync', size='lg').classes('text-teal-600')
                        ui.label('Circular by Design').classes('text-xs font-bold text-slate-700 mt-1')

                    ui.icon('compare_arrows', size='md').classes('text-sky-500')

                    with ui.column().classes('items-center max-w-[100px]'):
                        ui.icon('eco', size='lg').classes('text-teal-600')
                        ui.label('Sustainable Materials').classes('text-xs font-bold text-slate-700 mt-1')

                    ui.icon('compare_arrows', size='md').classes('text-sky-500')

                    with ui.column().classes('items-center max-w-[100px]'):
                        ui.icon('public', size='lg').classes('text-teal-600')
                        ui.label('Better for the Planet').classes('text-xs font-bold text-slate-700 mt-1')

        # ==========================================
        # CORE PRODUCT PORTFOLIO
        # ==========================================
        with ui.card().classes('w-full p-6 md:p-8 bg-white border border-slate-200 shadow-md rounded-xl'):
            ui.label('CORE PRODUCT PORTFOLIO').classes('text-xl font-black text-slate-900 mb-6 text-center tracking-wide w-full')

            with ui.grid().classes('grid-cols-1 md:grid-cols-3 gap-6 w-full'):
                
                # 01 UPSTREAM POLYMERS
                with ui.card().classes('p-6 bg-sky-50/50 border-t-4 border-sky-600 rounded-lg flex flex-col justify-between'):
                    with ui.column().classes('w-full gap-2'):
                        ui.label('01').classes('text-3xl font-black text-sky-600')
                        ui.label('UPSTREAM POLYMERS').classes('text-base font-bold text-slate-900 mb-2')
                        
                        items = [
                            'PET Scrap',
                            'Sheet Grade PET Lumps',
                            'PET Flakes & Regrind'
                        ]
                        for item in items:
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('check', size='xs').classes('text-sky-600')
                                ui.label(item).classes('text-xs text-slate-700 font-medium')
                    
                    with ui.card().classes('w-full p-2 mt-4 bg-sky-600 text-white text-center rounded font-bold text-xs'):
                        ui.label('→ High-Grade rPSF')

                # 02 POLYESTER STAPLE FIBER
                with ui.card().classes('p-6 bg-sky-50/50 border-t-4 border-sky-600 rounded-lg flex flex-col justify-between'):
                    with ui.column().classes('w-full gap-2'):
                        ui.label('02').classes('text-3xl font-black text-sky-600')
                        ui.label('POLYESTER STAPLE FIBER').classes('text-base font-bold text-slate-900 mb-2')
                        
                        items = [
                            'Virgin PSF',
                            'Premium Grade rPSF'
                        ]
                        for item in items:
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('check', size='xs').classes('text-sky-600')
                                ui.label(item).classes('text-xs text-slate-700 font-medium')
                    
                    with ui.card().classes('w-full p-2 mt-4 bg-sky-600 text-white text-center rounded font-bold text-xs'):
                        ui.label('→ Spinning Mills → Wovens\n→ Non-Wovens & Technical Textiles').classes('whitespace-pre-line')

                # 03 YARN PORTFOLIO
                with ui.card().classes('p-6 bg-sky-50/50 border-t-4 border-sky-600 rounded-lg flex flex-col justify-between'):
                    with ui.column().classes('w-full gap-2'):
                        ui.label('03').classes('text-3xl font-black text-sky-600')
                        ui.label('YARN PORTFOLIO').classes('text-base font-bold text-slate-900 mb-2')
                        
                        items = [
                            'Texturized Yarns (DTY)',
                            'PV Spun Yarn',
                            '100% Polyester Spun Yarn'
                        ]
                        for item in items:
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('check', size='xs').classes('text-sky-600')
                                ui.label(item).classes('text-xs text-slate-700 font-medium')
                    
                    with ui.card().classes('w-full p-2 mt-4 bg-sky-600 text-white text-center rounded font-bold text-xs'):
                        ui.label('→ Rapier & Airjet Weaving')
#  Run local web server
ui.run(title='Praveen Portfolio', reload=True, port=8080)
import os
from nicegui import app, ui

# Serve files from current directory under /static
app.add_static_files('/static', '.')

# ... your full UI code, components, and pages here ...

# Get dynamic port from environment (Render) or default to 10000 (Local)
port = int(os.environ.get('PORT', 10000))

ui.run(
    host='0.0.0.0',
    port=port,
    reload=False,
    title='Pro Fincap Services',
    favicon='favicon.jpg'  # Replace with your actual small icon filename
)
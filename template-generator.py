import uuid
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import os
from datetime import datetime
import webbrowser

class TemplateGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("TECSO iPhone Profile Generator")
        self.root.geometry("800x900")
        self.root.resizable(True, True)
        
        # TECSO Color Scheme - Neon GitHub style
        self.colors = {
            'bg_primary': '#0d1117',      # Dark GitHub background
            'bg_secondary': '#161b22',     # Secondary dark
            'bg_tertiary': '#21262d',      # Tertiary dark
            'accent_green': '#00ff87',     # Neon green
            'accent_purple': '#8b5cf6',    # Purple accent
            'text_primary': '#f0f6fc',     # Light text
            'text_secondary': '#8b949e',   # Gray text
            'border': '#30363d',           # Border color
            'button_bg': '#238636',        # Button background
            'button_hover': '#2ea043'      # Button hover
        }
        
        # Configure root window
        self.root.configure(bg=self.colors['bg_primary'])
        
        # Configure custom styles
        self.setup_styles()
        self.setup_ui()
        
    def setup_styles(self):
        """Setup custom ttk styles for TECSO theme"""
        style = ttk.Style()
        
        # Configure main theme
        style.theme_use('clam')
        
        # Configure styles
        style.configure('Title.TLabel', 
                       background=self.colors['bg_primary'],
                       foreground=self.colors['accent_green'],
                       font=('Segoe UI', 18, 'bold'))
        
        style.configure('Subtitle.TLabel',
                       background=self.colors['bg_primary'],
                       foreground=self.colors['accent_purple'],
                       font=('Segoe UI', 12, 'bold'))
        
        style.configure('Info.TLabel',
                       background=self.colors['bg_primary'],
                       foreground=self.colors['text_secondary'],
                       font=('Segoe UI', 9))
        
        style.configure('Contact.TLabel',
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 8))
        
        style.configure('Brand.TFrame',
                       background=self.colors['bg_secondary'],
                       relief='solid',
                       borderwidth=1)
        
        style.configure('Main.TFrame',
                       background=self.colors['bg_primary'])
        
        style.configure('Secondary.TFrame',
                       background=self.colors['bg_secondary'],
                       relief='solid',
                       borderwidth=1)
        
        style.configure('TECSO.TButton',
                       background=self.colors['button_bg'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 10, 'bold'),
                       relief='flat',
                       borderwidth=0)
        
        style.map('TECSO.TButton',
                 background=[('active', self.colors['button_hover']),
                           ('pressed', self.colors['accent_green'])])
        
        style.configure('Accent.TButton',
                       background=self.colors['accent_purple'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 11, 'bold'),
                       relief='flat',
                       borderwidth=0)
        
        style.configure('Custom.TEntry',
                       fieldbackground=self.colors['bg_tertiary'],
                       foreground=self.colors['text_primary'],
                       bordercolor=self.colors['border'],
                       insertcolor=self.colors['accent_green'])
        
        style.configure('Custom.TCombobox',
                       fieldbackground=self.colors['bg_tertiary'],
                       foreground=self.colors['text_primary'],
                       bordercolor=self.colors['border'])
        
        style.configure('Custom.TLabelFrame',
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['accent_green'],
                       relief='solid',
                       borderwidth=1)
        
        style.configure('Custom.TLabelFrame.Label',
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['accent_green'],
                       font=('Segoe UI', 10, 'bold'))
        
        style.configure('Custom.TRadiobutton',
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 10))
        
    def setup_ui(self):
        # Main container
        container = ttk.Frame(self.root, style='Main.TFrame')
        container.pack(fill=tk.BOTH, expand=True)
        
        # Create scrollable canvas
        canvas = tk.Canvas(container, bg=self.colors['bg_primary'], highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors['bg_primary'])
        
        # Configure scrolling
        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        
        def on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        scrollable_frame.bind("<Configure>", configure_scroll_region)
        canvas.bind("<MouseWheel>", on_mousewheel)
        
        # Create window in canvas
        canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        
        # Configure canvas scrolling
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Update canvas width when container resizes
        def configure_canvas_width(event):
            canvas.itemconfig(canvas_window, width=event.width)
        container.bind("<Configure>", configure_canvas_width)
        
        # TECSO Header
        header_frame = tk.Frame(scrollable_frame, bg=self.colors['bg_secondary'], relief='solid', bd=2)
        header_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        
        # TECSO Logo/Title
        title_label = tk.Label(header_frame, text="🚀 TECSO", 
                              bg=self.colors['bg_secondary'], fg=self.colors['accent_green'],
                              font=('Segoe UI', 20, 'bold'))
        title_label.pack(pady=(15, 5))
        
        subtitle_label = tk.Label(header_frame, text="iPhone Profile Generator", 
                                 bg=self.colors['bg_secondary'], fg=self.colors['accent_purple'],
                                 font=('Segoe UI', 14, 'bold'))
        subtitle_label.pack(pady=(0, 5))
        
        tagline_label = tk.Label(header_frame, text="Professional Mobile Configuration Tools", 
                               bg=self.colors['bg_secondary'], fg=self.colors['text_secondary'],
                               font=('Segoe UI', 10))
        tagline_label.pack(pady=(0, 15))
        
        # Contact Section
        contact_frame = tk.Frame(scrollable_frame, bg=self.colors['bg_secondary'], relief='solid', bd=1)
        contact_frame.pack(fill=tk.X, padx=20, pady=(0, 10))
        
        contact_title = tk.Label(contact_frame, text="🔗 Contact & Support", 
                                bg=self.colors['bg_secondary'], fg=self.colors['accent_green'],
                                font=('Segoe UI', 12, 'bold'))
        contact_title.pack(pady=(15, 10))
        
        # Create contact grid with proper layout
        contact_grid = tk.Frame(contact_frame, bg=self.colors['bg_secondary'])
        contact_grid.pack(padx=15, pady=(0, 15), fill=tk.X)
        
        # Contact information
        contact_info = [
            ("👨‍💻 COD: Ashkan Maleki", "+98 914 445 4463", self.open_phone),
            ("👔 CEO: Sobhan Azimzadeh", "+98 0905 843 2452", self.open_phone),
            ("📱 Telegram Support", "+98 992 206 8945", self.open_telegram),
            ("📧 Email", "tecsoteam@gmail.com", self.open_email),
            ("🌐 Website", "tecso.team", self.open_website),
            ("📷 Instagram", "@tecso.team", self.open_instagram),
            ("💼 GitHub", "Tecso-Dev", self.open_github),
            ("🔗 LinkedIn", "Sobhan Azimzadeh", self.open_linkedin),
            ("📄 Resume", "cv.tecso.team", self.open_resume)
        ]
        
        # Create contact buttons in a 3-column grid
        for i, (label, value, command) in enumerate(contact_info):
            row = i // 3
            col = i % 3
            
            contact_btn = tk.Button(contact_grid, text=f"{label}\n{value}", 
                                   command=command, bg=self.colors['button_bg'],
                                   fg=self.colors['text_primary'], font=('Segoe UI', 8),
                                   relief='flat', bd=0, width=22, height=3,
                                   activebackground=self.colors['button_hover'])
            contact_btn.grid(row=row, column=col, padx=3, pady=3, sticky="ew")
        
        # Configure grid column weights for proper resizing
        for i in range(3):
            contact_grid.columnconfigure(i, weight=1)
        
        # Main content area
        content_frame = tk.Frame(scrollable_frame, bg=self.colors['bg_primary'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Operator selection
        operator_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief='solid', bd=1)
        operator_frame.pack(fill=tk.X, pady=(0, 15))
        
        operator_title = tk.Label(operator_frame, text="📡 Select Operator", 
                                 bg=self.colors['bg_secondary'], fg=self.colors['accent_green'],
                                 font=('Segoe UI', 12, 'bold'))
        operator_title.pack(pady=(15, 10))
        
        self.operator_var = tk.StringVar(value="Hamrah Aval")
        operators = ["All Operators", "Hamrah Aval", "Irancell", "Rightel"]
        
        operator_grid = tk.Frame(operator_frame, bg=self.colors['bg_secondary'])
        operator_grid.pack(padx=15, pady=(0, 15), fill=tk.X)
        
        for i, operator in enumerate(operators):
            tk.Radiobutton(operator_grid, text=f"📶 {operator}", 
                          variable=self.operator_var, value=operator,
                          bg=self.colors['bg_secondary'], fg=self.colors['text_primary'],
                          selectcolor=self.colors['bg_tertiary'], font=('Segoe UI', 10),
                          activebackground=self.colors['bg_secondary']).grid(
                          row=i//2, column=i%2, sticky=tk.W, padx=10, pady=5)
        
        # Configure operator grid
        operator_grid.columnconfigure(0, weight=1)
        operator_grid.columnconfigure(1, weight=1)
        
        # Profile details
        details_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief='solid', bd=1)
        details_frame.pack(fill=tk.X, pady=(0, 15))
        
        details_title = tk.Label(details_frame, text="⚙️ Profile Configuration", 
                               bg=self.colors['bg_secondary'], fg=self.colors['accent_green'],
                               font=('Segoe UI', 12, 'bold'))
        details_title.pack(pady=(15, 10))
        
        details_grid = tk.Frame(details_frame, bg=self.colors['bg_secondary'])
        details_grid.pack(padx=15, pady=(0, 15), fill=tk.X)
        
        # Profile name
        tk.Label(details_grid, text="📝 Profile Name:", bg=self.colors['bg_secondary'], 
                fg=self.colors['text_secondary'], font=('Segoe UI', 10)).grid(
                row=0, column=0, sticky=tk.W, pady=8, padx=(0, 10))
        self.profile_name = ttk.Entry(details_grid, width=40, style='Custom.TEntry')
        self.profile_name.grid(row=0, column=1, sticky=tk.EW, pady=8)
        self.profile_name.insert(0, f"TECSO-Iran-Antenna-{datetime.now().strftime('%Y%m%d')}")
        
        # Organization
        tk.Label(details_grid, text="🏢 Organization:", bg=self.colors['bg_secondary'], 
                fg=self.colors['text_secondary'], font=('Segoe UI', 10)).grid(
                row=1, column=0, sticky=tk.W, pady=8, padx=(0, 10))
        self.organization = ttk.Entry(details_grid, width=40, style='Custom.TEntry')
        self.organization.grid(row=1, column=1, sticky=tk.EW, pady=8)
        self.organization.insert(0, "TECSO Team")
        
        # Description
        tk.Label(details_grid, text="📋 Description:", bg=self.colors['bg_secondary'], 
                fg=self.colors['text_secondary'], font=('Segoe UI', 10)).grid(
                row=2, column=0, sticky=tk.W, pady=8, padx=(0, 10))
        self.description = ttk.Entry(details_grid, width=40, style='Custom.TEntry')
        self.description.grid(row=2, column=1, sticky=tk.EW, pady=8)
        self.description.insert(0, "Professional cellular configuration by TECSO")
        
        # Configure details grid
        details_grid.columnconfigure(1, weight=1)
        
        # UUID section
        uuid_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief='solid', bd=1)
        uuid_frame.pack(fill=tk.X, pady=(0, 15))
        
        uuid_title = tk.Label(uuid_frame, text="🔑 UUID Management", 
                             bg=self.colors['bg_secondary'], fg=self.colors['accent_green'],
                             font=('Segoe UI', 12, 'bold'))
        uuid_title.pack(pady=(15, 10))
        
        uuid_grid = tk.Frame(uuid_frame, bg=self.colors['bg_secondary'])
        uuid_grid.pack(padx=15, pady=(0, 15), fill=tk.X)
        
        # Generated UUID display
        tk.Label(uuid_grid, text="🆔 Generated UUID:", bg=self.colors['bg_secondary'], 
                fg=self.colors['text_secondary'], font=('Segoe UI', 10)).grid(
                row=0, column=0, sticky=tk.W, pady=8, padx=(0, 10))
        self.uuid_entry = ttk.Entry(uuid_grid, width=50, font=("Consolas", 10), style='Custom.TEntry')
        self.uuid_entry.grid(row=0, column=1, sticky=tk.EW, pady=8, padx=(0, 10))
        
        # Generate new UUID button
        ttk.Button(uuid_grid, text="🔄 Generate New", 
                  command=self.generate_new_uuid, style='Accent.TButton').grid(
                  row=0, column=2, pady=8)
        
        # Configure UUID grid
        uuid_grid.columnconfigure(1, weight=1)
        
        # APN Settings
        apn_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief='solid', bd=1)
        apn_frame.pack(fill=tk.X, pady=(0, 15))
        
        apn_title = tk.Label(apn_frame, text="🌐 APN Configuration", 
                           bg=self.colors['bg_secondary'], fg=self.colors['accent_green'],
                           font=('Segoe UI', 12, 'bold'))
        apn_title.pack(pady=(15, 10))
        
        apn_grid = tk.Frame(apn_frame, bg=self.colors['bg_secondary'])
        apn_grid.pack(padx=15, pady=(0, 15), fill=tk.X)
        
        # APN Type
        tk.Label(apn_grid, text="📡 APN Type:", bg=self.colors['bg_secondary'], 
                fg=self.colors['text_secondary'], font=('Segoe UI', 10)).grid(
                row=0, column=0, sticky=tk.W, pady=8, padx=(0, 10))
        self.apn_type = ttk.Combobox(apn_grid, values=["mcinet", "mtnirancell"], 
                                   width=15, style='Custom.TCombobox')
        self.apn_type.grid(row=0, column=1, sticky=tk.W, pady=8, padx=(0, 20))
        self.apn_type.set("mcinet")
        
        # Auth Type
        tk.Label(apn_grid, text="🔐 Auth Type:", bg=self.colors['bg_secondary'], 
                fg=self.colors['text_secondary'], font=('Segoe UI', 10)).grid(
                row=0, column=2, sticky=tk.W, pady=8, padx=(0, 10))
        self.auth_type = ttk.Combobox(apn_grid, values=["CHAP", "PAP"], 
                                    width=10, style='Custom.TCombobox')
        self.auth_type.grid(row=0, column=3, sticky=tk.W, pady=8, padx=(0, 20))
        self.auth_type.set("CHAP")
        
        # IP Version
        tk.Label(apn_grid, text="🌍 IP Version:", bg=self.colors['bg_secondary'], 
                fg=self.colors['text_secondary'], font=('Segoe UI', 10)).grid(
                row=1, column=0, sticky=tk.W, pady=8, padx=(0, 10))
        self.ip_version = ttk.Combobox(apn_grid, values=["IPv4", "IPv6", "IPv4v6"], 
                                     width=15, style='Custom.TCombobox')
        self.ip_version.grid(row=1, column=1, sticky=tk.W, pady=8)
        self.ip_version.set("IPv4")
        
        # Action Buttons
        button_frame = tk.Frame(content_frame, bg=self.colors['bg_primary'])
        button_frame.pack(fill=tk.X, pady=20)
        
        # Center the buttons
        button_container = tk.Frame(button_frame, bg=self.colors['bg_primary'])
        button_container.pack()
        
        ttk.Button(button_container, text="⚡ Generate Template", 
                  command=self.generate_template, style='Accent.TButton').pack(side=tk.LEFT, padx=10)
        
        ttk.Button(button_container, text="💾 Save Template", 
                  command=self.save_template, style='TECSO.TButton').pack(side=tk.LEFT, padx=10)
        
        ttk.Button(button_container, text="📂 Load Template", 
                  command=self.load_template, style='TECSO.TButton').pack(side=tk.LEFT, padx=10)
        
        # Output text area
        output_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief='solid', bd=1)
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(15, 0))
        
        output_title = tk.Label(output_frame, text="📄 Generated Configuration", 
                              bg=self.colors['bg_secondary'], fg=self.colors['accent_green'],
                              font=('Segoe UI', 12, 'bold'))
        output_title.pack(pady=(15, 10))
        
        # Text widget with scrollbar in a proper container
        text_container = tk.Frame(output_frame, bg=self.colors['bg_secondary'])
        text_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        self.output_text = tk.Text(text_container, wrap=tk.WORD, font=("Consolas", 9),
                                  bg=self.colors['bg_tertiary'], fg=self.colors['text_primary'],
                                  insertbackground=self.colors['accent_green'],
                                  selectbackground=self.colors['accent_purple'],
                                  height=15)  # Fixed height for better layout
        
        output_scrollbar = ttk.Scrollbar(text_container, orient=tk.VERTICAL, command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=output_scrollbar.set)
        
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Status label
        self.status_label = tk.Label(content_frame, text="✅ Ready to generate TECSO profile", 
                                    font=('Segoe UI', 10), fg=self.colors['accent_green'],
                                    bg=self.colors['bg_primary'])
        self.status_label.pack(pady=15)
        
        # Footer
        footer_frame = tk.Frame(content_frame, bg=self.colors['bg_secondary'], relief='solid', bd=1)
        footer_frame.pack(fill=tk.X, pady=(20, 0))
        
        footer_label = tk.Label(footer_frame, 
                               text="© 2025 TECSO Team - Professional Mobile Solutions", 
                               font=('Segoe UI', 9), fg=self.colors['text_secondary'],
                               bg=self.colors['bg_secondary'])
        footer_label.pack(pady=10)
        
        # Generate initial UUID
        self.generate_new_uuid()
        
        # Bind mousewheel to scrollable area
        def bind_mousewheel(widget):
            widget.bind("<MouseWheel>", on_mousewheel)
            
        # Apply mousewheel binding to all child widgets
        def bind_tree(widget):
            bind_mousewheel(widget)
            for child in widget.winfo_children():
                bind_tree(child)
                
        bind_tree(scrollable_frame)
    
    # Contact methods
    def open_phone(self):
        messagebox.showinfo("Phone", "Please dial the number manually from your phone")
    
    def open_telegram(self):
        webbrowser.open("https://t.me/+989922068945")
        
    def open_email(self):
        webbrowser.open("mailto:tecsoteam@gmail.com")
        
    def open_website(self):
        webbrowser.open("https://tecso.team")
        
    def open_instagram(self):
        webbrowser.open("https://instagram.com/tecso.team")
        
    def open_github(self):
        webbrowser.open("https://github.com/Tecso-Dev")
        
    def open_linkedin(self):
        webbrowser.open("https://linkedin.com/in/sobhan-azimzadeh")
        
    def open_resume(self):
        webbrowser.open("https://cv.tecso.team")
        
    def generate_new_uuid(self):
        """Generate a new UUID"""
        new_uuid = str(uuid.uuid4())
        self.uuid_entry.delete(0, tk.END)
        self.uuid_entry.insert(0, new_uuid)
        # Status update with TECSO branding
        self.status_label.config(text="🔥 New UUID generated by TECSO!", foreground=self.colors['accent_green'])
        
    def get_template_content(self, operator, profile_uuid, profile_name, organization, description, apn_type, auth_type, ip_version):
        """Generate the mobile config template content"""
        
        # Base template structure
        template = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>APNs</key>
            <array>
                <dict>
                    <key>APN</key>
                    <string>{apn_type}</string>
                    <key>Name</key>
                    <string>{operator} Data</string>
                    <key>Username</key>
                    <string></string>
                    <key>Password</key>
                    <string></string>
                    <key>ProxyServer</key>
                    <string></string>
                    <key>ProxyPort</key>
                    <integer>0</integer>
                    <key>DefaultProtocolMask</key>
                    <integer>3</integer>
                    <key>AllowedProtocolMask</key>
                    <integer>3</integer>
                    <key>AuthenticationType</key>
                    <string>{auth_type}</string>
                </dict>
            </array>
            <key>AttachAPN</key>
            <dict>
                <key>APN</key>
                <string>{apn_type}</string>
                <key>Name</key>
                <string>{operator} Attach</string>
                <key>Username</key>
                <string></string>
                <key>Password</key>
                <string></string>
                <key>AuthenticationType</key>
                <string>{auth_type}</string>
            </dict>
            <key>PayloadDisplayName</key>
            <string>{operator} Cellular</string>
            <key>PayloadIdentifier</key>
            <string>com.apple.cellular.{profile_uuid}</string>
            <key>PayloadType</key>
            <string>com.apple.cellular</string>
            <key>PayloadUUID</key>
            <string>{profile_uuid}</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>{profile_name}</string>
    <key>PayloadIdentifier</key>
    <string>com.apple.profile.{profile_uuid}</string>
    <key>PayloadOrganization</key>
    <string>{organization}</string>
    <key>PayloadRemovalDisallowed</key>
    <false/>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>{profile_uuid}</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
    <key>PayloadDescription</key>
    <string>{description}</string>
</dict>
</plist>'''
        return template
        
    def generate_template(self):
        """Generate the mobile config template"""
        try:
            operator = self.operator_var.get()
            profile_uuid = self.uuid_entry.get().strip()
            profile_name = self.profile_name.get().strip()
            organization = self.organization.get().strip()
            description = self.description.get().strip()
            apn_type = self.apn_type.get()
            auth_type = self.auth_type.get()
            ip_version = self.ip_version.get()
            
            if not profile_uuid:
                messagebox.showerror("Error", "Please generate a UUID first!")
                return
                
            if not profile_name:
                messagebox.showerror("Error", "Please enter a profile name!")
                return
            
            # Generate template content
            template_content = self.get_template_content(
                operator, profile_uuid, profile_name, organization, 
                description, apn_type, auth_type, ip_version
            )
            
            # Display in output text
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(1.0, template_content)
            
            self.status_label.config(text=f"🚀 TECSO template generated for {operator}!", foreground=self.colors['accent_green'])
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate template: {str(e)}")
            
    def save_template(self):
        """Save the generated template to a file"""
        try:
            content = self.output_text.get(1.0, tk.END).strip()
            if not content:
                messagebox.showwarning("Warning", "No template content to save!")
                return
            
            # Sanitize filename components
            operator = self.operator_var.get().replace(" ", "-").replace("/", "-")
            profile_name = self.profile_name.get().strip()
            if not profile_name:
                profile_name = "iPhone-Profile"
            profile_name = profile_name.replace(" ", "-").replace("/", "-")
            
            # Create safe filename
            timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
            filename = f"{profile_name}-{operator}-{timestamp}.mobileconfig"
            
            # Remove any invalid characters from filename
            invalid_chars = '<>:"|?*'
            for char in invalid_chars:
                filename = filename.replace(char, "-")
            
            # Show save dialog
            file_path = filedialog.asksaveasfilename(
                title="Save Mobile Configuration",
                defaultextension=".mobileconfig",
                filetypes=[("Mobile Config Files", "*.mobileconfig"), ("All Files", "*.*")],
                initialfile=filename
            )
            
            if file_path:
                # Ensure the file has the correct extension
                if not file_path.lower().endswith('.mobileconfig'):
                    file_path += '.mobileconfig'
                
                # Write the file
                with open(file_path, 'w', encoding='utf-8', newline='') as f:
                    f.write(content)
                
                # Update status
                self.status_label.config(text=f"💾 TECSO: Saved {os.path.basename(file_path)}", 
                                       foreground=self.colors['accent_purple'])
                messagebox.showinfo("Success", f"Template saved successfully!\n\nFile: {os.path.basename(file_path)}")
            else:
                self.status_label.config(text="❌ Save cancelled", foreground=self.colors['text_secondary'])
                
        except PermissionError:
            messagebox.showerror("Permission Error", "Cannot save file. Please check file permissions or choose a different location.")
            self.status_label.config(text="Permission error", foreground="red")
        except FileNotFoundError:
            messagebox.showerror("Path Error", "Invalid file path. Please choose a different location.")
            self.status_label.config(text="Invalid path", foreground="red")
        except Exception as e:
            error_msg = f"Failed to save template: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.status_label.config(text="Save failed", foreground="red")
            print(f"Save error details: {e}")  # For debugging
            
    def load_template(self):
        """Load an existing template file"""
        try:
            file_path = filedialog.askopenfilename(
                title="Load Mobile Configuration",
                filetypes=[("Mobile Config Files", "*.mobileconfig"), ("XML Files", "*.xml"), ("All Files", "*.*")]
            )
            
            if file_path:
                # Check if file exists
                if not os.path.exists(file_path):
                    messagebox.showerror("File Error", "Selected file does not exist.")
                    return
                
                # Read the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Clear and load content
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(1.0, content)
                
                # Update status
                self.status_label.config(text=f"📂 TECSO: Loaded {os.path.basename(file_path)}", 
                                       foreground=self.colors['accent_purple'])
                messagebox.showinfo("Success", f"Template loaded successfully!\n\nFile: {os.path.basename(file_path)}")
            else:
                self.status_label.config(text="Load cancelled", foreground="orange")
                
        except PermissionError:
            messagebox.showerror("Permission Error", "Cannot read file. Please check file permissions.")
            self.status_label.config(text="Permission error", foreground="red")
        except UnicodeDecodeError:
            messagebox.showerror("Encoding Error", "Cannot read file. File may be corrupted or in wrong format.")
            self.status_label.config(text="Encoding error", foreground="red")
        except Exception as e:
            error_msg = f"Failed to load template: {str(e)}"
            messagebox.showerror("Error", error_msg)
            self.status_label.config(text="Load failed", foreground="red")
            print(f"Load error details: {e}")  # For debugging

def main():
    root = tk.Tk()
    app = TemplateGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
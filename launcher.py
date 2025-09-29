import tkinter as tk
from tkinter import ttk
import subprocess
import os
import webbrowser

class LauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 TECSO Professional Tools")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # TECSO Color Scheme
        self.colors = {
            'bg_primary': '#0d1117',
            'bg_secondary': '#161b22',
            'bg_tertiary': '#21262d',
            'accent_green': '#00ff87',
            'accent_purple': '#8b5cf6',
            'text_primary': '#f0f6fc',
            'text_secondary': '#8b949e'
        }
        
        self.root.configure(bg=self.colors['bg_primary'])
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_styles()
        self.setup_ui()
        
    def setup_styles(self):
        """Setup TECSO custom styles"""
        style = ttk.Style()
        
        style.configure('Title.TLabel', 
                       background=self.colors['bg_primary'],
                       foreground=self.colors['accent_green'],
                       font=('Segoe UI', 24, 'bold'))
        
        style.configure('Subtitle.TLabel',
                       background=self.colors['bg_primary'],
                       foreground=self.colors['accent_purple'],
                       font=('Segoe UI', 14, 'bold'))
        
        style.configure('Info.TLabel',
                       background=self.colors['bg_primary'],
                       foreground=self.colors['text_secondary'],
                       font=('Segoe UI', 10))
        
        style.configure('Contact.TLabel',
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 9))
        
        style.configure('TECSO.TFrame',
                       background=self.colors['bg_secondary'],
                       relief='solid',
                       borderwidth=1)
        
        style.configure('Main.TFrame',
                       background=self.colors['bg_primary'])
        
        style.configure('TECSO.TButton',
                       background='#238636',
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 12, 'bold'),
                       relief='flat',
                       borderwidth=0)
        
        style.configure('Accent.TButton',
                       background=self.colors['accent_purple'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 11, 'bold'),
                       relief='flat',
                       borderwidth=0)
        
        style.configure('Contact.TButton',
                       background=self.colors['bg_tertiary'],
                       foreground=self.colors['text_primary'],
                       font=('Segoe UI', 9),
                       relief='flat',
                       borderwidth=0)
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, style='Main.TFrame', padding="30")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # TECSO Header
        header_frame = ttk.Frame(main_frame, style='TECSO.TFrame', padding="25")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        title_label = ttk.Label(header_frame, text="🚀 TECSO", style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(header_frame, text="Professional iPhone Tools", style='Subtitle.TLabel')
        subtitle_label.pack(pady=(0, 10))
        
        tagline_label = ttk.Label(header_frame, text="Advanced Mobile Configuration Suite", style='Info.TLabel')
        tagline_label.pack()
        
        # Tools Section
        tools_frame = ttk.Frame(main_frame, style='TECSO.TFrame', padding="20")
        tools_frame.pack(fill=tk.X, pady=(0, 20))
        
        tools_label = ttk.Label(tools_frame, text="🛠️ Available Tools", style='Subtitle.TLabel')
        tools_label.pack(pady=(0, 15))
        
        # UUID Generator button
        uuid_btn = ttk.Button(tools_frame, text="🆔 UUID Generator\nGenerate unique identifiers", 
                             command=self.launch_uuid_generator,
                             width=30, style="Accent.TButton")
        uuid_btn.pack(pady=8)
        
        # Template Generator button
        template_btn = ttk.Button(tools_frame, text="📱 Template Generator\nCreate mobile configuration files", 
                                 command=self.launch_template_generator,
                                 width=30, style="TECSO.TButton")
        template_btn.pack(pady=8)
        
        # Contact Section
        contact_frame = ttk.Frame(main_frame, style='TECSO.TFrame', padding="20")
        contact_frame.pack(fill=tk.X, pady=(0, 20))
        
        contact_label = ttk.Label(contact_frame, text="🔗 TECSO Contact", style='Subtitle.TLabel')
        contact_label.pack(pady=(0, 10))
        
        # Contact buttons in grid
        contact_buttons = ttk.Frame(contact_frame, style='TECSO.TFrame')
        contact_buttons.pack()
        
        contact_info = [
            ("📱 Telegram", self.open_telegram),
            ("📧 Email", self.open_email),
            ("🌐 Website", self.open_website),
            ("💻 GitHub", self.open_github)
        ]
        
        for i, (text, command) in enumerate(contact_info):
            btn = ttk.Button(contact_buttons, text=text, command=command, 
                           style='Contact.TButton', width=12)
            btn.grid(row=i//2, column=i%2, padx=8, pady=5)
        
        # Instructions
        instructions_frame = ttk.Frame(main_frame, style='Main.TFrame')
        instructions_frame.pack(fill=tk.X, pady=10)
        
        instructions = """🔧 Quick Start Guide:
1. UUID Generator - Create unique identifiers for profiles
2. Template Generator - Build complete mobile config files
3. Contact us for support and custom solutions"""
        
        instructions_label = tk.Label(instructions_frame, text=instructions, 
                                     font=("Segoe UI", 9), fg=self.colors['text_secondary'],
                                     bg=self.colors['bg_primary'], justify=tk.LEFT)
        instructions_label.pack()
        
        # Status
        self.status_label = tk.Label(main_frame, text="✅ TECSO Tools Ready", 
                                    font=("Segoe UI", 10), fg=self.colors['accent_green'],
                                    bg=self.colors['bg_primary'])
        self.status_label.pack(pady=10)
        
        # Footer
        footer_label = tk.Label(main_frame, text="© 2025 TECSO Team - Professional Mobile Solutions", 
                               font=("Segoe UI", 8), fg=self.colors['text_secondary'],
                               bg=self.colors['bg_primary'])
        footer_label.pack(side=tk.BOTTOM, pady=10)
    
    # Contact methods
    def open_telegram(self):
        webbrowser.open("https://t.me/+989922068945")
        self.status_label.config(text="🔗 Opening Telegram...", fg=self.colors['accent_purple'])
        
    def open_email(self):
        webbrowser.open("mailto:tecsoteam@gmail.com")
        self.status_label.config(text="📧 Opening Email...", fg=self.colors['accent_purple'])
        
    def open_website(self):
        webbrowser.open("https://tecso.team")
        self.status_label.config(text="🌐 Opening Website...", fg=self.colors['accent_purple'])
    
    def open_github(self):
        webbrowser.open("https://github.com/Tecso-Dev")
        self.status_label.config(text="💻 Opening GitHub...", fg=self.colors['accent_purple'])
        
    def launch_uuid_generator(self):
        """Launch the UUID Generator"""
        try:
            # Get the directory where the launcher is running from
            base_dir = os.path.dirname(os.path.abspath(__file__))
            exe_path = os.path.join(base_dir, "dist", "TECSO-UUID-Generator.exe")
            
            if os.path.exists(exe_path):
                subprocess.Popen([exe_path], cwd=base_dir)
                self.status_label.config(text="🆔 TECSO UUID Generator launched", fg=self.colors['accent_green'])
            else:
                self.status_label.config(text=f"❌ UUID Generator not found at: {exe_path}", fg='#ff6b6b')
        except Exception as e:
            self.status_label.config(text=f"❌ Error: {str(e)}", fg='#ff6b6b')
            
    def launch_template_generator(self):
        """Launch the Template Generator"""
        try:
            # Get the directory where the launcher is running from
            base_dir = os.path.dirname(os.path.abspath(__file__))
            exe_path = os.path.join(base_dir, "dist", "TECSO-Template-Generator-Updated.exe")
            
            if os.path.exists(exe_path):
                subprocess.Popen([exe_path], cwd=base_dir)
                self.status_label.config(text="📱 TECSO Template Generator launched", fg=self.colors['accent_green'])
            else:
                self.status_label.config(text=f"❌ Template Generator not found at: {exe_path}", fg='#ff6b6b')
        except Exception as e:
            self.status_label.config(text=f"❌ Error: {str(e)}", fg='#ff6b6b')

def main():
    root = tk.Tk()
    app = LauncherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
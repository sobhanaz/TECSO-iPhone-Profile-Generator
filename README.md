# 🚀 TECSO iPhone Profile Generator

<div align="center">

![TECSO Logo](https://img.shields.io/badge/TECSO-Professional%20Mobile%20Solutions-00ff87?style=for-the-badge&logo=apple&logoColor=white)

[![License: MIT](https://img.shields.io/badge/License-MIT-8b5cf6.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.13-00ff87?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows-8b5cf6?style=for-the-badge&logo=windows&logoColor=white)](https://windows.com)
[![iPhone](https://img.shields.io/badge/iPhone-14%20%7C%2015%20%7C%2016-00ff87?style=for-the-badge&logo=apple&logoColor=white)](https://apple.com)

**Professional Mobile Configuration Suite for Iranian Networks**

*Bypass restrictions • Maintain connectivity • Professional tools*

</div>

---

## 🌟 Overview

TECSO iPhone Profile Generator is a comprehensive suite of professional tools designed to create unique mobile configuration profiles for iPhone users in Iran. Our solution helps maintain reliable cellular connectivity by generating unique identifiers and complete mobile configuration files.

### ✨ Key Features

- 🆔 **UUID Generator** - Create unique identifiers to prevent profile blocking
- 📱 **Template Generator** - Build complete mobile configuration files  
- 🎨 **Modern UI** - Professional dark theme with neon accents
- 🔧 **Multi-Operator Support** - Hamrah Aval, Irancell, Rightel, All Networks
- 💾 **Easy Export** - Save as `.mobileconfig` files for iPhone installation
- 🚀 **Standalone Apps** - No installation required, just run the executables

---

## � Application Screenshots

<div align="center">

### 🚀 TECSO Professional Launcher
*Main hub for accessing all TECSO tools*

![TECSO Launcher](https://github.com/sobhanaz/TECSO-iPhone-Profile-Generator/blob/main/screenshots/Screenshot%202025-09-29%20150912.png)

---

### 🆔 UUID Generator
*Generate unique identifiers for mobile profiles*

![UUID Generator](https://github.com/sobhanaz/TECSO-iPhone-Profile-Generator/blob/main/screenshots/Screenshot%202025-09-29%20150951.png)

---

### 📱 Template Generator
*Create complete mobile configuration profiles*

![Template Generator](https://github.com/sobhanaz/TECSO-iPhone-Profile-Generator/blob/main/screenshots/image.png)

---

### 📋 Generated Configuration
*Live preview of mobile configuration XML*

![Configuration Preview](https://github.com/sobhanaz/TECSO-iPhone-Profile-Generator/blob/main/screenshots/Screenshot%202025-09-29%20150853.png)

</div>

> **📝 Note:** To capture screenshots, please:
> 1. Run each application from the `dist/` folder
> 2. Take screenshots of each tool's interface
> 3. Save them in the `screenshots/` folder with the names shown above
> 4. Recommended size: 1200x800 pixels for best quality

---

## �🛠️ Tools Included

### 1. 🆔 UUID Generator
Generate unique identifiers for mobile profiles to prevent blocking when multiple devices use the same configuration.

**Features:**
- ⚡ Instant UUID generation
- 📋 One-click copy to clipboard
- 🔑 Both standard and HEX formats
- 🎯 Professional interface

### 2. 📱 Template Generator  
Create complete mobile configuration profiles with customizable settings.

**Features:**
- 📡 Multi-operator support (Hamrah Aval, Irancell, Rightel)
- ⚙️ Configurable APN settings
- 🔧 Advanced authentication options
- 💾 Save/Load functionality
- 🎨 Live preview of generated XML

### 3. 🚀 Professional Launcher
Central hub for accessing all TECSO tools with integrated contact information.

**Features:**
- 🎯 Quick tool access
- 📞 Integrated contact buttons  
- 🌐 Direct links to TECSO resources
- ✨ Modern interface design

---

## 📱 Supported Networks

<div align="center">

| Operator | APN Type | Support Level | Status |
|----------|----------|---------------|---------|
| 📶 Hamrah Aval | `mcinet` | ✅ Full | Active |
| 📶 Irancell | `mtnirancell` | ✅ Full | Active |
| 📶 Rightel | `mcinet` | ✅ Full | Active |
| 📶 All Networks | `Universal` | ✅ Full | Active |

</div>

---

## 🎯 Quick Start

### Method 1: Use Pre-built Executables
1. **Download** the latest release from our repository
2. **Run** `TECSO-Launcher-Updated.exe` for the main interface
3. **Click** on the tool you need (UUID Generator or Template Generator)
4. **Generate** your unique profile and save as `.mobileconfig`
5. **Transfer** to iPhone and install via Settings

### Method 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/Tecso-Dev/Iphone-14-15-IRAN-Anten.git

# Navigate to directory
cd Iphone-14-15-IRAN-Anten

# Set up Python environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install pyperclip

# Run the tools
python uuid-Generator.py           # UUID Generator
python template-generator.py       # Template Generator
python launcher.py                 # Main Launcher
```

---

## 📖 Detailed Usage Guide

### 🔧 Creating a Mobile Profile

1. **Start the Template Generator**
   ```
   Run: TECSO-Template-Generator-Updated.exe
   ```

2. **Configure Your Profile**
   - Select your mobile operator
   - Enter profile name and organization
   - Generate or enter a unique UUID
   - Configure APN settings (defaults work for most cases)

3. **Generate and Save**
   - Click "⚡ Generate Template"
   - Review the generated XML
   - Click "💾 Save Template"
   - Save as `.mobileconfig` file

4. **Install on iPhone**
   - Transfer file to iPhone (AirDrop, email, etc.)
   - Open the file on iPhone
   - Go to Settings → VPN & Device Management
   - Install the profile
   - Enable cellular data and restart phone

### 🆔 Generating Unique UUIDs

```python
# Each profile needs a unique UUID to prevent blocking
UUID: d85183f5-84b7-4895-9eb3-eb76e7cd45ab
HEX:  d85183f584b748959eb3eb76e7cd45ab
```

**Why unique UUIDs matter:**
- Prevents profile detection and blocking
- Allows multiple devices to use different configurations
- Ensures reliable long-term connectivity

---

## 🏢 About TECSO

<div align="center">

**Professional Mobile Solutions & Software Development**

*Pioneering telecommunications technology since 2025*

</div>

### 👥 Leadership Team

| Role | Name | Contact |
|------|------|---------|
| 👔 **CEO** | Sobhan Azimzadeh | +98 0905 843 2452 |
| 👨‍💻 **COD** | Ashkan Maleki | +98 914 445 4463 |

### 📞 Contact Information

<div align="center">

[![Telegram](https://img.shields.io/badge/Telegram-+98%20992%20206%208945-00ff87?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/+989922068945)
[![Email](https://img.shields.io/badge/Email-tecsoteam@gmail.com-8b5cf6?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tecsoteam@gmail.com)
[![Website](https://img.shields.io/badge/Website-tecso.team-00ff87?style=for-the-badge&logo=globe&logoColor=white)](https://tecso.team)

[![GitHub](https://img.shields.io/badge/GitHub-Tecso--Dev-8b5cf6?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Tecso-Dev)
[![Instagram](https://img.shields.io/badge/Instagram-@tecso.team-00ff87?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/tecso.team)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sobhan%20Azimzadeh-8b5cf6?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sobhan-azimzadeh)

[![Resume](https://img.shields.io/badge/Resume-cv.tecso.team-00ff87?style=for-the-badge&logo=readthedocs&logoColor=white)](https://cv.tecso.team)

</div>

---

## 🔧 Technical Specifications

### System Requirements
- **OS**: Windows 10/11 (64-bit)
- **Memory**: 2GB RAM minimum
- **Storage**: 50MB available space
- **Network**: Internet connection for contact links

### Built With
- **Python 3.13** - Core development language
- **Tkinter** - GUI framework
- **PyInstaller** - Executable packaging
- **UUID Module** - Unique identifier generation

### File Structure
```
📁 TECSO-iPhone-Profile-Generator/
├── 📱 uuid-Generator.py                    # UUID generation tool
├── 📱 template-generator.py                # Profile template creator
├── 🚀 launcher.py                         # Main application launcher
├── � massive-config-generator.py          # Bulk UUID generation tool
├── �📁 dist/                               # Compiled executables
│   ├── TECSO-UUID-Generator.exe           # UUID Generator executable
│   ├── TECSO-Template-Generator-Updated.exe # Template Generator (latest)
│   ├── TECSO-Launcher-Updated.exe         # Professional Launcher (latest)
│   └── TECSO-Template-Generator-Fixed.exe # Template Generator (legacy)
├── 📁 screenshots/                        # Application preview images
│   ├── launcher-preview.png
│   ├── uuid-generator-preview.png
│   ├── template-generator-preview.png
│   └── configuration-preview.png
├── 📄 .gitignore                          # Git ignore rules
├── 📄 LICENSE                             # MIT License
├── 📖 README.md                           # This documentation
├── 📖 FA-README.md                        # Persian documentation
├── 📁 .venv/                              # Python virtual environment
└── 📋 *-template.mobileconfig             # Mobile configuration templates
    ├── Hamrah-Aval-template.mobileconfig
    ├── Irancell-template.mobileconfig
    ├── Rightel-template.mobileconfig
    └── Alloprators-template.mobileconfig
```

---

## 🚀 Development & Contribution

### Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/sobhanaz/TECSO-iPhone-Profile-Generator.git
cd Iphone-14-15-IRAN-Anten

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install pyperclip pyinstaller

# Run development versions
python uuid-Generator.py
python template-generator.py
python launcher.py
```

### Building Executables

```bash
# Build UUID Generator
pyinstaller --onefile --windowed uuid-Generator.py --name "TECSO-UUID-Generator"

# Build Template Generator  
pyinstaller --onefile --windowed template-generator.py --name "TECSO-Template-Generator-Updated"

# Build Launcher
pyinstaller --onefile --windowed launcher.py --name "TECSO-Launcher-Updated"
```

---

## 🛡️ Security & Privacy

### Security Features
- ✅ **No Data Collection** - All operations performed locally
- ✅ **Unique Identifiers** - Each profile gets a unique UUID
- ✅ **Secure Generation** - Cryptographically secure UUID generation
- ✅ **Open Source** - Full transparency of code and operations

### Privacy Policy
- We do **NOT** collect any personal data
- All profile generation is performed **locally**
- No network communication except for contact links
- Your configuration data **stays on your device**

---

## 🐛 Troubleshooting

### Common Issues

**Q: Profile not working after installation?**
A: Try generating a new UUID and creating a fresh profile. Ensure you're using the correct operator settings.

**Q: Save function not working?**
**A: Use the latest version: `TECSO-Template-Generator-Updated.exe`. All UI issues including scrolling and grid layouts have been fixed.

**Q: Executable won't run?**
A: Ensure you have Windows Defender exceptions set up. Some antivirus software may flag PyInstaller executables.

**Q: Profile gets blocked after some time?**
A: Generate a new UUID and create a fresh profile. This usually happens when multiple devices use the same UUID.

### Getting Help

1. **Check Issues** - Browse our [GitHub Issues](https://github.com/sobhanaz/TECSO-iPhone-Profile-Generator/issues)
2. **Contact Support** - Reach out via Telegram: +98 992 206 8945
3. **Email Support** - Send details to: tecsoteam@gmail.com
4. **Community** - Join our Telegram group for user discussions

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 TECSO Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

<div align="center">

**Made with ❤️ by TECSO Team**

*Professional Mobile Solutions • Reliable Connectivity • Iranian Networks*

[![TECSO](https://img.shields.io/badge/Powered%20by-TECSO-00ff87?style=for-the-badge&logo=apple&logoColor=white)](https://tecso.team)

---

**© 2025 TECSO Team. All rights reserved.**

*Connecting Iran, One Profile at a Time* 🇮🇷

</div>
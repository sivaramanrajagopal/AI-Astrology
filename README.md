# 🌟 Vedic Astrology Application

A comprehensive Vedic astrology application with planetary calculations, Dasa timelines, career insights, and AI-powered interpretations.

![Vedic Astrology](https://img.shields.io/badge/Astrology-Vedic-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Next.js](https://img.shields.io/badge/Next.js-14.0+-black)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-red)

## ✨ Features

- **🌌 Planetary Chart**: Complete birth chart with planetary positions
- **🔮 AI Predictions**: GPT-powered cosmic interpretations
- **💼 Career Insights**: Detailed career analysis and recommendations
- **⏰ Dasa Timeline**: Vimshottari Dasa calculations
- **📊 Dasa Bhukti**: Comprehensive Dasa-Bhukti analysis
- **⚡ Yogas & Doshas**: Detection of astrological combinations
- **🎯 Life Purpose**: Analysis of life purpose and spiritual path
- **💕 Spouse Analysis**: Marriage and relationship predictions
- **💰 Wealth Cycles**: Indu Lagnam-based prosperity analysis

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- OpenAI API key

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/sivaramanrajagopal/AI-Astrology.git
   cd AI-Astrology
   ```

2. **Setup Backend**
   ```bash
   cd astro-backend
   pip install -r requirements.txt
   cd astro-backend
   cp env_config_template.py env_config.py
   # Edit env_config.py with your OpenAI API key
   ```

3. **Setup Frontend**
   ```bash
   cd astro-frontend
   npm install
   ```

4. **Run the application**
   ```bash
   # Terminal 1 - Backend
   cd astro-backend/astro-backend
   python start_production.py
   
   # Terminal 2 - Frontend
   cd astro-frontend
   npm run dev
   ```

5. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://127.0.0.1:8000

## 🌐 Deployment

### Backend (Render)

1. **Create Render Account**: Sign up at [render.com](https://render.com)
2. **New Web Service**: 
   - Connect your GitHub repository
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `cd astro-backend && python start_production.py`
3. **Environment Variables**:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `ALLOWED_ORIGINS`: Your frontend domain

### Frontend (Vercel)

1. **Create Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **Import Project**: Connect your GitHub repository
3. **Environment Variables**:
   - `NEXT_PUBLIC_BACKEND_URL`: Your Render backend URL

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API status and available endpoints |
| `/predict` | GET | Planetary positions and predictions |
| `/career` | GET | Career analysis and insights |
| `/dasa` | GET | Vimshottari Dasa timeline |
| `/yogas` | GET | Yogas and doshas detection |
| `/life_purpose` | GET | Life purpose analysis |
| `/dasa_bhukti` | GET | Comprehensive Dasa-Bhukti analysis |
| `/spouse` | GET | Spouse and marriage analysis |
| `/indu_dasa` | GET | Indu Lagnam-based wealth cycles |

## 🔒 Security Features

- ✅ **API Key Security**: Environment variables only
- ✅ **Input Validation**: Comprehensive data validation
- ✅ **CORS Protection**: Restricted to specific domains
- ✅ **Error Handling**: Proper HTTP status codes
- ✅ **Rate Limiting**: Built-in protection against abuse

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern Python web framework
- **Swiss Ephemeris**: Astronomical calculations
- **OpenAI API**: AI-powered interpretations
- **Uvicorn**: ASGI server

### Frontend
- **Next.js**: React framework
- **Tailwind CSS**: Styling
- **Custom Components**: Astrology-specific UI elements

### Astronomical Calculations
- **Ayanamsa**: Lahiri (Vedic)
- **House System**: Placidus
- **Ephemeris**: Swiss Ephemeris
- **Dasa System**: Vimshottari

## 📁 Project Structure

```
AI-Astrology/
├── astro-backend/
│   ├── astro-backend/
│   │   ├── main.py              # FastAPI application
│   │   ├── astrology.py         # Planetary calculations
│   │   ├── carear.py           # Career analysis
│   │   ├── dasa.py             # Dasa calculations
│   │   ├── validation.py       # Input validation
│   │   └── start_production.py # Production server
│   ├── requirements.txt         # Python dependencies
│   └── build.sh               # Render build script
├── astro-frontend/
│   ├── pages/
│   │   └── index.js           # Main application
│   ├── package.json           # Node.js dependencies
│   └── vercel.json           # Vercel configuration
└── README.md                 # This file
```

## 🔧 Configuration

### Environment Variables

#### Backend (Render)
```bash
OPENAI_API_KEY=your_openai_api_key_here
ALLOWED_ORIGINS=https://your-frontend-domain.vercel.app
PORT=8000
HOST=0.0.0.0
```

#### Frontend (Vercel)
```bash
NEXT_PUBLIC_BACKEND_URL=https://your-backend-domain.onrender.com
```

## 🐛 Troubleshooting

### Common Issues

1. **Backend not starting**
   - Ensure all dependencies are installed
   - Check if port 8000 is available
   - Verify OpenAI API key is correctly set

2. **Frontend not connecting to backend**
   - Ensure backend is running
   - Check CORS settings
   - Verify network connectivity

3. **API errors**
   - Check OpenAI API key validity
   - Ensure sufficient API credits
   - Verify birth data format

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Swiss Ephemeris for astronomical calculations
- OpenAI for AI-powered interpretations
- Vedic astrology community for knowledge sharing

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Verify all dependencies are correctly installed
3. Ensure proper API key configuration
4. Check console logs for error messages

---

⭐ **Star this repository if you find it helpful!** 